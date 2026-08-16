"""
Busca a projecao oficial de populacao do IBGE por UF (tabela SIDRA 7358,
"Projecao da Populacao"), para os anos 2022 e 2033, e calcula a taxa de
crescimento populacional anual composta (CAGR) oficial por UF nesse
horizonte. Isso substitui, no forecast recursivo de ICR-SM ate 2033
(scripts 09 e 16), a expectativa de crescimento populacional que antes era o
CAGR historico de cada municipio dentro do proprio painel SNIS (1995-2022),
por uma projecao demografica real, que ja incorpora a desaceleracao/declinio
da populacao brasileira prevista pelo IBGE, algo que o CAGR historico nao
captura.

Fonte: IBGE SIDRA, tabela 7358 (Populacao, por sexo e idade, projetada),
variavel 606 (Populacao), sexo=Total, idade=Total, anos 2022 e 2033, nivel UF.
API: https://servicodados.ibge.gov.br/api/v3/agregados/7358/periodos/2018/
     variaveis/606?localidades=N3[all]&classificacao=2[6794]|287[100362]|1933[49038,49049]

Entrada: dados_brutos_externos/ibge_projecao_populacao_uf_raw.json (cache local
         do request acima, ja salvo)
Saida: br_expectativa_crescimento_uf_ibge.csv
"""
import json
import pandas as pd

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"

NOME_PARA_SIGLA = {
    "Rondônia": "RO", "Acre": "AC", "Amazonas": "AM", "Roraima": "RR", "Pará": "PA",
    "Amapá": "AP", "Tocantins": "TO", "Maranhão": "MA", "Piauí": "PI", "Ceará": "CE",
    "Rio Grande do Norte": "RN", "Paraíba": "PB", "Pernambuco": "PE", "Alagoas": "AL",
    "Sergipe": "SE", "Bahia": "BA", "Minas Gerais": "MG", "Espírito Santo": "ES",
    "Rio de Janeiro": "RJ", "São Paulo": "SP", "Paraná": "PR", "Santa Catarina": "SC",
    "Rio Grande do Sul": "RS", "Mato Grosso do Sul": "MS", "Mato Grosso": "MT",
    "Goiás": "GO", "Distrito Federal": "DF",
}

with open(f"{BASE}\\dados_brutos_externos\\ibge_projecao_populacao_uf_raw.json", encoding="utf-8") as f:
    raw = json.load(f)

resultados = raw[0]["resultados"]

pop_por_ano_uf = {}  # {sigla_uf: {ano: pop}}
for res in resultados:
    ano = None
    for cls in res["classificacoes"]:
        if cls["id"] == "1933":
            ano = int(list(cls["categoria"].values())[0])
    for s in res["series"]:
        nome_uf = s["localidade"]["nome"]
        sigla = NOME_PARA_SIGLA.get(nome_uf)
        if sigla is None:
            continue
        valor = list(s["serie"].values())[0]
        if valor in ("-", "..", "...", None):
            continue
        pop_por_ano_uf.setdefault(sigla, {})[ano] = float(valor)

linhas = []
for sigla, d in pop_por_ano_uf.items():
    if 2022 in d and 2033 in d and d[2022] > 0:
        n_anos = 2033 - 2022
        cagr = ((d[2033] / d[2022]) ** (1 / n_anos) - 1) * 100
        linhas.append({
            "sigla_uf": sigla,
            "populacao_ibge_2022": d[2022],
            "populacao_ibge_2033": d[2033],
            "expectativa_crescimento_populacional_ibge_pct_aa": cagr,
        })

proj_uf = pd.DataFrame(linhas).sort_values("sigla_uf")
print(proj_uf.round(3).to_string(index=False))
print(f"\nMedia nacional (simples, nao ponderada por populacao): {proj_uf['expectativa_crescimento_populacional_ibge_pct_aa'].mean():.3f}% a.a.")

proj_uf.to_csv(f"{BASE}\\br_expectativa_crescimento_uf_ibge.csv", index=False, encoding="utf-8")
print("\nArquivo salvo: br_expectativa_crescimento_uf_ibge.csv")
