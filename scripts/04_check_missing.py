"""
Checa missingness das variaveis do modelo no painel combinado, geral e restrito
ao sub-periodo 2002-2022 (onde PIB/crescimento/clima estao disponiveis).

Entrada: br_painel_analise_final.csv
Saida: missingness_relatorio.txt
"""
import pandas as pd

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")

vars_modelo = [
    "ICR_SM",
    "investimento_percapita", "investimento_percapita_lag1",
    "cv_investimento_5a", "cv_investimento_5a_lag1",
    "prop_financiamento_oneroso", "prop_financiamento_oneroso_lag1",
    "indice_perda_faturamento", "indice_perda_faturamento_lag1",
    "indice_atendimento_urbano_agua", "indice_coleta_esgoto",
    "log_populacao_urbana", "regiao",
    "pib_per_capita_reais", "log_pib_per_capita",
    "crescimento_populacional_pct_aa", "crescimento_va_servicos_pct_aa",
    "expectativa_crescimento_populacional_pct_aa",
    "anomalia_precipitacao_pct",
]

linhas_saida = []

def linha(txt=""):
    print(txt)
    linhas_saida.append(txt)

linha("=== Missingness geral (1995-2022, todas as linhas) ===")
n = len(df)
for v in vars_modelo:
    nn = df[v].notna().sum()
    linha(f"{v:45s} {nn:7d}/{n} ({nn/n*100:5.1f}%)")

linha("")
linha("=== Missingness restrito a 2002-2022 ===")
sub = df[df["ano"] >= 2002]
n2 = len(sub)
for v in vars_modelo:
    nn = sub[v].notna().sum()
    linha(f"{v:45s} {nn:7d}/{n2} ({nn/n2*100:5.1f}%)")

linha("")
linha("=== Linhas com TODAS as variaveis do modelo principal (H1/H2, defasado) nao-nulas ===")
core_lag = ["ICR_SM", "investimento_percapita_lag1", "cv_investimento_5a_lag1",
            "prop_financiamento_oneroso_lag1", "indice_perda_faturamento_lag1",
            "log_populacao_urbana", "regiao"]
completos = df.dropna(subset=core_lag)
linha(f"{len(completos)} / {n} linhas ({len(completos)/n*100:.1f}%)")
linha(f"Municipios distintos nessa amostra: {completos['id_municipio'].nunique()}")
linha(f"Anos cobertos: {completos['ano'].min()} - {completos['ano'].max()}")

linha("")
linha("=== Linhas com modelo completo INCLUINDO PIB/crescimento/clima (H4) ===")
core_full = core_lag + ["log_pib_per_capita", "crescimento_populacional_pct_aa",
                          "crescimento_va_servicos_pct_aa", "anomalia_precipitacao_pct"]
completos_full = df.dropna(subset=core_full)
linha(f"{len(completos_full)} / {n} linhas ({len(completos_full)/n*100:.1f}%)")
linha(f"Municipios distintos: {completos_full['id_municipio'].nunique()}")
linha(f"Anos cobertos: {completos_full['ano'].min()} - {completos_full['ano'].max()}")

with open(f"{BASE}\\missingness_relatorio.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(linhas_saida))
print("\nRelatorio salvo em missingness_relatorio.txt")
