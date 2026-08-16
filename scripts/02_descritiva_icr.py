"""
Estatistica descritiva do ICR_SM por ano, regiao e porte de municipio.
Responde o objetivo especifico 1 do plano (secao 6.0).

Entrada: br_painel_icr_sm.csv
Saida: descritiva_icr_por_ano.csv, descritiva_icr_por_regiao.csv,
       descritiva_icr_por_porte.csv, descritiva_icr_tendencia_regiao.csv
"""
import pandas as pd

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_icr_sm.csv")

por_ano = df.groupby("ano")["ICR_SM"].agg(["median", "mean", "count"]).round(3)
por_regiao = df.groupby("regiao")["ICR_SM"].agg(["median", "mean", "count"]).round(3)

ultimo_ano = df["ano"].max()
por_regiao_ultimo = df[df["ano"] == ultimo_ano].groupby("regiao")["ICR_SM"].agg(["median", "mean", "count"]).round(3)

por_porte = df.groupby("porte", observed=True)["ICR_SM"].agg(["median", "mean", "count"]).round(3)

primeiro_ano_valido = df[df["ICR_SM"].notna()]["ano"].min()
tendencia = df[df["ano"].isin([primeiro_ano_valido, ultimo_ano])].groupby(["regiao", "ano"])["ICR_SM"].median().unstack()
tendencia["variacao_pp"] = (tendencia[ultimo_ano] - tendencia[primeiro_ano_valido]).round(3)

por_ano.to_csv(f"{BASE}\\descritiva_icr_por_ano.csv")
por_regiao.to_csv(f"{BASE}\\descritiva_icr_por_regiao.csv")
por_porte.to_csv(f"{BASE}\\descritiva_icr_por_porte.csv")
tendencia.to_csv(f"{BASE}\\descritiva_icr_tendencia_regiao.csv")

print("=== ICR_SM por ano ===")
print(por_ano)
print("\n=== ICR_SM por regiao (media do periodo) ===")
print(por_regiao)
print(f"\n=== ICR_SM por regiao ({ultimo_ano}) ===")
print(por_regiao_ultimo)
print("\n=== ICR_SM por porte ===")
print(por_porte)
print(f"\n=== Tendencia {primeiro_ano_valido} -> {ultimo_ano} por regiao ===")
print(tendencia.round(3))
print("\nTabelas salvas em", BASE)
