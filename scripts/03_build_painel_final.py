"""
Une todas as bases (SNIS+ICR_SM, salario minimo, PIB/populacao, crescimento,
expectativa de crescimento, clima) num unico painel municipio-ano, e constroi
as variaveis de planejamento (investimento per capita, CV de 5 anos, proporcao
de financiamento oneroso) defasadas em 1 ano para o modelo preditivo.

Entrada: br_mdr_snis_municipio_agua_esgoto.csv, salario_minimo_1995_2022.csv,
         br_ibge_pib_populacao_municipio.csv,
         br_crescimento_populacao_pib_servicos_municipio.csv,
         br_expectativa_crescimento_municipio.csv, br_clima_precipitacao_uf.csv

Saida: br_painel_analise_final.csv
"""
import pandas as pd
import numpy as np

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"

snis = pd.read_csv(f"{BASE}\\br_mdr_snis_municipio_agua_esgoto.csv")
sm = pd.read_csv(f"{BASE}\\salario_minimo_1995_2022.csv")
pib_pop = pd.read_csv(f"{BASE}\\br_ibge_pib_populacao_municipio.csv")
cresc = pd.read_csv(f"{BASE}\\br_crescimento_populacao_pib_servicos_municipio.csv")
expect = pd.read_csv(f"{BASE}\\br_expectativa_crescimento_municipio.csv")
clima = pd.read_csv(f"{BASE}\\br_clima_precipitacao_uf.csv")

# ============ 1) ICR_SM ============
df = snis.merge(sm[["ano", "salario_minimo_media_ponderada_ano"]], on="ano", how="left")
receita_total = df["receita_operacional_direta_agua"].fillna(0) + df["receita_operacional_direta_esgoto"].fillna(0)
economias = df["quantidade_economia_residencial_ativa_agua"]
df["tarifa_media_mensal_residencial"] = np.where(
    (economias.notna()) & (economias > 0), (receita_total / economias) / 12, np.nan
)
df["ICR_SM"] = df["tarifa_media_mensal_residencial"] / df["salario_minimo_media_ponderada_ano"] * 100
df["ICR_SM"] = df["ICR_SM"].where((df["ICR_SM"] >= 0) & (df["ICR_SM"] <= 100))

# ============ 2) regiao / porte ============
regiao_map = {
    "AC": "Norte", "AP": "Norte", "AM": "Norte", "PA": "Norte", "RO": "Norte", "RR": "Norte", "TO": "Norte",
    "AL": "Nordeste", "BA": "Nordeste", "CE": "Nordeste", "MA": "Nordeste", "PB": "Nordeste",
    "PE": "Nordeste", "PI": "Nordeste", "RN": "Nordeste", "SE": "Nordeste",
    "DF": "Centro-Oeste", "GO": "Centro-Oeste", "MT": "Centro-Oeste", "MS": "Centro-Oeste",
    "ES": "Sudeste", "MG": "Sudeste", "RJ": "Sudeste", "SP": "Sudeste",
    "PR": "Sul", "RS": "Sul", "SC": "Sul",
}
df["regiao"] = df["sigla_uf"].map(regiao_map)
bins = [0, 5000, 20000, 50000, 100000, 500000, np.inf]
labels = ["<5 mil", "5-20 mil", "20-50 mil", "50-100 mil", "100-500 mil", "500 mil+"]
df["porte"] = pd.cut(df["populacao_urbana"], bins=bins, labels=labels)

# ============ 3) planejamento: investimento per capita, CV 5 anos, financiamento oneroso ============
df = df.sort_values(["id_municipio", "ano"])
df["investimento_percapita"] = df["investimento_total_prestador"] / df["populacao_atendida_agua"]
df["investimento_percapita"] = df["investimento_percapita"].replace([np.inf, -np.inf], np.nan)

df["prop_financiamento_oneroso"] = (
    df["investimento_recurso_oneroso_prestador"] / df["investimento_total_prestador"]
).replace([np.inf, -np.inf], np.nan)
df.loc[df["investimento_total_prestador"] <= 0, "prop_financiamento_oneroso"] = np.nan

def cv_trailing(s, window=5):
    roll_mean = s.rolling(window, min_periods=3).mean()
    roll_std = s.rolling(window, min_periods=3).std()
    return (roll_std / roll_mean).replace([np.inf, -np.inf], np.nan)

df["cv_investimento_5a"] = df.groupby("id_municipio")["investimento_percapita"].transform(cv_trailing)

# ============ 4) merge PIB / populacao (IBGE) ============
pib_pop_slim = pib_pop[["id_municipio", "ano", "pib_per_capita_reais"]]
df = df.merge(pib_pop_slim, on=["id_municipio", "ano"], how="left")
df["log_pib_per_capita"] = np.log(df["pib_per_capita_reais"].where(df["pib_per_capita_reais"] > 0))

# ============ 5) merge crescimento ============
cresc_slim = cresc[["id_municipio", "ano", "crescimento_populacional_pct_aa",
                     "crescimento_pib_per_capita_pct_aa", "crescimento_va_servicos_pct_aa"]]
df = df.merge(cresc_slim, on=["id_municipio", "ano"], how="left")

# ============ 6) merge expectativa (time-invariant por municipio) ============
df = df.merge(expect, on="id_municipio", how="left")

# ============ 7) merge clima por UF-ano ============
clima_slim = clima[["sigla_uf", "ano", "anomalia_precipitacao_pct"]]
df = df.merge(clima_slim, on=["sigla_uf", "ano"], how="left")

# ============ 8) log populacao ============
df["log_populacao_urbana"] = np.log(df["populacao_urbana"].where(df["populacao_urbana"] > 0))

# ============ 9) variaveis defasadas (t-1), para o modelo preditivo (objetivo 2) ============
lag_vars = ["investimento_percapita", "cv_investimento_5a", "prop_financiamento_oneroso",
            "indice_perda_faturamento", "indice_perda_distribuicao_agua"]
for v in lag_vars:
    df[f"{v}_lag1"] = df.groupby("id_municipio")[v].shift(1)

out_path = f"{BASE}\\br_painel_analise_final.csv"
df.to_csv(out_path, index=False, encoding="utf-8")
print("Painel final salvo:", out_path)
print("Linhas:", len(df), "Colunas:", len(df.columns))
