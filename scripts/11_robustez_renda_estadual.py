"""
Robustez adicional inspirada em Fagundes, Marques & Malheiros (2025, Water Resources
Management) -- eles usam salario medio ESTADUAL (PNADC) como denominador de
affordability, em vez de um piso nacional unico. Este script constroi essa alternativa
e testa se o achado central (affordability e estrutural, nao gerencial) se mantem.

Fonte: SIDRA tabela 5436, variavel 5933 (rendimento medio mensal real, habitual, todos
os trabalhos, PNADC trimestral por UF). So existe a partir de 2012 -- restringe o teste
a 2012-2022, sub-periodo do painel principal.

Entrada: pnadc_renda_uf.json (baixado via API), br_painel_analise_final.csv
Saida: br_icr_renda_estadual.csv, comparacao_icr_sm_vs_renda_uf.csv,
       robustez_renda_estadual_modelo.txt
"""
import json
import pandas as pd
import numpy as np
from linearmodels.panel import PanelOLS

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"

# ============ 1) processa renda media estadual (PNADC) para serie anual ============
# fonte: SIDRA tabela 5436, variavel 5933, baixado via API e salvo em dados_brutos_externos/
with open(f"{BASE}\\dados_brutos_externos\\pnadc_renda_uf.json", encoding="utf-8") as f:
    raw = json.load(f)

nome_para_sigla = {
    "Rondônia": "RO", "Acre": "AC", "Amazonas": "AM", "Roraima": "RR", "Pará": "PA",
    "Amapá": "AP", "Tocantins": "TO", "Maranhão": "MA", "Piauí": "PI", "Ceará": "CE",
    "Rio Grande do Norte": "RN", "Paraíba": "PB", "Pernambuco": "PE", "Alagoas": "AL",
    "Sergipe": "SE", "Bahia": "BA", "Minas Gerais": "MG", "Espírito Santo": "ES",
    "Rio de Janeiro": "RJ", "São Paulo": "SP", "Paraná": "PR", "Santa Catarina": "SC",
    "Rio Grande do Sul": "RS", "Mato Grosso do Sul": "MS", "Mato Grosso": "MT",
    "Goiás": "GO", "Distrito Federal": "DF",
}

registros = []
for serie in raw[0]["resultados"][0]["series"]:
    sigla = nome_para_sigla[serie["localidade"]["nome"]]
    for periodo, valor in serie["serie"].items():
        if valor in (None, "-", "..", "..."):
            continue
        ano = int(periodo[:4])
        registros.append({"sigla_uf": sigla, "ano": ano, "renda_trimestre": float(valor)})

renda_df = pd.DataFrame(registros)
renda_anual = renda_df.groupby(["sigla_uf", "ano"])["renda_trimestre"].mean().reset_index()
renda_anual = renda_anual.rename(columns={"renda_trimestre": "renda_media_estadual_pnadc"})
renda_anual.to_csv(f"{BASE}\\br_renda_media_estadual_pnadc.csv", index=False, encoding="utf-8")
print(f"Renda estadual anual: {len(renda_anual)} linhas, {renda_anual['sigla_uf'].nunique()} UFs, "
      f"anos {renda_anual['ano'].min()}-{renda_anual['ano'].max()}")

# ============ 2) constroi ICR alternativo (denominador = renda media estadual) ============
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")
df = df.merge(renda_anual, on=["sigla_uf", "ano"], how="left")

df["ICR_renda_UF"] = df["tarifa_media_mensal_residencial"] / df["renda_media_estadual_pnadc"] * 100
df["ICR_renda_UF"] = df["ICR_renda_UF"].where((df["ICR_renda_UF"] >= 0) & (df["ICR_renda_UF"] <= 100))

sub = df[(df["ano"] >= 2012) & (df["ano"] <= 2022)].copy()
print(f"\nSub-periodo 2012-2022: {len(sub)} linhas")
print(f"ICR_SM valido: {sub['ICR_SM'].notna().sum()}")
print(f"ICR_renda_UF valido: {sub['ICR_renda_UF'].notna().sum()}")

