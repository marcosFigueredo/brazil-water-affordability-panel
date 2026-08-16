"""
Testa a robustez do achado central (Modelo 1: planejamento nao explica ICR-SM,
variacao e ~85% between / ~0% within) a escolhas alternativas de especificacao:

  (a) variaveis de planejamento CONTEMPORANEAS em vez de defasadas
  (b) janela de CV do investimento em 3 anos em vez de 5
  (c) janela de CV do investimento em 10 anos em vez de 5

Se o padrao (nenhuma variavel significativa, R2 within ~0) se mantiver nas
tres alternativas, o achado central fica mais defensavel. Se mudar, precisa
ser revisto antes de virar afirmacao no artigo.

Entrada: br_painel_analise_final.csv
Saida: robustez_modelo1.txt, robustez_modelo1_resumo.csv
"""
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")
df = df.sort_values(["id_municipio", "ano"])

# --- CV de investimento em janelas alternativas (3 e 10 anos) ---
def cv_trailing(s, window):
    roll_mean = s.rolling(window, min_periods=max(3, window // 2)).mean()
    roll_std = s.rolling(window, min_periods=max(3, window // 2)).std()
    return (roll_std / roll_mean).replace([np.inf, -np.inf], np.nan)

df["cv_investimento_3a"] = df.groupby("id_municipio")["investimento_percapita"].transform(lambda s: cv_trailing(s, 3))
df["cv_investimento_10a"] = df.groupby("id_municipio")["investimento_percapita"].transform(lambda s: cv_trailing(s, 10))
df["cv_investimento_3a_lag1"] = df.groupby("id_municipio")["cv_investimento_3a"].shift(1)
df["cv_investimento_10a_lag1"] = df.groupby("id_municipio")["cv_investimento_10a"].shift(1)

df_idx = df.set_index(["id_municipio", "ano"])

especificacoes = {
    "Original (defasado, CV 5a)": [
        "investimento_percapita_lag1", "cv_investimento_5a_lag1",
        "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
        "log_populacao_urbana",
    ],
    "(a) Contemporaneo (sem defasagem)": [
        "investimento_percapita", "cv_investimento_5a",
        "prop_financiamento_oneroso", "indice_perda_faturamento",
        "log_populacao_urbana",
    ],
    "(b) Defasado, CV janela 3 anos": [
        "investimento_percapita_lag1", "cv_investimento_3a_lag1",
        "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
        "log_populacao_urbana",
    ],
    "(c) Defasado, CV janela 10 anos": [
        "investimento_percapita_lag1", "cv_investimento_10a_lag1",
        "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
        "log_populacao_urbana",
    ],
}

linhas_resumo = []
saida_txt = []

for nome, cols in especificacoes.items():
    d = df_idx[["ICR_SM"] + cols].dropna()
    mod = PanelOLS(d["ICR_SM"], d[cols], entity_effects=True, time_effects=True, drop_absorbed=True)
    res = mod.fit(cov_type="clustered", cluster_entity=True)

    header = f"\n{'='*70}\n{nome} | N={len(d)} | municipios={d.index.get_level_values(0).nunique()}\n{'='*70}"
    print(header)
    print(res.summary)
    saida_txt.append(header)
    saida_txt.append(str(res.summary))

    n_sig = (res.pvalues < 0.05).sum()
    linhas_resumo.append({
        "especificacao": nome,
        "N": len(d),
        "municipios": d.index.get_level_values(0).nunique(),
        "r2_between": res.rsquared_between,
        "r2_within": res.rsquared_within,
        "n_variaveis_significativas": n_sig,
        "variaveis_significativas": ", ".join(res.pvalues[res.pvalues < 0.05].index.tolist()) or "(nenhuma)",
    })

resumo = pd.DataFrame(linhas_resumo)
print("\n\n=== RESUMO COMPARATIVO DAS 4 ESPECIFICACOES ===")
print(resumo.to_string(index=False))

resumo.to_csv(f"{BASE}\\robustez_modelo1_resumo.csv", index=False, encoding="utf-8")
with open(f"{BASE}\\robustez_modelo1.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(saida_txt))
    f.write("\n\n=== RESUMO COMPARATIVO ===\n")
    f.write(resumo.to_string(index=False))

print("\nSalvos: robustez_modelo1.txt, robustez_modelo1_resumo.csv")
