"""
Constroi a variavel de affordability ICR_SM (Indice de Comprometimento de Renda,
adaptado para usar salario minimo nacional no denominador em vez de renda domiciliar).

Entrada:
  - br_mdr_snis_municipio_agua_esgoto.csv (painel SNIS, 1995-2022)
  - salario_minimo_1995_2022.csv

Saida:
  - br_painel_icr_sm.csv (painel SNIS + ICR_SM + regiao + porte)
"""
import pandas as pd
import numpy as np

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"

snis = pd.read_csv(f"{BASE}\\br_mdr_snis_municipio_agua_esgoto.csv")
sm = pd.read_csv(f"{BASE}\\salario_minimo_1995_2022.csv")

# --- merge salario minimo por ano ---
df = snis.merge(sm[["ano", "salario_minimo_media_ponderada_ano"]], on="ano", how="left")

# --- tarifa media mensal residencial (R$/mes) ---
receita_total = df["receita_operacional_direta_agua"].fillna(0) + df["receita_operacional_direta_esgoto"].fillna(0)
economias = df["quantidade_economia_residencial_ativa_agua"]

df["tarifa_media_mensal_residencial"] = np.where(
    (economias.notna()) & (economias > 0),
    (receita_total / economias) / 12,
    np.nan,
)

# --- ICR_SM (%) = tarifa mensal residencial / salario minimo * 100 ---
df["ICR_SM"] = df["tarifa_media_mensal_residencial"] / df["salario_minimo_media_ponderada_ano"] * 100

# regra de limpeza: valores negativos ou > 100% sao implausiveis (erro de dado /
# subnotificacao de economias residenciais) -> tratados como ausentes
df["ICR_SM"] = df["ICR_SM"].where((df["ICR_SM"] >= 0) & (df["ICR_SM"] <= 100))

# --- regiao a partir da UF ---
regiao_map = {
    "AC": "Norte", "AP": "Norte", "AM": "Norte", "PA": "Norte", "RO": "Norte", "RR": "Norte", "TO": "Norte",
    "AL": "Nordeste", "BA": "Nordeste", "CE": "Nordeste", "MA": "Nordeste", "PB": "Nordeste",
    "PE": "Nordeste", "PI": "Nordeste", "RN": "Nordeste", "SE": "Nordeste",
    "DF": "Centro-Oeste", "GO": "Centro-Oeste", "MT": "Centro-Oeste", "MS": "Centro-Oeste",
    "ES": "Sudeste", "MG": "Sudeste", "RJ": "Sudeste", "SP": "Sudeste",
    "PR": "Sul", "RS": "Sul", "SC": "Sul",
}
df["regiao"] = df["sigla_uf"].map(regiao_map)

# --- porte do municipio (faixas padrao IBGE, baseado em populacao urbana) ---
bins = [0, 5000, 20000, 50000, 100000, 500000, np.inf]
labels = ["<5 mil", "5-20 mil", "20-50 mil", "50-100 mil", "100-500 mil", "500 mil+"]
df["porte"] = pd.cut(df["populacao_urbana"], bins=bins, labels=labels)

cols_out = ["ano", "id_municipio", "sigla_uf", "regiao", "porte", "populacao_urbana",
            "tarifa_media_mensal_residencial", "salario_minimo_media_ponderada_ano", "ICR_SM",
            "indice_atendimento_urbano_agua", "indice_coleta_esgoto", "indice_tratamento_esgoto"]
out = df[cols_out]
out.to_csv(f"{BASE}\\br_painel_icr_sm.csv", index=False, encoding="utf-8")

print("Painel salvo:", f"{BASE}\\br_painel_icr_sm.csv", "| linhas:", len(out))
print(f"Cobertura ICR_SM: {out['ICR_SM'].notna().sum()}/{len(out)} ({out['ICR_SM'].notna().mean()*100:.1f}%)")
print(out["ICR_SM"].describe())
