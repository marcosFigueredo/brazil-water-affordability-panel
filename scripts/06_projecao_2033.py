"""
Projeta cobertura de agua e esgoto por municipio ate 2033 (extrapolacao linear
simples sobre a serie historica), classifica em on_track/at_risk/will_not_meet
contra a meta legal (Lei 14.026/2020: 99% agua, 90% esgoto), e testa evidencia
de trade-off entre a inclinacao da cobertura e a inclinacao do ICR_SM.

Entrada: br_painel_analise_final.csv
Saida: br_projecao_cobertura_2033.csv, br_projecao_cobertura_2033_esgoto.csv
"""
import pandas as pd
import numpy as np

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")

ANO_META = 2033


def extrapola(grupo, coluna):
    g = grupo.dropna(subset=[coluna])
    if len(g) < 3:
        return pd.Series({"projecao_2033": np.nan, "inclinacao_aa": np.nan, "n_obs": len(g)})
    x = g["ano"].values.astype(float)
    y = g[coluna].values.astype(float)
    slope, intercept = np.polyfit(x, y, 1)
    proj = min(max(slope * ANO_META + intercept, 0), 150)
    return pd.Series({"projecao_2033": proj, "inclinacao_aa": slope, "n_obs": len(g)})


def classifica(p, meta):
    if pd.isna(p):
        return np.nan
    if p >= meta:
        return "on_track"
    elif p >= meta - 10:
        return "at_risk"
    else:
        return "will_not_meet"


def tendencia_icr(grupo):
    g = grupo.dropna(subset=["ICR_SM"])
    if len(g) < 3:
        return np.nan
    x = g["ano"].values.astype(float)
    y = g["ICR_SM"].values.astype(float)
    slope, _ = np.polyfit(x, y, 1)
    return slope


info_mun = df.sort_values("ano").groupby("id_municipio").last()[["sigla_uf", "regiao", "porte", "populacao_urbana"]]
icr_trend = df.groupby("id_municipio").apply(tendencia_icr, include_groups=False)
icr_trend.name = "tendencia_icr_sm_aa"

# ---------------- AGUA (meta 99%) ----------------
proj_agua = df.groupby("id_municipio").apply(extrapola, coluna="indice_atendimento_urbano_agua", include_groups=False).reset_index()
proj_agua["classificacao_2033"] = proj_agua["projecao_2033"].apply(lambda p: classifica(p, 99.0))
proj_agua = proj_agua.merge(info_mun, on="id_municipio", how="left")
proj_agua = proj_agua.merge(icr_trend, on="id_municipio", how="left")
proj_agua.to_csv(f"{BASE}\\br_projecao_cobertura_2033.csv", index=False, encoding="utf-8")

print("=== AGUA: distribuicao classificacao 2033 (meta 99%) ===")
print(proj_agua["classificacao_2033"].value_counts(dropna=False))
print(f"({proj_agua['classificacao_2033'].notna().sum()} / {len(proj_agua)} municipios com projecao valida)")
print("\nPor regiao (%):")
print((pd.crosstab(proj_agua["regiao"], proj_agua["classificacao_2033"], normalize="index") * 100).round(1))
print("\nPor porte (%):")
print((pd.crosstab(proj_agua["porte"], proj_agua["classificacao_2033"], normalize="index") * 100).round(1))

valid = proj_agua.dropna(subset=["inclinacao_aa", "tendencia_icr_sm_aa"])
corr = valid["inclinacao_aa"].corr(valid["tendencia_icr_sm_aa"])
print(f"\nCorrelacao inclinacao cobertura x inclinacao ICR_SM (N={len(valid)}): {corr:.4f}")

# ---------------- ESGOTO (meta 90%) ----------------
proj_esg = df.groupby("id_municipio").apply(extrapola, coluna="indice_coleta_esgoto", include_groups=False).reset_index()
proj_esg = proj_esg.rename(columns={"projecao_2033": "projecao_2033_esgoto", "inclinacao_aa": "inclinacao_esgoto_aa", "n_obs": "n_obs_esgoto"})
proj_esg["classificacao_2033_esgoto"] = proj_esg["projecao_2033_esgoto"].apply(lambda p: classifica(p, 90.0))
proj_esg = proj_esg.merge(info_mun, on="id_municipio", how="left")
proj_esg.to_csv(f"{BASE}\\br_projecao_cobertura_2033_esgoto.csv", index=False, encoding="utf-8")

n_validos = proj_esg["classificacao_2033_esgoto"].notna().sum()
print(f"\n=== ESGOTO: {n_validos}/{len(proj_esg)} municipios com projecao valida (meta 90%) ===")
print(proj_esg["classificacao_2033_esgoto"].value_counts(dropna=False))
print("\nPor regiao (%):")
print((pd.crosstab(proj_esg["regiao"], proj_esg["classificacao_2033_esgoto"], normalize="index") * 100).round(1))

# cruzamento agua x esgoto
comp = proj_agua[["id_municipio", "classificacao_2033"]].merge(
    proj_esg[["id_municipio", "classificacao_2033_esgoto"]], on="id_municipio", how="inner"
).dropna()
print(f"\n=== Cruzamento agua x esgoto (N={len(comp)}) ===")
print(pd.crosstab(comp["classificacao_2033"], comp["classificacao_2033_esgoto"]))

print("\nSalvos: br_projecao_cobertura_2033.csv e br_projecao_cobertura_2033_esgoto.csv")
