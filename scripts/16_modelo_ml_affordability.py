"""
Modelos de ML para prever ICR-SM (affordability) um passo a frente e projetar
recursivamente ate 2033, espelhando o desenho do script 09 (que faz o mesmo
para cobertura). Isso responde a um gap apontado por revisao externa, o
exercicio original de ML preve cobertura, nao affordability, entao nao valida
diretamente o resultado do modelo de painel sobre affordability.

Dois modelos sao comparados, gradient boosting (HistGradientBoostingRegressor,
lida nativamente com NaN e variavel categorica) e Random Forest
(RandomForestRegressor, requer one-hot e imputacao, mas e uma familia de
ensemble de arvore diferente, bagging em vez de boosting, o que serve como
checagem de robustez independente do resultado). Uma LSTM foi considerada e
descartada, cada municipio tem no maximo ~27 pontos anuais, sequencia curta
demais para uma rede recorrente aprender padrao temporal sem overfitar.

A expectativa de crescimento populacional usada no forecast recursivo tambem
foi trocada aqui, do CAGR historico de cada municipio dentro do proprio
painel SNIS (que nao captura a desaceleracao demografica brasileira) para a
projecao oficial de populacao do IBGE por UF 2022-2033 (script 20).

Desenho:
1) Forecast de 1 passo a frente (t-1 -> t): treina os dois modelos em anos
   <=2016, testa em 2017-2022, compara contra dois baselines (persistencia
   do ICR-SM e extrapolacao linear por municipio) no MESMO conjunto de teste.
2) Ablation por permutation importance no holdout (gradient boosting).
3) Salva previsoes individuais do holdout para grafico previsto vs observado.
4) Forecast recursivo 2023->2033 por municipio para os DOIS modelos, usando
   a projecao oficial de populacao do IBGE por UF como expectativa de
   crescimento populacional.

Entrada: br_painel_analise_final.csv, br_expectativa_crescimento_uf_ibge.csv
Saida: holdout_predicoes_ml_icr.csv, validacao_ml_icr.csv,
       importancia_features_ml_icr.csv, br_projecao_icr_2033_ml.csv,
       br_projecao_icr_2033_rf.csv
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.inspection import permutation_importance

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")
pop_ibge_uf = pd.read_csv(f"{BASE}\\br_expectativa_crescimento_uf_ibge.csv")

TARGET = "ICR_SM"

# ============================================================
# 1) monta features de 1 passo a frente: X em t-1 -> y em t
# ============================================================
df = df.sort_values(["id_municipio", "ano"])
df["icr_sm_lag1"] = df.groupby("id_municipio")[TARGET].shift(1)

FEATURES = [
    "icr_sm_lag1", "ano",
    "investimento_percapita_lag1", "cv_investimento_5a_lag1",
    "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
    "log_populacao_urbana", "log_pib_per_capita",
    "crescimento_populacional_pct_aa", "crescimento_va_servicos_pct_aa",
    "anomalia_precipitacao_pct",
]
CAT_FEATURES = ["regiao"]
X_cols = FEATURES + CAT_FEATURES

modelo_df = df.dropna(subset=[TARGET, "icr_sm_lag1"]).copy()
for c in CAT_FEATURES:
    modelo_df[c] = modelo_df[c].astype("category")

treino = modelo_df[modelo_df["ano"] <= 2016]
teste = modelo_df[(modelo_df["ano"] >= 2017) & (modelo_df["ano"] <= 2022)]

print(f"Treino: {len(treino)} obs (anos <=2016) | Teste: {len(teste)} obs (2017-2022)")

# ---------------- gradient boosting (lida nativamente com NaN/categorica) ----------------
modelo_gb = HistGradientBoostingRegressor(
    max_iter=300, max_depth=6, learning_rate=0.05,
    categorical_features=[X_cols.index(c) for c in CAT_FEATURES],
    random_state=42,
)
modelo_gb.fit(treino[X_cols], treino[TARGET])
pred_gb = modelo_gb.predict(teste[X_cols])

# ---------------- random forest (precisa one-hot + imputacao) ----------------
def prepara_rf(frame, medianas=None, colunas_ref=None):
    X = pd.get_dummies(frame[X_cols], columns=CAT_FEATURES)
    if colunas_ref is not None:
        X = X.reindex(columns=colunas_ref, fill_value=0)
    if medianas is None:
        medianas = X.median()
    X = X.fillna(medianas)
    return X, medianas

X_treino_rf, medianas_rf = prepara_rf(treino)
X_teste_rf, _ = prepara_rf(teste, medianas=medianas_rf, colunas_ref=X_treino_rf.columns)

modelo_rf = RandomForestRegressor(
    n_estimators=300, max_depth=12, min_samples_leaf=5,
    random_state=42, n_jobs=-1,
)
modelo_rf.fit(X_treino_rf, treino[TARGET])
pred_rf = modelo_rf.predict(X_teste_rf)

pred_persistencia = teste["icr_sm_lag1"].values  # baseline ingenuo: repete o ultimo valor

# baseline de extrapolacao linear: para cada municipio-ano de teste, ajusta reta
# usando o HISTORICO COMPLETO do municipio restrito a anos <=2016 e extrapola
print("Calculando baseline de extrapolacao linear (pode demorar um pouco)...")
historico_completo = df[df["ano"] <= 2016][["id_municipio", "ano", TARGET]].dropna(subset=[TARGET])
hist_por_municipio = {mun: g[["ano", TARGET]].values for mun, g in historico_completo.groupby("id_municipio")}

def prever_linear(mun, ano_alvo):
    h = hist_por_municipio.get(mun)
    if h is None or len(h) < 3:
        return np.nan
    slope, intercept = np.polyfit(h[:, 0], h[:, 1], 1)
    return slope * ano_alvo + intercept

pred_linear = pd.Series(
    [prever_linear(mun, ano) for mun, ano in zip(teste["id_municipio"], teste["ano"])],
    index=teste.index,
)

# ============================================================
# 2) avaliacao: MAE e RMSE dos 4 metodos no mesmo conjunto de teste
# ============================================================
y_true = teste[TARGET].values
valid_linear = pred_linear.notna()

resultados_validacao = pd.DataFrame({
    "metodo": ["Gradient Boosting (ML)", "Random Forest (ML)", "Persistencia (repete ultimo valor)", "Extrapolacao linear por municipio"],
    "MAE": [
        mean_absolute_error(y_true, pred_gb),
        mean_absolute_error(y_true, pred_rf),
        mean_absolute_error(y_true, pred_persistencia),
        mean_absolute_error(y_true[valid_linear], pred_linear[valid_linear]),
    ],
    "RMSE": [
        np.sqrt(mean_squared_error(y_true, pred_gb)),
        np.sqrt(mean_squared_error(y_true, pred_rf)),
        np.sqrt(mean_squared_error(y_true, pred_persistencia)),
        np.sqrt(mean_squared_error(y_true[valid_linear], pred_linear[valid_linear])),
    ],
    "N_teste": [len(y_true), len(y_true), len(y_true), int(valid_linear.sum())],
})

holdout_predicoes = pd.DataFrame({
    "id_municipio": teste["id_municipio"].values,
    "ano": teste["ano"].values,
    "regiao": teste["regiao"].values,
    "observado": y_true,
    "previsto_ml": pred_gb,
    "previsto_rf": pred_rf,
    "previsto_persistencia": pred_persistencia,
    "previsto_linear": pred_linear.values,
})
holdout_predicoes.to_csv(f"{BASE}\\holdout_predicoes_ml_icr.csv", index=False, encoding="utf-8")
print(f"Previsoes do holdout salvas: holdout_predicoes_ml_icr.csv ({len(holdout_predicoes)} linhas)")

print("\n=== Validacao 1-passo-a-frente (2017-2022), ICR-SM, 4 metodos ===")
print(resultados_validacao.round(3).to_string(index=False))
resultados_validacao.to_csv(f"{BASE}\\validacao_ml_icr.csv", index=False)

print("\n=== Importancia das features (permutation importance, holdout, gradient boosting) ===")
try:
    perm = permutation_importance(modelo_gb, teste[X_cols], teste[TARGET], n_repeats=5, random_state=42, n_jobs=-1)
    imp = pd.DataFrame({"feature": X_cols, "importancia": perm.importances_mean}).sort_values("importancia", ascending=False)
    print(imp.round(4).to_string(index=False))
    imp.to_csv(f"{BASE}\\importancia_features_ml_icr.csv", index=False)
except Exception as e:
    print("Erro no calculo de importancia:", e)

print("\nArquivos salvos: holdout_predicoes_ml_icr.csv, validacao_ml_icr.csv, importancia_features_ml_icr.csv")

# ============================================================
# 3) forecast recursivo 2023 -> 2033 por municipio (ICR-SM), 2 modelos
# ============================================================
print("\nRodando forecast recursivo 2023->2033 para ICR-SM, gradient boosting e random forest (pode demorar)...")

ultimo_ano_obs = df[df["ano"] <= 2022].dropna(subset=[TARGET]).groupby("id_municipio").apply(
    lambda g: g.sort_values("ano").iloc[-1], include_groups=False
).reset_index()

estado = ultimo_ano_obs.set_index("id_municipio").copy()
estado = estado.merge(pop_ibge_uf[["sigla_uf", "expectativa_crescimento_populacional_ibge_pct_aa"]], on="sigla_uf", how="left")
estado.index = ultimo_ano_obs["id_municipio"].values
# municipios sem correspondencia de UF (nao deveria ocorrer) usam a media nacional do IBGE
media_ibge = pop_ibge_uf["expectativa_crescimento_populacional_ibge_pct_aa"].mean()
estado["expectativa_crescimento_populacional_ibge_pct_aa"] = estado["expectativa_crescimento_populacional_ibge_pct_aa"].fillna(media_ibge)

ANO_META = 2033

def roda_recursivo(nome_modelo, predict_fn):
    est = estado.copy()
    est["icr_atual"] = est[TARGET]
    resultado = {}
    for ano_fut in range(2023, ANO_META + 1):
        linha = pd.DataFrame({
            "icr_sm_lag1": est["icr_atual"],
            "ano": ano_fut,
            "investimento_percapita_lag1": est["investimento_percapita_lag1"],
            "cv_investimento_5a_lag1": est["cv_investimento_5a_lag1"],
            "prop_financiamento_oneroso_lag1": est["prop_financiamento_oneroso_lag1"],
            "indice_perda_faturamento_lag1": est["indice_perda_faturamento_lag1"],
            "log_populacao_urbana": est["log_populacao_urbana"],
            "log_pib_per_capita": est["log_pib_per_capita"],
            # projecao oficial de populacao do IBGE por UF (2022-2033), no lugar do
            # CAGR historico do proprio municipio usado antes
            "crescimento_populacional_pct_aa": est["expectativa_crescimento_populacional_ibge_pct_aa"],
            "crescimento_va_servicos_pct_aa": est["expectativa_crescimento_va_servicos_pct_aa"],
            "anomalia_precipitacao_pct": 0.0,
            "regiao": est["regiao"].astype("category"),
        }, index=est.index)
        pred = predict_fn(linha)
        pred = np.clip(pred, 0, 100)
        est["icr_atual"] = pred
        resultado[ano_fut] = pred.copy()
    proj = pd.DataFrame(resultado, index=est.index)
    proj["icr_sm_2022"] = est[TARGET]
    proj[f"projecao_icr_2033_{nome_modelo}"] = proj[ANO_META]
    proj["variacao_pp_2022_2033"] = proj[f"projecao_icr_2033_{nome_modelo}"] - proj["icr_sm_2022"]
    proj["regiao"] = est["regiao"]
    proj["porte"] = est["porte"]
    proj["sigla_uf"] = est["sigla_uf"]
    proj = proj.reset_index().rename(columns={"index": "id_municipio"})
    return proj

proj_gb = roda_recursivo("ml", lambda linha: modelo_gb.predict(linha[X_cols]))

def predict_rf(linha):
    X_linha, _ = prepara_rf(linha, medianas=medianas_rf, colunas_ref=X_treino_rf.columns)
    return modelo_rf.predict(X_linha)

proj_rf = roda_recursivo("rf", predict_rf)

LIMITE_INTERNACIONAL = 5.0  # limite superior da faixa internacional de affordability (3-5%) usada no artigo
for nome, proj, col in [("Gradient Boosting", proj_gb, "projecao_icr_2033_ml"), ("Random Forest", proj_rf, "projecao_icr_2033_rf")]:
    proj["acima_limite_internacional_2033"] = proj[col] > LIMITE_INTERNACIONAL
    print(f"\n=== {nome}: ICR-SM nacional projetado para 2033 (media dos municipios) ===")
    print(f"Media 2022 (ultimo ano observado por municipio): {proj['icr_sm_2022'].mean():.2f}%")
    print(f"Media projetada 2033: {proj[col].mean():.2f}%")
    print(f"Variacao media: {proj['variacao_pp_2022_2033'].mean():+.2f} p.p.")
    print(f"Municipios acima do limite internacional (5%) em 2033: {proj['acima_limite_internacional_2033'].mean()*100:.1f}%")
    print("Por regiao, media projetada 2033 (%):")
    print(proj.groupby("regiao")[col].mean().round(2))

proj_gb.to_csv(f"{BASE}\\br_projecao_icr_2033_ml.csv", index=False, encoding="utf-8")
proj_rf.to_csv(f"{BASE}\\br_projecao_icr_2033_rf.csv", index=False, encoding="utf-8")
print("\nArquivos salvos: br_projecao_icr_2033_ml.csv, br_projecao_icr_2033_rf.csv")
