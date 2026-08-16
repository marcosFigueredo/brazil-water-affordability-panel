"""
Modelo de ML (gradient boosting) para projetar cobertura de agua ate 2033,
conforme decidido no plano (Modelo de painel + ML, com extrapolacao linear
como baseline de comparacao) -- este script estava faltando na execucao
original e foi adicionado apos o usuario notar a lacuna.

Desenho:
1) Forecast de 1 passo a frente (t-1 -> t): treina HistGradientBoostingRegressor
   em anos <=2016, testa em 2017-2022, compara contra dois baselines (persistencia
   e extrapolacao linear por municipio) no MESMO conjunto de teste.
2) Forecast recursivo 2023->2033: aplica o modelo treinado iterativamente,
   realimentando a previsao de cada ano como "cobertura_lag1" do ano seguinte.
   Para features que nao existem no futuro (crescimento, investimento), usa
   a expectativa de crescimento de longo prazo (CAGR historico) ja calculada,
   ou o ultimo valor observado (persistencia), com a suposicao declarada
   explicitamente.
3) Compara a classificacao 2033 resultante (on_track/at_risk/will_not_meet)
   contra a da extrapolacao linear simples (script 06), para ver se os dois
   metodos concordam.

Entrada: br_painel_analise_final.csv, br_expectativa_crescimento_municipio.csv,
         br_projecao_cobertura_2033.csv (extrapolacao linear, p/ comparar)
Saida: br_projecao_2033_ml.csv, comparacao_metodos_2033.csv
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")

TARGET = "indice_atendimento_urbano_agua"
ANO_META = 2033
META_AGUA = 99.0

# ============================================================
# 1) monta features de 1 passo a frente: X em t-1 -> y em t
# ============================================================
df = df.sort_values(["id_municipio", "ano"])
df["cobertura_lag1"] = df.groupby("id_municipio")[TARGET].shift(1)

FEATURES = [
    "cobertura_lag1", "ano",
    "investimento_percapita_lag1", "cv_investimento_5a_lag1",
    "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
    "log_populacao_urbana", "log_pib_per_capita",
    "crescimento_populacional_pct_aa", "crescimento_va_servicos_pct_aa",
    "anomalia_precipitacao_pct",
]
CAT_FEATURES = ["regiao"]

modelo_df = df.dropna(subset=[TARGET, "cobertura_lag1"]).copy()
for c in CAT_FEATURES:
    modelo_df[c] = modelo_df[c].astype("category")

X_cols = FEATURES + CAT_FEATURES
treino = modelo_df[modelo_df["ano"] <= 2016]
teste = modelo_df[(modelo_df["ano"] >= 2017) & (modelo_df["ano"] <= 2022)]

print(f"Treino: {len(treino)} obs (anos <=2016) | Teste: {len(teste)} obs (2017-2022)")

modelo = HistGradientBoostingRegressor(
    max_iter=300, max_depth=6, learning_rate=0.05,
    categorical_features=[X_cols.index(c) for c in CAT_FEATURES],
    random_state=42,
)
modelo.fit(treino[X_cols], treino[TARGET])

pred_ml = modelo.predict(teste[X_cols])
pred_persistencia = teste["cobertura_lag1"].values  # baseline ingenuo: repete o ultimo valor

# baseline de extrapolacao linear: para cada municipio-ano de teste, ajusta reta
# usando o HISTORICO COMPLETO do municipio (do painel inteiro, nao so do
# subconjunto de teste) restrito a anos <=2016 (nao usa dado futuro) e extrapola
# ate o ano de teste -- bug corrigido: a 1a versao buscava historico dentro do
# proprio "teste" (que so tem 2017-2022), entao nunca achava >=3 anos anteriores
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
# 2) avaliacao: MAE e RMSE dos 3 metodos no mesmo conjunto de teste
# ============================================================
y_true = teste[TARGET].values
valid_linear = pred_linear.notna()

resultados_validacao = pd.DataFrame({
    "metodo": ["Gradient Boosting (ML)", "Persistencia (repete ultimo valor)", "Extrapolacao linear por municipio"],
    "MAE": [
        mean_absolute_error(y_true, pred_ml),
        mean_absolute_error(y_true, pred_persistencia),
        mean_absolute_error(y_true[valid_linear], pred_linear[valid_linear]),
    ],
    "RMSE": [
        np.sqrt(mean_squared_error(y_true, pred_ml)),
        np.sqrt(mean_squared_error(y_true, pred_persistencia)),
        np.sqrt(mean_squared_error(y_true[valid_linear], pred_linear[valid_linear])),
    ],
    "N_teste": [len(y_true), len(y_true), int(valid_linear.sum())],
})

# salva as previsoes individuais do conjunto de teste (holdout), para grafico
# previsto vs observado -- nao apenas as metricas agregadas
holdout_predicoes = pd.DataFrame({
    "id_municipio": teste["id_municipio"].values,
    "ano": teste["ano"].values,
    "regiao": teste["regiao"].values,
    "observado": y_true,
    "previsto_ml": pred_ml,
    "previsto_persistencia": pred_persistencia,
    "previsto_linear": pred_linear.values,
})
holdout_predicoes.to_csv(f"{BASE}\\holdout_predicoes_ml.csv", index=False, encoding="utf-8")
print(f"Previsoes do holdout salvas: holdout_predicoes_ml.csv ({len(holdout_predicoes)} linhas)")

print("\n=== Validacao 1-passo-a-frente (2017-2022), 3 metodos ===")
print(resultados_validacao.round(3).to_string(index=False))
resultados_validacao.to_csv(f"{BASE}\\validacao_ml_vs_linear.csv", index=False)

# importancia das features (permutation nao calculada por custo; usa a nativa do modelo)
import io
print("\n=== Importancia das features (gain-based, HistGradientBoosting) ===")
try:
    from sklearn.inspection import permutation_importance
    perm = permutation_importance(modelo, teste[X_cols], teste[TARGET], n_repeats=5, random_state=42, n_jobs=-1)
    imp = pd.DataFrame({"feature": X_cols, "importancia": perm.importances_mean}).sort_values("importancia", ascending=False)
    print(imp.round(4).to_string(index=False))
    imp.to_csv(f"{BASE}\\importancia_features_ml.csv", index=False)
except Exception as e:
    print("Erro no calculo de importancia:", e)

# ============================================================
# 3) forecast recursivo 2023 -> 2033 por municipio
# ============================================================
print("\nRodando forecast recursivo 2023->2033 (pode demorar)...")

# nota: br_painel_analise_final.csv ja tem as colunas de expectativa de
# crescimento mescladas (script 03) -- nao precisa mesclar de novo aqui
ultimo_ano_obs = df[df["ano"] <= 2022].groupby("id_municipio").apply(
    lambda g: g.sort_values("ano").iloc[-1], include_groups=False
).reset_index()

estado = ultimo_ano_obs.set_index("id_municipio").copy()

# usa cobertura observada em 2022 (ou ultimo ano disponivel) como ponto de partida
estado["cobertura_atual"] = estado[TARGET]
resultado_recursivo = {}

for ano_fut in range(2023, ANO_META + 1):
    linha = pd.DataFrame({
        "cobertura_lag1": estado["cobertura_atual"],
        "ano": ano_fut,
        "investimento_percapita_lag1": estado["investimento_percapita_lag1"],
        "cv_investimento_5a_lag1": estado["cv_investimento_5a_lag1"],
        "prop_financiamento_oneroso_lag1": estado["prop_financiamento_oneroso_lag1"],
        "indice_perda_faturamento_lag1": estado["indice_perda_faturamento_lag1"],
        "log_populacao_urbana": estado["log_populacao_urbana"],
        "log_pib_per_capita": estado["log_pib_per_capita"],
        "crescimento_populacional_pct_aa": estado["expectativa_crescimento_populacional_pct_aa"],
        "crescimento_va_servicos_pct_aa": estado["expectativa_crescimento_va_servicos_pct_aa"],
        "anomalia_precipitacao_pct": 0.0,
        "regiao": estado["regiao"].astype("category"),
    }, index=estado.index)
    pred = modelo.predict(linha[X_cols])
    pred = np.clip(pred, 0, 100)
    estado["cobertura_atual"] = pred
    resultado_recursivo[ano_fut] = pred.copy()

proj_ml = pd.DataFrame(resultado_recursivo, index=estado.index)
proj_ml["projecao_2033_ml"] = proj_ml[ANO_META]

def classifica(p, meta=META_AGUA):
    if pd.isna(p):
        return np.nan
    if p >= meta:
        return "on_track"
    elif p >= meta - 10:
        return "at_risk"
    else:
        return "will_not_meet"

proj_ml["classificacao_2033_ml"] = proj_ml["projecao_2033_ml"].apply(classifica)
proj_ml = proj_ml.reset_index().rename(columns={"index": "id_municipio"})

print("\n=== Distribuicao classificacao 2033 -- MODELO ML ===")
print(proj_ml["classificacao_2033_ml"].value_counts(dropna=False))

proj_ml[["id_municipio", "projecao_2033_ml", "classificacao_2033_ml"]].to_csv(
    f"{BASE}\\br_projecao_cobertura_2033_ml.csv", index=False, encoding="utf-8"
)

# ============================================================
# 4) compara com a extrapolacao linear (script 06)
# ============================================================
proj_linear = pd.read_csv(f"{BASE}\\br_projecao_cobertura_2033.csv")[["id_municipio", "classificacao_2033", "projecao_2033"]]
comp = proj_ml.merge(proj_linear, on="id_municipio", how="inner").dropna(
    subset=["classificacao_2033_ml", "classificacao_2033"]
)
print(f"\n=== Concordancia ML vs. extrapolacao linear (N={len(comp)}) ===")
tab_concordancia = pd.crosstab(comp["classificacao_2033"], comp["classificacao_2033_ml"])
print(tab_concordancia)
taxa_concordancia = (comp["classificacao_2033"] == comp["classificacao_2033_ml"]).mean()
print(f"\nTaxa de concordancia exata: {taxa_concordancia*100:.1f}%")

diff_media = (comp["projecao_2033_ml"] - comp["projecao_2033"]).abs().mean()
print(f"Diferenca media absoluta entre as duas projecoes de nivel: {diff_media:.2f} pontos")

comp.to_csv(f"{BASE}\\comparacao_metodos_2033.csv", index=False, encoding="utf-8")
print("\nArquivos salvos: br_projecao_cobertura_2033_ml.csv, comparacao_metodos_2033.csv, validacao_ml_vs_linear.csv")