# ============ 3) comparacao descritiva ============
comp = sub.dropna(subset=["ICR_SM", "ICR_renda_UF"])
corr = comp["ICR_SM"].corr(comp["ICR_renda_UF"])
print(f"\nCorrelacao ICR_SM x ICR_renda_UF (N={len(comp)}): {corr:.3f}")

por_regiao = sub.groupby("regiao")[["ICR_SM", "ICR_renda_UF"]].median()
print("\n=== Mediana por regiao: ICR_SM (salario minimo nacional) vs ICR_renda_UF (renda media estadual PNADC) ===")
print(por_regiao.round(2))
por_regiao.to_csv(f"{BASE}\\comparacao_icr_sm_vs_renda_uf.csv")

# ============ 4) reroda Modelo 1 (H1/H2) com a variavel dependente alternativa ============
sub_idx = sub.set_index(["id_municipio", "ano"])
cols_m1 = ["ICR_renda_UF", "investimento_percapita_lag1", "cv_investimento_5a_lag1",
           "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
           "log_populacao_urbana"]
d1 = sub_idx[cols_m1].dropna()
print(f"\n=== Modelo 1 com ICR_renda_UF como dependente (N={len(d1)}, municipios={d1.index.get_level_values(0).nunique()}) ===")

if len(d1) > 100:
    mod = PanelOLS(
        d1["ICR_renda_UF"],
        d1[["investimento_percapita_lag1", "cv_investimento_5a_lag1",
            "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
            "log_populacao_urbana"]],
        entity_effects=True, time_effects=True, drop_absorbed=True,
    )
    res = mod.fit(cov_type="clustered", cluster_entity=True)
    print(res.summary)

    with open(f"{BASE}\\robustez_renda_estadual_modelo.txt", "w", encoding="utf-8") as f:
        f.write(f"Correlacao ICR_SM x ICR_renda_UF (N={len(comp)}): {corr:.3f}\n\n")
        f.write("Mediana por regiao:\n")
        f.write(por_regiao.round(2).to_string())
        f.write(f"\n\n=== Modelo 1, dependente=ICR_renda_UF (N={len(d1)}) ===\n")
        f.write(str(res.summary))
    print("\nSalvo: robustez_renda_estadual_modelo.txt")
else:
    print("Amostra insuficiente para rodar o modelo.")

sub[["id_municipio", "ano", "sigla_uf", "regiao", "ICR_SM", "ICR_renda_UF",
     "renda_media_estadual_pnadc"]].to_csv(f"{BASE}\\br_icr_renda_estadual.csv", index=False, encoding="utf-8")
print("Salvo: br_icr_renda_estadual.csv, comparacao_icr_sm_vs_renda_uf.csv")

# ============ 5) checagem de isolamento: mesmo modelo, mesma amostra (2012-2022),
#                mas com ICR_SM (denominador nacional) em vez de ICR_renda_UF, para
#                separar "efeito do denominador" de "efeito do periodo mais curto" ============
d1b_cols = ["ICR_SM", "investimento_percapita_lag1", "cv_investimento_5a_lag1",
            "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
            "log_populacao_urbana"]
d1b = sub_idx[d1b_cols].dropna()
print(f"\n=== CHECAGEM DE ISOLAMENTO: Modelo 1 com ICR_SM, MESMA amostra 2012-2022 (N={len(d1b)}) ===")
mod_b = PanelOLS(
    d1b["ICR_SM"],
    d1b[["investimento_percapita_lag1", "cv_investimento_5a_lag1",
         "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
         "log_populacao_urbana"]],
    entity_effects=True, time_effects=True, drop_absorbed=True,
)
res_b = mod_b.fit(cov_type="clustered", cluster_entity=True)
print(res_b.summary)

with open(f"{BASE}\\robustez_renda_estadual_modelo.txt", "a", encoding="utf-8") as f:
    f.write(f"\n\n=== CHECAGEM DE ISOLAMENTO: Modelo 1 com ICR_SM, MESMA amostra 2012-2022 (N={len(d1b)}) ===\n")
    f.write(str(res_b.summary))
print("\nChecagem de isolamento salva.")
