"""
Projeta o ICR-SM (affordability) por municipio ate 2033 por extrapolacao
linear simples sobre a serie historica, espelhando exatamente a logica ja
usada para cobertura no script 06 (funcao `extrapola`), mas aplicada ao
ICR-SM. Nao ha meta legal para affordability, entao nao classificamos contra
um alvo regulatorio, apenas reportamos o nivel projetado e a variacao frente
ao ultimo ano observado, e sinalizamos se o municipio fica acima do teto da
faixa internacional de affordability (3 a 5%) ja usada no artigo.

Entrada: br_painel_analise_final.csv
Saida: br_projecao_icr_2033_linear.csv
"""
import pandas as pd
import numpy as np

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")

ANO_META = 2033
LIMITE_INTERNACIONAL = 5.0


def extrapola_icr(grupo):
    g = grupo.dropna(subset=["ICR_SM"])
    if len(g) < 3:
        return pd.Series({"projecao_icr_2033_linear": np.nan, "inclinacao_icr_aa": np.nan, "n_obs": len(g)})
    x = g["ano"].values.astype(float)
    y = g["ICR_SM"].values.astype(float)
    slope, intercept = np.polyfit(x, y, 1)
    proj = min(max(slope * ANO_META + intercept, 0), 100)
    return pd.Series({"projecao_icr_2033_linear": proj, "inclinacao_icr_aa": slope, "n_obs": len(g)})


info_mun = df.sort_values("ano").groupby("id_municipio").last()[["sigla_uf", "regiao", "porte"]]
ultimo_icr = df.dropna(subset=["ICR_SM"]).sort_values("ano").groupby("id_municipio")["ICR_SM"].last()
ultimo_icr.name = "icr_sm_ultimo_observado"

proj = df.groupby("id_municipio").apply(extrapola_icr, include_groups=False).reset_index()
proj = proj.merge(info_mun, on="id_municipio", how="left")
proj = proj.merge(ultimo_icr, on="id_municipio", how="left")
proj["variacao_pp_ultimo_2033"] = proj["projecao_icr_2033_linear"] - proj["icr_sm_ultimo_observado"]
proj["acima_limite_internacional_2033"] = proj["projecao_icr_2033_linear"] > LIMITE_INTERNACIONAL

n_validos = proj["projecao_icr_2033_linear"].notna().sum()
print(f"=== Extrapolacao linear do ICR-SM: {n_validos}/{len(proj)} municipios com projecao valida ===")
print(f"Media do ultimo ano observado: {proj['icr_sm_ultimo_observado'].mean():.2f}%")
print(f"Media projetada 2033: {proj['projecao_icr_2033_linear'].mean():.2f}%")
print(f"Variacao media: {proj['variacao_pp_ultimo_2033'].mean():+.2f} p.p.")
print(f"Municipios acima do limite internacional (5%) em 2033: {proj['acima_limite_internacional_2033'].mean()*100:.1f}%")

print("\nPor regiao, media projetada 2033 (%):")
print(proj.groupby("regiao")["projecao_icr_2033_linear"].mean().round(2))

print("\nPor porte, media projetada 2033 (%):")
ordem_porte = ["<5 mil", "5-20 mil", "20-50 mil", "50-100 mil", "100-500 mil", "500 mil+"]
print(proj.groupby("porte")["projecao_icr_2033_linear"].mean().reindex(ordem_porte).round(2))

proj.to_csv(f"{BASE}\\br_projecao_icr_2033_linear.csv", index=False, encoding="utf-8")
print("\nArquivo salvo: br_projecao_icr_2033_linear.csv")
