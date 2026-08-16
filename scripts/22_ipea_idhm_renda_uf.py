"""
Processa o IDHM-renda (dimensao renda do Indice de Desenvolvimento Humano
Municipal) por UF, baixado do IPEAdata (fonte: censos 1991/2000/2010 e
estimativas anuais a partir de 2012 com base na PNAD Continua). Usado para
interpretar o mapa de projecao de affordability 2033 (script 21), testando
se a geografia do mapa acompanha o nivel de desenvolvimento humano de cada
estado ou a velocidade com que ele cresceu.

Fonte: IPEAdata, http://www.ipeadata.gov.br/
Entrada: dados_brutos_externos/ipeadata_idhm_renda_uf.csv (export manual do
         portal, ja salvo)
Saida: br_idhm_renda_uf.csv
"""
import pandas as pd

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"

idhm = pd.read_csv(
    f"{BASE}\\dados_brutos_externos\\ipeadata_idhm_renda_uf.csv",
    sep=";", skiprows=1, encoding="utf-8-sig",
)
idhm.columns = [c.strip() for c in idhm.columns]
idhm = idhm.dropna(subset=["Sigla"])
for c in idhm.columns[3:]:
    idhm[c] = idhm[c].astype(str).str.replace(",", ".").astype(float)

idhm = idhm.rename(columns={"Sigla": "sigla_uf"}).set_index("sigla_uf")
idhm["crescimento_idhm_renda_2010_2024"] = idhm["2024"] - idhm["2010"]
idhm["crescimento_idhm_renda_1991_2010"] = idhm["2010"] - idhm["1991"]

print("IDHM-renda por UF, 1991 a 2024")
print(idhm[["1991", "2000", "2010", "2022", "2024", "crescimento_idhm_renda_2010_2024"]].round(3).to_string())

n_declinio = (idhm["crescimento_idhm_renda_1991_2010"] < 0).sum()
print(f"\nEstados com IDHM-renda em declinio 1991-2010: {n_declinio} (de {len(idhm)})")

idhm.reset_index().to_csv(f"{BASE}\\br_idhm_renda_uf.csv", index=False, encoding="utf-8")
print("\nArquivo salvo: br_idhm_renda_uf.csv")
