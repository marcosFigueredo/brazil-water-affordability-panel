"""
Modelo de painel com efeitos fixos duplos (municipio + ano), erro clusterizado
por municipio, para testar H1/H2 (planejamento defasado -> ICR_SM), H3
(cobertura x regiao -> ICR_SM) e H4 (pressao de crescimento -> ICR_SM e ->
cobertura).

Requer: pip install linearmodels

Entrada: br_painel_analise_final.csv
Saida: resultados_modelo_painel.txt
"""
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")

for r in ["Norte", "Nordeste", "Centro-Oeste", "Sul"]:
    df[f"cobertura_x_{r.replace('-', '')}"] = np.where(
        df["regiao"] == r, df["indice_atendimento_urbano_agua"], 0.0
    )

df = df.set_index(["id_municipio", "ano"])

# ===================== MODELO 1 (H1+H2) =====================
cols_m1 = ["ICR_SM", "investimento_percapita_lag1", "cv_investimento_5a_lag1",
           "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
           "log_populacao_urbana"]
d1 = df[cols_m1].dropna()
mod1 = PanelOLS(
    d1["ICR_SM"],
    d1[["investimento_percapita_lag1", "cv_investimento_5a_lag1",
        "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
        "log_populacao_urbana"]],
    entity_effects=True, time_effects=True, drop_absorbed=True,
)
res1 = mod1.fit(cov_type="clustered", cluster_entity=True)

# ===================== MODELO 2 (H3) =====================
cols_m2 = ["ICR_SM", "indice_atendimento_urbano_agua",
           "cobertura_x_Norte", "cobertura_x_Nordeste", "cobertura_x_CentroOeste", "cobertura_x_Sul",
           "log_populacao_urbana"]
d2 = df[cols_m2].dropna()
mod2 = PanelOLS(
    d2["ICR_SM"],
    d2[["indice_atendimento_urbano_agua", "cobertura_x_Norte", "cobertura_x_Nordeste",
        "cobertura_x_CentroOeste", "cobertura_x_Sul", "log_populacao_urbana"]],
    entity_effects=True, time_effects=True, drop_absorbed=True,
)
res2 = mod2.fit(cov_type="clustered", cluster_entity=True)

# ===================== MODELO 3 (H4 -> ICR_SM) =====================
cols_m3 = ["ICR_SM", "investimento_percapita_lag1", "cv_investimento_5a_lag1",
           "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
           "log_populacao_urbana", "log_pib_per_capita",
           "crescimento_populacional_pct_aa", "crescimento_va_servicos_pct_aa",
           "anomalia_precipitacao_pct"]
d3 = df[cols_m3].dropna()
mod3 = PanelOLS(d3["ICR_SM"], d3.drop(columns=["ICR_SM"]),
                 entity_effects=True, time_effects=True, drop_absorbed=True)
res3 = mod3.fit(cov_type="clustered", cluster_entity=True)

# ===================== MODELO 4 (H4 -> cobertura, trade-off) =====================
cols_m4 = ["indice_atendimento_urbano_agua", "investimento_percapita_lag1",
           "cv_investimento_5a_lag1", "prop_financiamento_oneroso_lag1",
           "log_populacao_urbana", "crescimento_populacional_pct_aa",
           "crescimento_va_servicos_pct_aa"]
d4 = df[cols_m4].dropna()
mod4 = PanelOLS(d4["indice_atendimento_urbano_agua"], d4.drop(columns=["indice_atendimento_urbano_agua"]),
                 entity_effects=True, time_effects=True, drop_absorbed=True)
res4 = mod4.fit(cov_type="clustered", cluster_entity=True)

with open(f"{BASE}\\resultados_modelo_painel.txt", "w", encoding="utf-8") as f:
    for nome, res, d in [
        ("MODELO 1 (H1+H2): planejamento defasado -> ICR_SM", res1, d1),
        ("MODELO 2 (H3): cobertura x regiao -> ICR_SM (baseline regiao = Sudeste)", res2, d2),
        ("MODELO 3 (H4): pressao de crescimento -> ICR_SM", res3, d3),
        ("MODELO 4 (H4, trade-off): pressao de crescimento -> cobertura de agua", res4, d4),
    ]:
        n = len(d)
        nmuni = d.index.get_level_values(0).nunique()
        header = f"{'='*70}\n{nome} | N={n} | municipios={nmuni}\n{'='*70}\n"
        print(header)
        print(res.summary)
        f.write(header)
        f.write(str(res.summary))
        f.write("\n\n")

print("\nResultados salvos em resultados_modelo_painel.txt")
