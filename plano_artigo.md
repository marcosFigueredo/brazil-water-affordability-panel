# Plano de artigo — Edição Especial "Water Utility Planning for Customer Equity Outcomes"

**Deadline de submissão:** 31 jan 2027 | **Guest editor:** Gregory Pierce | Categoria: "VSI: Water Equity Planning"

> Histórico de revisões:
> - Rev.1: affordability via renda domiciliar municipal (Censo/SIDRA) — descartada, sem esse dado.
> - Rev.2: pivô para previsão de cobertura vs. meta legal de universalização (2033) — mantida
>   como componente, mas **não é mais o foco central sozinho**.
> - Rev.3: o foco da chamada é explicitamente affordability ("water utility planning
>   for customer affordability outcomes"), confirmado pelo usuário. Proposta reancorada em
>   affordability, usando **salário mínimo nacional** (não renda municipal) como denominador —
>   dado público, série única nacional, sem necessidade de cruzar com censo por município.
> - **Rev.4 (atual): pergunta e hipóteses reescritas para refletir os resultados empíricos
>   reais** (seção 6.5/6.6), não a expectativa original. O modelo foi rodado (painel com
>   efeitos fixos, N=41.720–90.952) e H1/H2 originais **não se confirmaram**: as alavancas
>   canônicas de planejamento (investimento, financiamento, perdas) não explicam a variação
>   de affordability ano a ano dentro do mesmo município — 85% da variação é *entre*
>   municípios (estrutural), não *dentro* deles ao longo do tempo. A pergunta central do
>   artigo mudou de "planejamento produz affordability?" (assumido) para "por que o
>   planejamento observável não move affordability, e o que de fato move os resultados de
>   acesso e preço?" (testado e respondido). Problema, objetivo e hipóteses abaixo já
>   refletem essa versão final — a versão original fica registrada em `git`/histórico de
>   edições deste arquivo, não repetida aqui.

## 1. Problema

No Brasil, affordability é tratada, na prática regulatória e na literatura, como algo que
o planejamento da prestadora — nível de investimento, fonte de financiamento, controle de
perdas — pode produzir. Esse pressuposto raramente é testado empiricamente em painel
longo. Este estudo testa essa premissa diretamente, usando 28 anos de dados de todas as
prestadoras de água/esgoto do Brasil, e encontra que **ela não se sustenta**: as alavancas
de planejamento observáveis no SNIS explicam quase nada da variação de affordability
dentro do mesmo município ao longo do tempo — a variação é overwhelmingly estrutural,
fixa por município/região. O problema real, portanto, não é "por que os prestadores não
planejam para affordability", mas **"por que affordability parece presa a características
estruturais do município, e o que — se não o planejamento de curto prazo medido pelo
SNIS — de fato move os resultados de acesso e de preço"**.

## 2. Objetivo

**Geral:** Testar se as alavancas canônicas de planejamento de utilities (nível e
estabilidade de investimento, fonte de financiamento — recurso próprio vs. oneroso/dívida,
perdas de faturamento) explicam a variação de affordability (ICR-SM) no painel de
municípios brasileiros atendidos por serviços de água/esgoto (1995–2022) e, dado que — como
o teste empírico mostrou — não explicam, caracterizar o que de fato explica: heterogeneidade
estrutural entre municípios/regiões, porte do município, e pressão de crescimento
populacional sobre o acesso (não sobre o preço).

**Fundamentação da métrica de affordability:** não existe um padrão internacional único —
é uma família de métricas de "gasto ÷ renda" com thresholds que variam por instituição
(EPA 2,5–4,5%; OECD ~3–4%; World Bank e ONU 5%), todas derivadas da lógica consolidada por
**Hutton (2012)**, referência-base usada pela OMS/UNICEF (JMP) para monitorar affordability
globalmente. No Brasil, o precedente direto é o **Índice de Comprometimento de Renda (ICR)**
= tarifa ÷ renda domiciliar, usado por reguladoras estaduais (ex. ADASA-DF) e na literatura
acadêmica (Pereira & Alvez, 2022, *Revista DAE*). Nossa variável é uma **adaptação do ICR**:
como não há renda domiciliar municipal em série longa, substituímos o denominador por
**salário mínimo nacional** — escolha que tem apoio indireto na própria prática do IBGE de
definir linha de pobreza em frações de salário mínimo (ex. "meio salário mínimo per capita").
Essa substituição será declarada explicitamente como limitação metodológica (não é o ICR
"puro"), e o modelo será testado também com bandas de threshold da literatura internacional
(3% e 5%) como checagem de robustez, em vez de um corte único arbitrário.

**Específicos:**
- Construir série histórica de affordability (tarifa média residencial / salário mínimo)
  por município e comparar sua evolução entre regiões e portes de município. *(Executado —
  seção 6.0.)*
- Testar empiricamente — não assumir — se padrões de planejamento (investimento estável vs.
  reativo; financiamento próprio vs. dívida) predizem trajetórias de affordability mais
  favoráveis. *(Executado — resultado: não predizem; seção 6.5.)*
- Decompor a variância do ICR-SM em componente estrutural (entre municípios) vs. componente
  de curto prazo (dentro do mesmo município ao longo do tempo) — achado que se tornou o
  eixo central do artigo. *(Executado — 85% between, ~0% within; seção 6.5.)*
- Mapear onde o trade-off cobertura×affordability de fato aparece (regionalmente) e onde a
  pressão de crescimento populacional/econômico atua — sobre o preço (ICR) ou sobre o
  acesso (cobertura) — usando a meta legal de universalização (99% água / 90% esgoto até
  31/12/2033, Lei 14.026/2020 / PLANSAB) como horizonte de referência para cobertura.
  *(Executado — seções 6.3.1/6.3.2.)*

## 3. Hipóteses finais (testadas — substituem as hipóteses originais H1–H4)

> As hipóteses originais (H1: investimento estável → affordability melhor; H2: dívida →
> affordability pior; H3: trade-off Nordeste específico; H4: crescimento → affordability
> pior) foram testadas e **H1 e H2 não se confirmaram; H3 e H4 se confirmaram em forma
> revisada**, diferente da formulação a priori. As hipóteses abaixo são a versão final,
> pós-dados — resultado completo na seção 6.5/6.6.

- **H1' — Affordability é predominantemente estrutural, não gerencial de curto prazo.**
  As alavancas de planejamento que o SNIS registra (nível/estabilidade de investimento,
  fonte de financiamento, perdas) não explicam variação de affordability dentro do mesmo
  município ao longo do tempo (todos p>0,19 no modelo defasado). 85% da variação do ICR-SM
  é *entre* municípios; ~0% é *dentro*. **Confirmada — é o achado central do artigo.**
- **H2' — O trade-off cobertura×affordability é regional, mas concentrado em Norte e
  Centro-Oeste, não no Nordeste.** Nessas regiões, aumento de cobertura vem acompanhado de
  piora do ICR-SM (interação região×cobertura significativa, p<0,02); no Nordeste e no Sul
  esse padrão não aparece. **Confirmada, com correção geográfica em relação à hipótese
  original.**
- **H3' — Pressão de crescimento atinge o sistema pelo lado do acesso, não do preço.**
  Crescimento populacional reduz cobertura de água (β=-0,106, p=0,003), mas crescimento de
  comércio/serviços está associado a affordability *melhor*, não pior (β=-0,0033, p<0,001).
  **Confirmada nessa forma revisada — inverte o sinal esperado originalmente para a parte
  de affordability.**
- **H4' (nova, decorrente do achado de 6.3.2) — Água e esgoto são trajetórias de
  planejamento desacopladas.** 63% dos municípios "on track" para a meta de água de 2033
  estão "will not meet" para a meta de esgoto — cobertura de um serviço não prediz
  cobertura do outro. **Confirmada.**

## 4. Decisões fechadas nesta revisão

- **Escopo geográfico:** Brasil inteiro (confirmado pelo usuário), sem recorte exclusivo
  Nordeste/Bahia — região/UF entra como variável de controle/interação, não como filtro.
- **Bases externas priorizadas** (usuário selecionou): salário mínimo nacional, PIB per
  capita municipal (IBGE), dados climáticos/seca. **Tipo de prestador (natureza jurídica)
  não foi priorizado** — fica descartado por ora, pode ser revisitado se H1/H2 precisarem
  de mais poder explicativo.

## 4.1 Questões em aberto (não bloqueiam mais o desenho, mas seguem pendentes)

1. ~~Motivação Bahia/Nordeste~~ — resolvido: escopo é nacional.
2. ~~Tipo de prestador~~ — não priorizado nesta rodada, mantido como extensão futura.

## 5. Dados

### Já disponível
- `br_mdr_snis_municipio_agua_esgoto.csv` — SNIS/Brasil, painel município-ano,
  1995–2022, 5.549 municípios, 27 UFs, 119.256 linhas, sem chaves duplicadas.
- Variáveis-chave para este desenho:
  - Affordability: `receita_operacional_direta_agua`, `receita_operacional_direta_esgoto`,
    `quantidade_economia_residencial_ativa_agua`, `quantidade_economia_residencial_ativa_esgoto`
    (para construir tarifa média residencial implícita)
  - Cobertura: `indice_atendimento_urbano_agua`, `indice_atendimento_total_agua`,
    `indice_coleta_esgoto`, `indice_tratamento_esgoto`, `indice_atendimento_agua_esgoto`
  - População: `populacao_atendida_agua`, `populacao_urbana`,
    `populacao_urbana_atendida_agua_ibge` (série de crescimento populacional)
  - Planejamento/investimento: `investimento_total_prestador`,
    `investimento_agua_prestador`, `investimento_esgoto_prestador`,
    `investimento_recurso_proprio_prestador` vs `investimento_recurso_oneroso_prestador`
    (financiamento próprio vs. dívida)
  - Eficiência/perdas: `indice_perda_faturamento`, `indice_perda_distribuicao_agua`,
    `indice_perda_linear_agua`
  - Finanças: `receita_operacional`, `despesa_total_servico`, `despesa_divida_total`
- Missingness em variáveis-chave: ~17–23% (checar concentração por ano/porte de
  município antes de modelar).

### Baixado nesta revisão (já em disco, na pasta do projeto)
- **`salario_minimo_1995_2022.csv`** — série anual do salário mínimo nacional, 1995–2022,
  com 3 colunas: valor vigente em 1º de janeiro, valor vigente em 31 de dezembro, e média
  ponderada pelo número de dias de vigência no ano (recomendada para a razão affordability,
  pois pondera corretamente anos com reajuste no meio do ano). Fonte: IBGE
  (`evolucao_do_salario_minimo.xls`, oficial, 1995–2015) cruzada com contabeis.com.br
  (2016–2023) para os anos mais recentes — valores conferem entre as duas fontes.
- **`br_ibge_pib_populacao_municipio.csv`** — 122.466 linhas, `id_municipio` (código IBGE,
  compatível com o SNIS) × `ano` (2002–2023), com PIB corrente (mil reais, tabela SIDRA
  5938), população estimada (tabela SIDRA 6579) e `pib_per_capita_reais` calculado.
  **Não existe tabela pronta de PIB per capita municipal no SIDRA** — foi calculado aqui
  a partir de PIB total ÷ população. População não tinha estimativa oficial em 2007, 2010,
  2022 e 2023 (anos de censo/pós-censo); esses 4 pontos foram interpolados linearmente
  entre os anos vizinhos por município — marcado na coluna `populacao_interpolada`.
  **Cobre 2002–2023, não 1995–2001** do painel SNIS (7 primeiros anos do painel ficam
  sem esse controle).
- **`br_crescimento_populacao_pib_servicos_municipio.csv`** — 122.540 linhas,
  `id_municipio` × `ano` (2002–2023), com valor adicionado de serviços (tabela SIDRA 5938,
  variável "serviços, exclusive administração/defesa/educação/saúde públicas" — proxy de
  comércio/serviços privados, a categoria mais próxima do que existe nas Contas Nacionais
  municipais) e **taxas de crescimento ano a ano** (%) de população, PIB per capita e
  serviços. Cobertura: ~95% das linhas têm crescimento populacional/PIB per capita
  calculado, ~86% têm crescimento de serviços (primeiro ano de cada município fica sem
  taxa, por não ter ano anterior de comparação — natural em qualquer cálculo de variação).
- **`br_expectativa_crescimento_municipio.csv`** — 5.570 municípios, com uma
  **"expectativa de crescimento"** por município = CAGR (taxa composta anual) de longo
  prazo entre o primeiro e o último ano disponível de cada série (população, PIB per
  capita, serviços). É uma extrapolação simples de tendência histórica, não uma projeção
  oficial — **não existe projeção populacional oficial em nível municipal no IBGE**
  (só nacional/UF). Serve como proxy de "pressão de crescimento esperada" sobre o
  planejamento da prestadora (alimenta H4) e como ponto de partida para o componente de
  extrapolação/ML mencionado na seção 6.

Sources:
- [Tabela 5938 — PIB dos Municípios, valores correntes (SIDRA/IBGE)](https://sidra.ibge.gov.br/tabela/5938)
- [Tabela 6579 — População residente estimada (SIDRA/IBGE)](https://sidra.ibge.gov.br/tabela/6579)
- [evolucao_do_salario_minimo.xls (IBGE, oficial)](https://ftp.ibge.gov.br/Salario_Minimo/evolucao_do_salario_minimo.xls)
- [Tabela salários mínimos 1995–2026 (contabeis.com.br)](https://www.contabeis.com.br/tabelas/salario-minimo/)

### Clima/seca — resolvido nesta revisão
- **`br_clima_precipitacao_uf.csv`** — 756 linhas, `sigla_uf` × `ano` (1995–2022, 27 UFs),
  com precipitação anual (mm, medida na capital de cada estado), normal climatológica
  1995–2022 e **anomalia de precipitação (%)** em relação a essa normal. Anomalias variam
  de -51% a +98%, consistente com eventos conhecidos de seca/cheia extrema no período.
- **Decisão de escopo (usuário escolheu):** granularidade por **UF** (27 séries), não por
  município individual nem por mesorregião — troca precisão espacial fina por viabilidade
  (o nível município a município exigiria ~5.570 chamadas de API, dezenas de minutos e
  risco de falhas parciais).
- **Fonte:** [Open-Meteo Historical Weather API](https://open-meteo.com/) (reanálise
  ERA5, gratuita, sem necessidade de cadastro/chave) — usada porque as fontes oficiais
  brasileiras de seca têm fricção de acesso alta para automação: o Monitor de Secas do
  CEMADEN exige cadastro por consulta manual e não tem bulk download; o BDMEP do INMET
  também exige cadastro. Coordenadas das capitais vieram de uma base pública de
  municípios brasileiros (latitude/longitude).
- **Limitação a declarar:** um ponto de medição por UF (a capital) representa o clima do
  estado inteiro — estados grandes/heterogêneos (ex. Amazonas, Bahia, Minas Gerais) têm
  variação climática interna que essa aproximação não captura. Adequado como controle de
  pressão climática regional no painel, não como medida precisa de seca local.

Sources:
- [Tabela 6784 — PIB dos Municípios (SIDRA/IBGE)](https://sidra.ibge.gov.br/tabela/6784)
- [Produto Interno Bruto (PIB) — Base dos Dados](https://basedosdados.org/dataset/fcf025ca-8b19-4131-8e2d-5ddb12492347)
- [Open-Meteo Historical Weather API](https://open-meteo.com/)
- [Municípios Monitorados — Cemaden](http://www2.cemaden.gov.br/municipios-monitorados-2/) (avaliado, descartado por fricção de acesso)

### Descartado
- ~~Renda domiciliar por município (Censo/SIDRA)~~ — decisão do usuário, substituído por
  salário mínimo nacional.

## 6. Especificação do modelo — entradas exatas e resultados esperados

### 6.0 Etapa descritiva (responde objetivo específico 1 — não é a regressão)

O objetivo específico 1 ("construir série histórica... comparar entre regiões e portes")
é atendido por estatística descritiva do ICR-SM (médias/medianas por região, porte de
município e ano, gráficos de trajetória), **não** pelo modelo de painel da seção 6.3 — essa
etapa vem antes da regressão, não é um subproduto dela.

**Executada — resultados preliminares** (`br_painel_icr_sm.csv` + tabelas
`descritiva_icr_*.csv`, na pasta do projeto):

- **Cobertura:** ICR_SM calculável em 80,6% das linhas do painel (96.081/119.256); 24
  valores implausíveis (negativos ou >100% do salário mínimo — provável erro de
  subnotificação de economias residenciais) tratados como ausentes (`ICR_SM_limpo`).
  Mediana geral: 6,1%; média: 6,8% — **já acima da banda internacional de 3–5%** usada
  como referência de affordability (achado relevante para a introdução/discussão).
- **Tendência nacional (1995→2022):** queda acentuada de ~15–18% (1995–1997, amostra
  pequena) para uma estabilização em torno de 5,2–6% desde ~2010. **Alerta metodológico
  importante:** essa queda coincide com a política de valorização real do salário mínimo
  (2003–2015+), que subiu bem acima da inflação — ou seja, parte da "melhora" de
  affordability é efeito do denominador (renda de referência subindo), não
  necessariamente de melhor planejamento tarifário. Os efeitos fixos de ano no modelo de
  painel absorvem esse efeito nacional comum, mas isso precisa ser discutido
  explicitamente no artigo, não deixado implícito.
- **Por região (média do período):** Nordeste tem o ICR_SM mais baixo (mediana 4,8%),
  Sul o mais alto (8,0%) — **padrão contraintuitivo à primeira vista**: a região
  historicamente mais pobre e com pior cobertura paga proporcionalmente menos, o que
  sugere tarifas mais baixas/subsidiadas acompanhadas de pior serviço, enquanto o Sul
  (mais rico, melhor cobertura) tem tarifas plenas de recuperação de custo. É material
  direto para H3 (trade-off cobertura × affordability por região).
- **Por porte de município (média do período):** relação crescente e monotônica — de
  5,7% em municípios <5 mil habitantes a 12,2% em municípios de 500 mil+. Municípios
  grandes pagam proporcionalmente mais, possivelmente por tarifas de custo pleno vs.
  sistemas pequenos subsidiados/deficitários.
- **Cautela:** os primeiros anos do painel (1995–2000) têm amostra muito pequena (28
  observações em 1995) e valores extremos (Centro-Oeste chega a 35% em 1995) — a série
  descritiva principal do artigo deve começar de um ano com N razoável (ex. 2000+),
  mantendo 1995–1999 apenas na regressão de painel (onde efeitos fixos de ano absorvem
  parte do ruído) e citando a limitação de amostra pequena no início da série.

### 6.1 Variável dependente

**ICR-SM** (Índice de Comprometimento de Renda adaptado, % do salário mínimo), por
município-ano:

```
tarifa_media_mensal_residencial_it =
    (receita_operacional_direta_agua_it + receita_operacional_direta_esgoto_it)
    / quantidade_economia_residencial_ativa_agua_it / 12

ICR_SM_it (%) = tarifa_media_mensal_residencial_it
              / salario_minimo_media_ponderada_ano_t * 100
```

Fonte: `br_mdr_snis_municipio_agua_esgoto.csv` (numerador) + `salario_minimo_1995_2022.csv`
(denominador, coluna `salario_minimo_media_ponderada_ano`).

**Variável dependente secundária** (para objetivo específico 3, trade-off): cobertura —
`indice_atendimento_urbano_agua` e `indice_coleta_esgoto` (mesma fonte SNIS).

### 6.2 Variáveis explicativas — tabela de entradas

| Bloco | Variável | Fórmula / coluna-fonte | Hipótese |
|---|---|---|---|
| Investimento | Investimento per capita | `investimento_total_prestador / populacao_atendida_agua` | H1 |
| Investimento | Estabilidade do investimento | desvio-padrão/média (CV) do investimento per capita em janela móvel de 5 anos | H1 |
| Financiamento | Proporção de financiamento oneroso | `investimento_recurso_oneroso_prestador / investimento_total_prestador` | H2 |
| Eficiência | Perdas de faturamento | `indice_perda_faturamento` | controle |
| Eficiência | Perdas de distribuição | `indice_perda_distribuicao_agua` | controle |
| Porte/região | População urbana (log) | `log(populacao_urbana)` | controle |
| Porte/região | Região (Norte/Nordeste/Centro-Oeste/Sudeste/Sul) | derivada de `sigla_uf` | H3 |
| Porte/região | Interação Região × Cobertura | `regiao_it * indice_atendimento_urbano_agua_it` | H3 |
| Capacidade econômica | PIB per capita (log) | `br_ibge_pib_populacao_municipio.csv::pib_per_capita_reais` (2002+) | controle |
| Pressão de crescimento | Crescimento populacional a.a. | `br_crescimento_populacao_pib_servicos_municipio.csv::crescimento_populacional_pct_aa` | H4 |
| Pressão de crescimento | Crescimento de serviços a.a. | `...::crescimento_va_servicos_pct_aa` (proxy comércio/serviços) | H4 |
| Pressão de crescimento | Expectativa de crescimento (nível, time-invariant) | `br_expectativa_crescimento_municipio.csv` — usada em especificação cross-section/RE à parte, pois é constante por município e seria absorvida pelos efeitos fixos municipais | H4 |
| Clima | Anomalia de precipitação | `br_clima_precipitacao_uf.csv::anomalia_precipitacao_pct`, casado por `sigla_uf` e `ano` | controle/H4 |

### 6.2.1 Painel consolidado e missingness — executado

`br_painel_analise_final.csv` — todas as bases unidas por `id_municipio`×`ano` (clima por
`sigla_uf`×`ano`), com `investimento_percapita`, `cv_investimento_5a`,
`prop_financiamento_oneroso` e as variáveis de perdas já defasadas em 1 ano
(`*_lag1`), prontas para o modelo preditivo do objetivo 2.

**Cobertura por variável (painel completo 1995–2022 vs. sub-período 2002–2022):**

| Variável | 1995–2022 | 2002–2022 |
|---|---|---|
| ICR_SM | 80,5% | 89,4% |
| investimento_percapita (lag1) | 66,9% | 77,6% |
| cv_investimento_5a (lag1) | 54,8% | 63,8% |
| prop_financiamento_oneroso (lag1) | 43,7% | 50,5% |
| indice_perda_faturamento (lag1) | 74,6% | 86,4% |
| indice_atendimento_urbano_agua | 78,7% | 87,2% |
| **indice_coleta_esgoto** | **33,1%** | **37,8%** |
| PIB per capita / crescimento / clima | 85–100% | 90–100% |

**Amostra final (listwise, todas as variáveis do modelo H1/H2 não-nulas):** 41.720
observações município-ano, **4.707 municípios distintos (85% dos 5.549 do painel
original)**, 2001–2021. Adicionar PIB/crescimento/clima (para H4) praticamente não reduz
mais a amostra (41.573 linhas) — essas bases já estão quase completas no período 2002+.
**Conclusão prática: o modelo principal (H1/H2/H4) tem N e cobertura de municípios
suficientes para ser robusto.**

**Alerta sério — cobertura de esgoto:** `indice_coleta_esgoto` só está disponível em
~33–38% do painel, muito abaixo de todas as outras variáveis. Isso compromete a parte do
objetivo 3 e H4b que depende de esgoto. Decisão: usar `indice_atendimento_urbano_agua`
(87% de cobertura) como variável de cobertura principal no trade-off e na projeção 2033;
tratar esgoto como análise secundária/robustez, com a limitação de amostra menor
declarada explicitamente — não misturar os dois num único índice sem declarar o
desbalanceamento.

### 6.3 Método de estimação

- **Modelo principal:** painel com efeitos fixos duplos (município + ano), erro-padrão
  clusterizado por município. Absorve características fixas do município (geografia,
  natureza do prestador não observada) e choques nacionais por ano (inflação, Marco Legal
  do Saneamento 2020).
- **Estrutura temporal — defasagem, não contemporaneidade:** as variáveis de planejamento
  (`CV_investimento`, `investimento_percapita`, `prop_financiamento_oneroso`) entram
  **defasadas** (janela `t-5` a `t-1` prevendo `ICR_SM` em `t`), não no mesmo ano. Isso é
  necessário para sustentar a linguagem de "predizem trajetórias" (objetivo específico 2) e
  para mitigar causalidade reversa: tarifa pior (ICR alto) financia mais investimento no
  mesmo ano, então a versão contemporânea do modelo confundiria as duas direções. Mesmo
  defasado, o resultado deve ser lido como associação preditiva, não causalidade
  identificada — declarar isso explicitamente na discussão.
- **Amostra:** 1995–2022 para especificações que usam só variáveis do SNIS/salário mínimo;
  2002–2022 para especificações que incluem PIB per capita/crescimento/clima (sub-período
  restrito pela cobertura dessas bases).
- **Robustez:** (i) log(ICR-SM) para reduzir assimetria; (ii) classificação binária
  "inacessível" usando thresholds de 3% e 5% (banda internacional) em vez de só a variável
  contínua; (iii) quebra pré/pós Marco Legal do Saneamento (2020) para checar mudança
  estrutural; (iv) versão contemporânea (sem defasagem) reportada lado a lado como checagem
  de sensibilidade, não como especificação principal.

### 6.3.1 Operacionalização da meta 2033 (objetivo específico 3 — antes ausente do modelo)

O objetivo específico 3 cita a meta legal (99% água / 90% esgoto até 2033) como referência
de horizonte, mas a especificação original não tinha nenhuma variável que a usasse — lacuna
identificada e corrigida aqui:

1. Para cada município, extrapolar a tendência histórica de `indice_atendimento_urbano_agua`
   e `indice_coleta_esgoto` (regressão linear simples por município sobre os anos
   disponíveis, ou o componente de ML já cogitado na seção anterior) até 2033.
2. Classificar cada município em **on_track** (projeção ≥ meta) / **at_risk** (projeção
   entre meta e meta−10p.p.) / **will_not_meet** (abaixo disso).
3. Testar H4b: `classificacao_2033 ~ ICR_SM (tendência 1995–2022) + crescimento_populacional
   + investimento_percapita + controles` — verifica se municípios com affordability pior
   também são os que devem ficar mais distantes da meta (a pergunta de trade-off real do
   objetivo 3), em vez de tratar cobertura e affordability como dois modelos desconectados.
4. Como robustez, comparar a inclinação de `ICR_SM` e de `cobertura` ao longo do tempo por
   município (duas séries, mesmo período) — se municípios que mais melhoraram cobertura são
   sistematicamente os que mais pioraram ICR_SM, isso é evidência direta do trade-off, sem
   depender da extrapolação até 2033.
- **Componente complementar (objetivo específico 3):** projeção de cobertura até 2033
  (extrapolação de tendência ou gradient boosting, a decidir) usando as taxas de crescimento
  já calculadas como indicador de demanda futura sobre a rede — não é mais pergunta central,
  serve para checar se ganhos de affordability vêm às custas de cobertura.

**Executado** — `br_projecao_cobertura_2033.csv` (extrapolação linear simples por
município, `indice_atendimento_urbano_agua`; esgoto não projetado por baixa cobertura de
dado — seção 6.2.1). 5.431/5.549 municípios com projeção válida (≥3 anos de dado):

| Classificação nacional | N | % |
|---|---|---|
| on_track (projeção ≥ 99%) | 3.077 | 56,6% |
| at_risk (89–99%) | 1.041 | 19,2% |
| will_not_meet (<89%) | 1.313 | 24,2% |

**Por região (% will_not_meet):** Sul 6,2% — Sudeste 27,6% — Nordeste 32,9% — **Norte
37,0%** (pior posicionado). Confirma desigualdade regional já conhecida na literatura de
saneamento brasileiro, agora com projeção quantitativa até o horizonte legal.

**Por porte (achado contraintuitivo):** municípios de 500 mil+ habitantes têm o **pior**
perfil (38,3% at_risk, apenas 36,2% on_track) — pior que municípios pequenos (<5 mil:
64,0% on_track). Hipótese para a discussão: grandes cidades já perto do teto de cobertura
crescem mais devagar em termos percentuais, e/ou têm bolsões de ocupação irregular mais
difíceis de universalizar; municípios pequenos podem estar perto de 100% com sistemas
simples. Merece nuance na redação, não é necessariamente "cidade grande = pior gestão".

**Teste do trade-off (correlação inclinação cobertura × inclinação ICR_SM, N=5.341):
r = -0,0095 — estatisticamente irrelevante.** Não há evidência de que municípios que mais
avançaram em cobertura ao longo do tempo tenham piorado o ICR_SM mais do que os outros.
**Isso reforça o achado da seção 6.5: não há trade-off sistemático cobertura×affordability
na tendência de longo prazo — os dois se movem de forma largamente independente**, o que é
coerente com affordability sendo majoritariamente estrutural (between-município) e cobertura
sendo mais sensível a dinâmica de crescimento populacional (achado do Modelo 4, H3').

### 6.3.1b Modelo de ML (gradient boosting) — a peça que faltava, adicionada após o usuário notar a lacuna

O plano original (seção 6.3) previa **dois** métodos de projeção — gradient boosting como
principal, extrapolação linear como baseline de comparação — mas só a extrapolação linear
havia sido de fato executada. Corrigido em `scripts/09_modelo_ml_projecao.py`.

**Desenho:** `HistGradientBoostingRegressor` (sklearn) treinado para prever cobertura de
água no ano *t* a partir de features do ano *t-1* (nível defasado + investimento,
crescimento, região, clima), treino em anos ≤2016, teste em 2017–2022. Depois, forecast
recursivo 2023→2033 (a previsão de cada ano realimenta o ano seguinte), usando a
expectativa de crescimento de longo prazo já calculada (seção 5) para os anos sem dado
observado, e persistência do último investimento/perdas observados (suposição declarada).

**Resultado da validação (N=25.978 município-ano, 2017–2022) — achado honesto e
importante:**

| Método | MAE (p.p. de cobertura) | RMSE |
|---|---|---|
| Persistência (repete o último valor observado) | **2,16** — melhor | 8,83 |
| Gradient Boosting (ML) | 3,26 | 8,93 |
| Extrapolação linear por município | 6,47 — pior | 14,45 |

**O modelo de ML não supera o baseline mais ingênuo possível** (simplesmente repetir o
último valor de cobertura observado). A importância de features confirma por quê:
`cobertura_lag1` domina com importância 1,30, e todas as outras variáveis (investimento,
crescimento, PIB, clima) têm importância próxima de zero ou negativa — cobertura é uma
métrica de infraestrutura extremamente persistente ano a ano, e não há sinal preditivo
adicional nas variáveis de planejamento além do próprio nível defasado. Isso é consistente
com o achado da seção 6.5 (affordability é estrutural) e estende a mesma lógica para
cobertura: **ano a ano, muito pouco muda por decisão de planejamento — o que se vê é
inércia estrutural.**

**Concordância ML vs. extrapolação linear na classificação 2033 (N=5.431):** apenas
**33,6%** de concordância exata; diferença média absoluta de **13,8 pontos percentuais**
entre as duas projeções de nível. O ML tende a empurrar a maioria dos municípios para
"at_risk" (73,6% da amostra) em vez de distribuir entre on_track/will_not_meet como a
extrapolação linear faz — sintoma conhecido de forecasting recursivo com árvores: a
previsão regride para a média ao ser aplicada repetidamente, em vez de manter uma
tendência linear consistente.

**Implicação metodológica para o artigo:** nem o ML nem a extrapolação linear têm
validação forte o suficiente para tratar os números de 2033 como previsão pontual
confiável — o próprio exercício de comparação é o resultado mais honesto: **há incerteza
substancial sobre a trajetória de 11 anos à frente, e isso precisa ser comunicado
explicitamente**, não escondido atrás de uma única tabela de classificação. Recomendação:
reportar a extrapolação linear como cenário central (mais interpretável, mais alinhado
com a lógica de tendência histórica que o artigo já usa em outros lugares), mas
apresentar a divergência com o ML como evidência de incerteza, não a esconder.

Arquivos: `br_projecao_cobertura_2033_ml.csv`, `comparacao_metodos_2033.csv`,
`validacao_ml_vs_linear.csv`, `importancia_features_ml.csv`.

### 6.3.2 Projeção de esgoto até 2033 — executado como robustez, apesar da amostra menor

`br_projecao_cobertura_2033_esgoto.csv`. Como esperado pela seção 6.2.1, a cobertura de
dado é bem mais baixa: **apenas 2.971/5.549 municípios (53,5%)** têm projeção válida de
esgoto, contra 97,9% para água. A própria ausência de dado já é um sinal: municípios que
não reportam coleta de esgoto ao SNIS tendem a ser os de infraestrutura mais fraca —
provável viés de seleção otimista nos resultados abaixo (quem não reporta provavelmente
está pior, não está no cálculo).

| Classificação nacional (esgoto, meta 90%) | N | % |
|---|---|---|
| on_track | 1.278 | 43,0% |
| at_risk | 240 | 8,1% |
| will_not_meet | 1.453 | 48,9% |

**Esgoto está muito mais atrasado que água em toda a amostra, inclusive nas regiões que
foram bem em água:**

| Região | will_not_meet água | will_not_meet esgoto | N válido esgoto |
|---|---|---|---|
| Sul | 6,2% | **53,5%** | 465 |
| Sudeste | 27,6% | 38,9% (melhor da amostra) | 1.549 |
| Centro-Oeste | 14,3% | 50,5% | 196 |
| Nordeste | 32,9% | 65,3% | 683 |
| Norte | 37,0% | **73,1%** | **apenas 78** |

O Sul, que lidera em água (93,8% on_track/at_risk), **despenca em esgoto** (quase metade
`will_not_meet`) — evidência de que investimento em água e em esgoto são trajetórias
historicamente desacopladas no Brasil, não um pacote único. O Norte tem o pior
desempenho projetado e, ao mesmo tempo, a menor cobertura de dado (N=78 de ~450
municípios da região) — a fragilidade de reporte acompanha a fragilidade de serviço.

**Cruzamento água×esgoto (N=2.961 municípios com projeção válida para os dois):** dos
1.135 municípios on_track em água, **715 (63%) são `will_not_meet` em esgoto** — reforça
que "bom em água" não implica "bom em esgoto"; são dimensões de planejamento
substancialmente independentes, o que é um argumento direto para a chamada da edição
especial sobre affordability/equidade não poder ser tratada como uma dimensão única do
serviço.

**Limitação a declarar com destaque:** os resultados de esgoto têm N muito menor e viés de
seleção plausível (quem reporta tende a estar em situação melhor) — devem ser
apresentados como suggestive/exploratórios, não com o mesmo peso inferencial dos
resultados de água.

### 6.4 Resultados esperados por hipótese (registro do que foi previsto a priori)

| Hipótese | Equação-alvo | Sinal esperado | O que confirmaria a hipótese |
|---|---|---|---|
| H1 | `ICR_SM ~ CV_investimento + investimento_percapita + controles` | β(CV) > 0 | Maior instabilidade do investimento (picos reativos) associada a affordability pior (ICR mais alto) |
| H2 | `ICR_SM ~ prop_financiamento_oneroso + controles` | β > 0 | Mais dívida no financiamento associada a affordability pior no curto/médio prazo, mesmo controlando por cobertura |
| H3 | `ICR_SM ~ cobertura + regiao × cobertura + controles` | interação significativa, sinal oposto Nordeste vs. Sudeste/Sul | Regiões que mais avançaram em cobertura (N/NE) pagam esse avanço em affordability pior; regiões já universalizadas conseguem cobertura alta sem penalizar ICR |
| H4 | `ICR_SM ~ crescimento_populacional + crescimento_servicos + controles` (e replicar com cobertura como dependente) | β > 0 para ICR_SM; β < 0 para cobertura | Municípios sob maior pressão de crescimento têm affordability pior e/ou cobertura mais distante da meta 2033 |

**Leitura de conjunto esperada:** se H1–H4 forem confirmadas, o artigo sustenta que
affordability não é um resultado neutro de "quanto se investe", mas de **como e sob que
pressão** o investimento é feito — planejamento estável e financiamento próprio produzem
affordability melhor, enquanto crescimento acelerado e dependência de dívida a corroem,
com intensidade desigual entre regiões. Esse é o argumento central para a chamada: mostra
*por que* affordability planning é raro (é mais fácil medir do que produzir sob pressão) e
*onde* políticas de equidade precisam mirar (municípios de alto crescimento, financiamento
oneroso, e a lacuna estrutural Norte/Nordeste).

### 6.5 Resultados obtidos (executado — painel com efeitos fixos duplos, erro clusterizado por município)

Script e saída completa em `resultados_modelo_painel.txt`, na pasta do projeto.

| Hipótese | Resultado real | Veredito |
|---|---|---|
| H1 (instabilidade de investimento → ICR pior) | β(CV investimento, lag1) = -0,015, p=0,56; investimento per capita lag1 p=0,55 | **Não suportada** — nenhuma variável de planejamento é significativa |
| H2 (financiamento oneroso → ICR pior) | β(prop. oneroso, lag1) = 0,035, p=0,33 | **Não suportada** |
| H3 (trade-off cobertura×região) | Cobertura reduz ICR no Sudeste (β=-0,020, p=0,03); interação positiva e significativa em **Norte** (p=0,015) e **Centro-Oeste** (p=0,02); Nordeste **não** significativo (p=0,55) | **Parcialmente suportada** — trade-off existe, mas não onde a hipótese original apontava (Norte/Centro-Oeste, não Nordeste) |
| H4a (crescimento → ICR pior) | β(crescimento serviços) = **-0,0033, p<0,001** (sinal invertido); crescimento populacional não significativo (p=0,16) | **Refutada** — crescimento de serviços associado a affordability *melhor*, não pior |
| H4b (crescimento → cobertura pior) | β(crescimento populacional) = **-0,106, p=0,003** | **Suportada** — pressão populacional reduz cobertura, mesmo não afetando o ICR |
| controle | log(PIB per capita): β=0,56, p<0,001; log(população urbana): β=0,91, p=0,008 (Modelo 3) | Municípios maiores/mais ricos têm ICR pior — confirma o padrão descritivo (seção 6.0) |

**Achado não previsto, mais importante do que qualquer hipótese individual:** no Modelo 1,
R² *between* = 0,85 mas R² *within* ≈ -0,013 (praticamente zero). **Quase toda a variação
do ICR_SM é entre municípios (estrutural/geográfico), não dentro do mesmo município ao
longo do tempo.** Ou seja, affordability parece muito mais uma característica fixa de
"onde você está" do que algo que as variáveis de planejamento de curto prazo aqui medidas
conseguem mover. O teste de poolability (F muito significativo, p<0,0001) confirma que os
efeitos fixos são necessários — não é um artefato de especificação pobre.

**Implicação para a narrativa do artigo:** o achado não é "planejamento não importa", é
mais preciso e mais interessante — **as alavancas de planejamento que o SNIS registra
(investimento, financiamento, perdas) não explicam a variação de curto prazo em
affordability; o que explica é estrutura regional e de porte**. Isso é consistente com o
argumento da introdução (affordability é medida, raramente planejada de fato) e desloca a
pergunta do artigo de "H1–H4 se confirmam?" para "por que o planejamento observável não
move affordability, e o que move?" — uma reformulação mais honesta e mais publicável do
que forçar significância que os dados não sustentam.

**Ajuste recomendado nas hipóteses (a decidir com o usuário antes de redigir):**
- H1/H2 podem ser mantidas como resultado nulo relatado (é uma contribuição legítima —
  “o modelo canônico de finanças de utility não explica variação de affordability no
  Brasil” é um achado publicável), ou reespecificadas com variáveis de estrutura de
  governança (tipo de prestador — extensão descartada na seção 4, pode valer reconsiderar
  aqui, já que a variação *between* alta sugere que características fixas do prestador
  importam mais do que decisões ano a ano).
- H3 deve ser reformulada para citar Norte/Centro-Oeste, não Nordeste, como as regiões
  onde o trade-off cobertura×affordability aparece.
- H4 deve ser desmembrada: a pressão de crescimento afeta **acesso**, não **preço** — essa
  é a hipótese correta a defender, não a original.

**Decisão do usuário (fechada):** manter H1/H2 como estão e reportar o resultado nulo como
achado legítimo — "o modelo canônico de finanças de utility (investimento, financiamento,
perdas) não explica a variação de affordability no Brasil" — e usar a variação
*between*-município de 85% como explicação central do artigo, não como nota de rodapé.
H3 e H4 são reformuladas conforme o resultado real (Norte/Centro-Oeste em vez de Nordeste;
crescimento afeta acesso, não preço). **Não** reabrir a busca por tipo de prestador nem
testar especificações alternativas ad hoc para forçar significância em H1/H2.

## 6.6 Hipóteses finais

Já promovidas para a seção 3 (topo do documento), que é a versão a usar na redação do
artigo — H1'/H2'/H3'/H4' com o veredito de cada uma. Esta seção 6.5 acima é o registro do
raciocínio (hipótese original → resultado → reformulação); a seção 3 é o destino final.

## 7. Limitações a declarar

- Affordability aproximada por tarifa média residencial / salário mínimo, não pela conta
  real de cada domicílio (sem dado de consumo por faixa de renda).
- Salário mínimo nacional é uma referência única para todo o país — não captura variação
  de custo de vida regional; declarar isso explicitamente como limitação e, se for o caso,
  citar literatura que discuta esse uso no contexto brasileiro.
- SNIS é autodeclarado pelas prestadoras — possível viés de subnotificação/qualidade de
  dado em municípios pequenos.
- Anomalia de precipitação medida por UF (capital como ponto de referência), não por
  município — não captura variação climática interna de estados grandes/heterogêneos.
- PIB per capita municipal e valor adicionado de serviços cobrem 2002–2023, não os
  primeiros 7 anos do painel SNIS (1995–2001).

## 8. Estado atual dos dados (todas as bases externas priorizadas já coletadas)

Arquivos na pasta do projeto:
1. `br_mdr_snis_municipio_agua_esgoto.csv` — painel SNIS, 1995–2022.
2. `salario_minimo_1995_2022.csv` — salário mínimo nacional anual.
3. `br_ibge_pib_populacao_municipio.csv` — PIB, população e PIB per capita municipal, 2002–2023.
4. `br_crescimento_populacao_pib_servicos_municipio.csv` — taxas de crescimento ano a ano.
5. `br_expectativa_crescimento_municipio.csv` — CAGR de longo prazo por município (proxy de tendência futura).
6. `br_clima_precipitacao_uf.csv` — precipitação e anomalia climática anual por UF, 1995–2022.

## 9. Estado ao final desta sessão — retomar daqui amanhã

### 9.1 O que está feito e publicado
- Painel completo construído (6 bases externas + SNIS), ICR-SM calculado, estatística
  descritiva rodada (seção 6.0).
- Modelo de painel com efeitos fixos duplos rodado para H1–H4 (seção 6.5).
- Projeção de cobertura até 2033 por extrapolação linear, água e esgoto (seções 6.3.1/6.3.2).
- Modelo de ML (gradient boosting) rodado como checagem de robustez da projeção —
  perdeu para o baseline de persistência, e diverge da extrapolação linear em ~2/3 dos
  municípios (seção 6.3.1b).
- Todo o código salvo permanentemente em `scripts/01` a `scripts/09` (nada mais é
  apagado após rodar — lição da sessão, ver 9.3).
- Relatório visual publicado (gráficos + tabelas):
  https://claude.ai/code/artifact/995d7984-3428-4946-857d-2e8f916db69f

### 9.2 Questão em aberto, levantada pelo usuário no fim da sessão — bloqueia redigir o artigo
**"Os dados trazem isso ou é o seu cruzamento?"** — pergunta central de validade que
precisa ser respondida com testes, não só com uma resposta em texto. Separação feita
nesta sessão:

- **Direto do dado, robusto a especificação:** ICR-SM por região/ano/porte (cálculo, não
  modelo); água×esgoto desacoplados (crosstab simples de duas séries observadas).
- **Depende da especificação do modelo que eu escolhi — ainda NÃO testado com
  especificações alternativas:**
  - "Affordability é 85% estrutural / ~0% gerencial" — é o R² *between/within* **deste**
    modelo (essas 4 variáveis de planejamento, essa janela de defasagem t-5→t-1, esses
    efeitos fixos). Pode mudar com outra especificação.
  - H3 (trade-off Norte/Centro-Oeste) — depende da interação região×cobertura construída
    dessa forma específica.
  - Projeção 2033 — **já demonstrado que é sensível ao método** (linear vs. ML divergem
    em 66% dos municípios), então tratar como cenário com incerteza, não número único,
    já é a decisão tomada.

**Próximo passo travado nisso:** rodar especificações alternativas do Modelo 1 (H1/H2)
antes de redigir o artigo, para checar se "affordability é estrutural" se mantém — por
exemplo: (a) variáveis de planejamento contemporâneas em vez de defasadas, como
sensibilidade; (b) janelas de defasagem diferentes (t-3, t-10) para o CV de investimento;
(c) reconsiderar incluir tipo/natureza jurídica do prestador (descartado na seção 4,
mas a alta variação *between* é justamente o tipo de coisa que characteristics fixas do
prestador poderiam explicar) — decisão de buscar esse dado ou não ainda pendente.

### 9.3 Feedback do usuário nesta sessão (aplicar daqui pra frente)
- **Nunca apagar scripts/código depois de rodar** — tudo tem que ficar salvo e
  reproduzível na pasta do projeto, não só no terminal. (Motivo: usuário não conseguia
  ver nem auditar nada do que foi feito.)
- **Gráficos não podem "maquiar" valor real** — ao mostrar um R² negativo, mostrar
  negativo (eixo que aceita valores abaixo de zero), não inflar para uma barra positiva
  só para "aparecer visualmente".
- **Menos autocrítica/tom de mea-culpa, mais solidez** — reportar achados nulos ou
  inesperados como parte normal de um estudo rigoroso ("o teste mostra X, consistente
  com Y"), não como confissão repetida de erro. Isso não muda o conteúdo dos achados,
  muda o tom de apresentação.
- Antes de apresentar qualquer achado como conclusão do artigo, **separar explicitamente
  o que é cálculo direto do que é resultado condicionado à especificação do modelo** — o
  usuário está atento a isso e vai continuar perguntando.

### 9.4 Robustez do Modelo 1 — testada (`scripts/10_robustez_modelo1.py`)

Quatro especificações, mesma variável dependente (ICR-SM), mesmos efeitos fixos duplos:

| Especificação | N | R² between | R² within | Variáveis significativas |
|---|---|---|---|---|
| Original (defasado, CV 5a) | 41.720 | 0,849 | −0,013 | nenhuma |
| (a) Contemporâneo (sem defasagem) | 44.889 | 0,853 | −0,015 | CV investimento, perdas, log população |
| (b) Defasado, CV janela 3 anos | 40.673 | 0,872 | −0,015 | log população |
| (c) Defasado, CV janela 10 anos | 37.057 | 0,871 | −0,012 | log população |

**O padrão central se sustenta nas três especificações defasadas** (original, 3 anos,
10 anos): R² *between* estável entre 0,85–0,87, R² *within* sempre próximo de zero
(−0,01 a −0,02), nenhuma variável de planejamento significativa. O achado não é
artefato de uma escolha específica de janela de defasagem.

**A única especificação em que variáveis aparecem significativas é a contemporânea (a)**
— exatamente a que remove a defasagem que foi introduzida para mitigar causalidade
reversa (tarifa e investimento determinados no mesmo ano). Os sinais nessa especificação
são difíceis de interpretar causalmente (mais perdas associadas a ICR *menor*, instabilidade
de investimento associada a ICR *menor*) — direção oposta à lógica de causalidade
planejamento→resultado que o artigo testa, e consistente com contaminação por
simultaneidade. Isso reforça, em vez de enfraquecer, a decisão de usar a especificação
defasada como principal.

**Achado secundário consistente:** `log_populacao_urbana` é significativo (p<0,05) em
3 das 4 especificações — municípios maiores têm ICR-SM sistematicamente pior mesmo
controlando por planejamento, efeito que sobrevive à troca de janela de defasagem.

**Conclusão sobre a pergunta de validade da seção 9.2:** "affordability é estrutural,
não gerencial" é um achado robusto à especificação testada aqui — não depende de uma
escolha específica e arbitrária de janela temporal.

### 9.6 Robustez adicional — denominador de renda estadual (inspirado em Fagundes et al. 2025)

Fagundes, Marques & Malheiros (2025, *Water Resources Management*) usam salário médio
**estadual** (PNADC) em vez de um piso nacional único como denominador de affordability.
Testamos essa alternativa (`scripts/11_robustez_renda_estadual.py`), construindo
`ICR_renda_UF` = tarifa residencial ÷ renda média estadual (PNADC, tabela SIDRA 5436,
disponível só 2012–2022 — restringe o teste a esse sub-período).

**Correlação ICR-SM × ICR_renda_UF:** 0,785 (N=49.190) — os dois descrevem o mesmo
fenômeno de forma consistente, mas não idêntica.

**Resultado do Modelo 1 com `ICR_renda_UF` como dependente (N=25.846, 2012–2022):** ao
contrário do painel completo 1995–2022, aqui **duas variáveis de planejamento são
significativas** — instabilidade do investimento (β=−0,027, p=0,005) e proporção de
financiamento oneroso (β=−0,072, p<0,001), ambas com sinal negativo (mais
instabilidade/dívida → ICR *menor*, ou seja, affordability *melhor* — sinal oposto ao
que H1/H2 originais previam).

**Checagem de isolamento — é o denominador ou é o período?** Rodamos o mesmo Modelo 1
com `ICR_SM` (denominador original) na **mesma amostra restrita a 2012–2022**. Resultado:
`prop_financiamento_oneroso_lag1` já aparece significativa (β=−0,187, p<0,001) mesmo
com o denominador nacional — ou seja, **a significância decorre principalmente do
recorte temporal (2012–2022), não da troca de denominador**. O denominador estadual
soma um segundo efeito (instabilidade do investimento também vira significativa), mas
o efeito dominante é de período.

**Interpretação:** o achado "estrutural, não gerencial" é robusto para o painel
histórico completo (1995–2022), mas **não é robusto ao recorte da década mais recente**
— na década de 2012–2022, financiamento oneroso está associado a affordability
*melhor*, não pior. Uma leitura plausível: a década de 2010 incluiu programas de
financiamento subsidiado para saneamento (ex. PAC, linhas BNDES/Caixa), então
"financiamento oneroso" nesse período pode ter significado crédito subsidiado que
viabilizou ganhos de eficiência, não dívida cara no sentido que H2 original supunha —
mas essa é uma hipótese interpretativa, não testada diretamente aqui, e fica registrada
como qualificação importante do achado central, não como contradição dele: **o achado
central vale para a trajetória de longo prazo (28 anos); o padrão recente (2012–2022)
é diferente e merece nota própria na discussão do artigo.**

Arquivos: `dados_brutos_externos/pnadc_renda_uf.json` (dado bruto),
`br_renda_media_estadual_pnadc.csv`, `br_icr_renda_estadual.csv`,
`comparacao_icr_sm_vs_renda_uf.csv`, `robustez_renda_estadual_modelo.txt`.

### 9.5 Próximos passos, em ordem
1. ~~Rodar especificações alternativas do Modelo 1~~ — feito, achado central confirmado
   robusto (seção 9.4).
2. ~~Decidir sobre tipo/natureza jurídica do prestador~~ — **decisão: não buscar.** O dado
   existe (SNIS classifica prestadores por natureza jurídica), mas com fricção de acesso
   maior que as bases já usadas (API antiga da Base dos Dados fora do ar; portal oficial
   exigiria download por série histórica de prestador em formato distinto). O achado
   estrutural já está robusto a 4 especificações — decompor exatamente o que compõe essa
   variação *between* fica registrado como pergunta em aberto para pesquisa futura no
   próprio artigo, não como lacuna a preencher agora.
3. Redigir o artigo (introdução, revisão de literatura, dados/método, resultados,
   discussão, implicações de política). — **em andamento**, ver `artigo_rascunho.md` e
   `sn-article-template/sn-article.tex`.
   - **Introduction** (em inglês, sem travessões/dois-pontos): escrita e revisada — 21
     das 28 referências do `sn-bibliography.bib` citadas.
   - **Related Work** (novo, curto): 3 parágrafos agrupando a literatura (governança/
     eficiência; affordability/tarifas/subsídios; métodos internacionais comparativos)
     + 1 parágrafo final com os 3 gaps que motivam o estudo (teste longitudinal
     ausente; água/esgoto tratados separadamente; sem validação de projeção).
   - Compila limpo com bibtex (estilo `sn-mathphys-num`, citações numeradas `[1]`),
     16 páginas, sem citações indefinidas nas referências reais.
   - **Data and Methods** (novo, seção 3, em inglês, com matemática formal): 7
     subseções (fontes de dados, medida de affordability, variáveis de planejamento,
     estrutura de defasagem, especificação de painel, projeção 2033, ML+validação,
     robustez, software/reprodutibilidade). 10 equações numeradas (tarifa, ICR, CV,
     financiamento, especificação de painel, interação regional, tendência linear,
     extrapolação, classificação por casos, MAE/RMSE). Escrita para permitir replicar
     o pipeline inteiro em outro país/painel trocando só as 4 fontes de dado
     equivalentes, sem mudar o código de estimação.
   - Pendente: Results/Discussion em inglês (já tem conteúdo em português a traduzir),
     Conclusion, Abstract final, título do artigo.
   - **Correção (usuário identificou):** Tabela de robustez (agora Table 3) misturava
     variáveis de controle (log população) com variáveis de planejamento na coluna
     "significativas", parecendo contradizer o texto ("nenhuma variável de planejamento
     significativa"). Corrigido: coluna renomeada para "Vars. de planejamento sig.",
     filtrando só as 4 variáveis de planejamento; efeito de log população movido para
     nota de rodapé + frase própria com o p-valor exato (0,066 na especificação original).
   - **Adicionado (usuário pediu):** seção 3.7 (ML) agora descreve hiperparâmetros de
     treino (300 iterações, profundidade 6, learning rate 0,05, tratamento nativo de
     categórica/missing), corte treino/teste (≤2016 vs. 2017–2022), e uma tabela de
     ablação (importância por permutação, 5 repetições) mostrando que só a cobertura
     defasada tem importância real — todas as outras variáveis são ruído. Isso virou a
     Tabela 1 do artigo (antes da Tabela de robustez, que subiu para Tabela 3).
   - **Adicionado (usuário pediu):** subseção nova 3.7.1 "Data treatment for the
     forecasting model" — explica sem scaling (árvores não precisam), sem imputação
     (missing tratado nativamente pelo algoritmo, aprendendo pra qual ramo mandar),
     split treino/teste estritamente cronológico (nunca aleatório). Acompanhada da
     Figura 2 (`scripts/14_series_temporais_ml.py` → `figuras/15_series_temporais_ml.png`)
     com as 6 séries temporais nacionais que alimentam o modelo (cobertura de água,
     investimento per capita, % financiamento oneroso, perdas, crescimento populacional,
     crescimento de serviços), linha tracejada marcando o corte 2016/2017. Nota:
     financiamento oneroso usa **média**, não mediana — a mediana é degenerada em zero
     porque a maioria dos municípios não usa financiamento oneroso em um dado ano.
   - **Results traduzida para inglês (usuário pediu):** seção 4 inteira reescrita em
     inglês, sem travessões nem dois-pontos, com parágrafo de introdução (mapeando as
     5 subseções) e parágrafo de conclusão que fecha a seção e faz a ponte para a
     Discussão. Números convertidos para convenção inglesa (vírgula = milhar, ponto =
     decimal). Citações a Fagundes et al. removidas do texto de Resultados (mantidas só
     em Related Work/Methods). Tabelas e legendas traduzidas. Pendente, apontado pelo
     usuário como próximo passo: revisar cada subseção uma a uma para aprofundar a
     discussão qualitativa além do que já está nas tabelas.
   - **Mapas regenerados sem título embutido, em inglês** (`scripts/12_mapas_coropleticos.py`
     atualizado) — título/legenda ficam só no `\caption` do LaTeX, não mais na imagem.
   - **4.3 e 4.4 mescladas** numa única subseção ("Where a coverage affordability trade
     off and growth pressure appear"), com frase de transição ligando os dois achados.
   - **Notas de tabela removidas, conteúdo movido para o texto corrido** nas 4 tabelas
     de Resultados (fonte de dados, N válido, corte treino/teste etc. agora estão nos
     parágrafos, não em `\footnotetext`).
   - **Referências cruzadas entre subseções removidas** (nada de "Subsection~\ref{...}"
     dentro de Results) — trocadas por "above"/"below"/"next" em prosa corrida.
   - **Interpretação dos mapas aprofundada com números reais conferidos**: mapa do
     ICR-SM agora discute Amazonas/Maranhão (mais leves) vs. Distrito Federal (outlier
     isolado, ~2x o segundo colocado) vs. Rondônia/Amapá (Norte heterogêneo, não
     uniforme); mapa do gap água×esgoto discute Mato Grosso do Sul como caso mais
     extremo, e inclui ressalva explícita de que os valores "verdes" (água pior que
     esgoto) no Norte são majoritariamente ruído de amostra pequena (n<10 municípios
     com dado de esgoto em AC/AP/RR/AM), exceto Maranhão (n=26, confiável).
   - Suavizada a linguagem de prova definitiva em 4.2 (ver conversa anterior) e mantida
     nesta rodada de edições.
   - **Tabela 4 corrigida** (usuário identificou): não eram 7 colunas, eram 6, mas o
     cabeçalho "Significant planning variables" estava com justificação total (`p{}`
     sem `\raggedright`), esticando o texto e criando ilusão visual de coluna vazia.
     Adicionado `\usepackage{array}` + `>{\raggedright\arraybackslash}` nas duas
     colunas de texto largo.
   - **Section 5 placeholder removida** (era resíduo do template original, nunca editado,
     "This is an example for first level head" com texto de exemplo).
   - **Discussion reescrita inteira em inglês** (seção 5, era só um rascunho curto em
     português com travessões/dois-pontos): agora percorre explicitamente as 4 perguntas
     de pesquisa da Introdução (planejamento não move affordability; trade-off regional
     concentrado, não nacional; crescimento afeta acesso não preço; água/esgoto quase
     independentes) e traz um parágrafo extenso e central sobre o comportamento do ML
     como diferencial metodológico real perante a literatura (ninguém mais nessa área
     valida projeção contra holdout; a convergência entre painel com efeitos fixos e
     forecasting descartado por ablação é o argumento mais forte do artigo). Contribuições
     e alcance dos objetivos aparecem implícitos na argumentação, sem frases do tipo
     "este estudo contribui com". Comparação com Fagundes et al. movida para cá (usando
     `\citep`), fora de Results como pedido antes. **Depois removida de novo** (usuário
     pediu): a Discussão agora apresenta só o que o próprio estudo fez, sem parágrafo de
     comparação/posicionamento frente a outro paper; a agenda de pesquisa futura
     (CadÚnico, ônus de conexão) foi mantida mas reescrita como decorrência dos próprios
     achados, não mais como "extensão sugerida por aquele framework". Citação ao
     Fagundes et al. permanece em Related Work, Methods e Introdução (não foi pedido
     remover de lá).
   - **Previsões de fato adicionadas** (usuário pediu, faltava): `scripts/09_modelo_ml_projecao.py`
     agora salva `holdout_predicoes_ml.csv` (previsões individuais do conjunto de
     teste, não só métricas agregadas). `scripts/15_grafico_predicoes_ml.py` novo,
     gera `figuras/16_previsto_vs_observado.png` (scatter previsto×observado, ML vs.
     persistência, 25.978 pontos). Inserido no artigo logo após a Tabela 6 (validação),
     com interpretação nova: o gráfico mostra visualmente que o ML comprime previsões
     para o centro da distribuição nos extremos (típico de árvores quando uma única
     feature defasada domina o ajuste), explicando *por que* perde para a persistência,
     não só *que* perde.
   - **Fontes de dados explícitas (usuário pediu):** subseção 3.1 agora nomeia cada
     fonte com footnote e URL (SNIS/Ministério das Cidades, IBGE salário mínimo,
     contabeis.com.br, SIDRA tabelas 5938/6579, Open-Meteo) + Tabela 1 nova
     ("Data sources underlying the municipal panel") resumindo provedor/identificador/
     período de cada uma.

### 9.7 Análise de artigo correlato e mapas coropléticos

Analisamos Fagundes, Marques & Malheiros (2025, *Water Resources Management*,
`sn-article-template/referencias/s11269-024-04076-4.pdf`) — mesmo tema, mesma base
(SNIS), mas corte transversal (2021, só prestadoras estaduais) com índice composto de
6 dimensões mapeado por UF, sem painel/efeitos fixos/ML. Usado para:
- Validar a escolha metodológica do ICR-SM (eles também usam fração de salário mínimo
  como denominador para famílias pobres).
- Gerar a robustez de denominador estadual (seção 9.6).
- **Mapas coropléticos por UF** (`scripts/12_mapas_coropleticos.py`), inspirados nas
  Figuras 3–9 do paper — contornos geográficos via API IBGE (`malhas/paises/BR`,
  salvos em `dados_brutos_externos/malha_uf.geojson`): ICR-SM médio por UF, % *will not
  meet* água/esgoto 2033 por UF, e mapa de diferença esgoto−água (evidencia visualmente
  o desacoplamento água×esgoto). Incorporados ao `sn-article.tex` (Figs. 1 e 2) e ao
  relatório visual publicado.
- Posicionamento do artigo na Discussão do `.tex`: nosso estudo é complementar (testa
  se affordability responde a planejamento ao longo do tempo; eles mapeiam onde é pior
  num único ano). CadÚnico (registro de pobreza) e ônus de conexão ficam registrados
  como extensões futuras sugeridas pelo framework deles, não incorporadas aqui.

**Arquivos novos desta etapa:** `scripts/12_mapas_coropleticos.py`,
`dados_brutos_externos/malha_uf.geojson`, `figuras/10` a `13_*.png`.

## 10. Índice de todos os scripts (`scripts/`)

| # | Script | Função |
|---|---|---|
| 01 | `build_painel_icr_sm.py` | Constrói a variável ICR-SM |
| 02 | `descritiva_icr.py` | Estatística descritiva por ano/região/porte |
| 03 | `build_painel_final.py` | Une todas as bases + variáveis defasadas |
| 04 | `check_missing.py` | Relatório de missingness |
| 05 | `run_panel_model.py` | Os 4 modelos de painel principais (H1–H4) |
| 06 | `projecao_2033.py` | Projeção água/esgoto até 2033 + teste de trade-off |
| 07 | `gerar_graficos.py` | Todos os gráficos (PNG) |
| 08 | `gerar_relatorio_html.py` | Relatório HTML consolidado (artifact publicado) |
| 09 | `modelo_ml_projecao.py` | Gradient boosting: validação + projeção recursiva 2033 |
| 10 | `robustez_modelo1.py` | Robustez do Modelo 1 a 4 especificações |
| 11 | `robustez_renda_estadual.py` | Robustez com denominador de renda estadual (PNADC) |
| 12 | `mapas_coropleticos.py` | Mapas por UF (ICR-SM, projeção 2033, gap água×esgoto) |
| 13 | `painel_numeros_nacionais.py` | Infográfico com números nacionais do painel (Fig. 1) |
| 14 | `series_temporais_ml.py` | Séries temporais nacionais das variáveis de entrada do ML (Fig. 2), 300dpi, painéis (a)-(f) sem título embutido |
| 15 | `grafico_predicoes_ml.py` | Previsto vs. observado no holdout 2017-2022, ML vs. persistência (Fig. 5) |

## 11. Ajustes finais na seção de ML (Machine learning forecast and validation)

- **Parágrafo de justificativa do modelo:** adicionado logo após o título da
  subseção, explicando por que gradient boosting foi escolhido em vez de um
  modelo linear (mistura de variável categórica `regiao` com contínuas em
  escalas diferentes, não linearidades/interações plausíveis) e em vez de
  rede neural (painel tabular de tamanho moderado, gradient boosting é o
  benchmark estabelecido para esse tipo de dado, mais fácil de inspecionar via
  permutation importance).
- **Figura 2 (`15_series_temporais_ml.png`) regenerada:** removidos título
  geral e subtítulos de cada painel (antes embutidos na imagem), painéis agora
  identificados apenas por `(a)`–`(f)` em negrito no canto superior esquerdo,
  labels do eixo x removidos (poluíam visualmente), figura ampliada e salva em
  300 dpi (antes 150).
- **Caption da Figura 2 reescrita:** agora declara explicitamente que todos os
  painéis cobrem o mesmo período (1995–2022), explica a linha tracejada
  (fronteira treino/teste 2016/2017) e define o que cada painel (a)–(f)
  representa (a = cobertura de água, b = investimento per capita, c = share de
  financiamento oneroso, d = índice de perda de faturamento, e = crescimento
  populacional, f = crescimento do valor adicionado de serviços).
- Compilação verificada limpa (`pdflatex`×2 + `bibtex`, 26 páginas, sem
  erros), páginas 8–9 inspecionadas visualmente via `pdftoppm`.

## 12. Fechamento do artigo (Conclusion, Acknowledgements, título e resumo)

- Reescrita a seção Conclusion (antes placeholder genérico do template):
  três parágrafos declarando o objetivo do estudo, como e por que foi
  atingido, retomando as quatro perguntas de pesquisa, e fechando com
  limitações e trabalhos futuros em um único parágrafo (registro de pobreza
  CadÚnico, custo de conexão inicial, incerteza da extrapolação até 2033).
- Removida a seção "Supplementary information" (placeholder, sem material
  suplementar real). "Acknowledgements" reescrito agradecendo CAPES e UNEB.
- Seção "Robustness and reproducibility" (antes subsection 3.3) transformada
  em `\paragraph{Robustness checks.}` fluido dentro da subseção 3.2, com
  referências explícitas a `Table~\ref{tab_robustez}` e à Seção de Resultados
  para indicar onde cada um dos três checks é reportado.
- Título e resumo revisados por não refletirem o achado real (ver seção 13).

## 13. Revisão por IA externa e reestruturação para a special issue

Usei um prompt de revisor de pares (fornecido ao usuário) para obter uma
crítica externa rigorosa do manuscrito. A revisão apontou fragilidades reais
que motivaram uma rodada de ajustes (mantendo os resultados empíricos
intactos, sem reprocessar os scripts):

- **Título e resumo overclaiming:** "Affordability Is Structural Not Planned"
  transformava um resultado de não significância em conclusão causal/
  ontológica. Novo título: "Testing Whether Utility Planning Moves Water and
  Sanitation Affordability A Three Decade Municipal Panel and Coverage
  Forecast for Brazil". Resumo reescrito para declarar o que foi testado e
  hedgear apropriadamente o que foi encontrado.
- **Descompasso lógico ML×affordability:** o modelo de gradient boosting
  prevê cobertura (`Cov_it`), não ICR-SM. O texto (resumo, Results 4.4,
  Discussion, Conclusion) tratava o fracasso do ML frente à persistência como
  "corroboração independente" do achado de affordability. Corrigido em todas
  as seções para deixar claro que é um "achado paralelo sobre uma variável
  distinta", não uma validação direta.
- **ICR-SM reenquadrado explicitamente** como proxy municipal de peso
  tarifário sobre clientes já conectados, não medida direta de affordability
  domiciliar ou de customer equity (Methods, seção 3.1, parágrafo
  "Affordability measure").
- **Nova tabela de equidade por porte municipal** (Table 4, Results 4.1):
  ICR-SM mediano/médio e cobertura de água por 6 classes de tamanho
  populacional, mostrando gradiente quase monotônico (5,7% nos municípios
  <5 mil a 12,2% acima de 500 mil, mais que o dobro), com interpretação
  ligada a customer equity. Números calculados diretamente de
  `br_painel_analise_final.csv` (coluna `porte` já existente no painel).
- **Linguagem causal suavizada** na Discussion e Conclusion (ex. "affordability
  planning offers a poor return on managerial attention" → hedged;
  "reasonably settled" → removido; subseção 4.2 renomeada de "Affordability
  is structural" para "Planning variables show no robust within municipality
  association").
- **Limitações expandidas** na Conclusion para reconhecer explicitamente
  endogeneidade residual mesmo com a defasagem de 1 ano, erro de medição em
  variáveis administrativas autorreportadas, e a instabilidade temporal já
  documentada no robustness check do PNADC 2012–2022.
- **Seção Declarations preenchida** (Data availability e Code availability
  descrevendo as fontes públicas e a pasta `scripts/`; demais itens com
  texto padrão razoável), substituindo o texto genérico do template.
- **Achado metodológico identificado mas NÃO corrigido ainda:** os scripts
  (`03_build_painel_final.py`) constroem `investimento_percapita` e o CV de
  instabilidade a partir de valores nominais do SNIS, sem deflacionar por
  IPCA/IGP. Isso é uma fragilidade real (mistura inflação com instabilidade
  real de investimento ao longo de 1995–2022). Decisão do usuário: não mexer
  nisso por ora, pois exigiria rerodar scripts 03/05/10 e pode alterar
  coeficientes, p-valores e tabelas em todo o artigo. Fica registrado aqui
  como pendência para uma rodada futura caso se decida enfrentar.
- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 29 páginas, sem
  erros nem referências indefinidas), páginas 1, 14 (nova Table 4) e 23
  (Declarations) inspecionadas visualmente via `pdftoppm`.

## 14. Modelo de ML previsto diretamente para affordability (ICR-SM)

Usuário apontou que o texto dizia "o modelo de ML prevê cobertura, não
affordability, e por isso não corrobora diretamente o resultado econométrico
central" e pediu que a rede de fato fizesse essa previsão, com demonstração
real, não apenas uma ressalva textual. Implementado:

- **`scripts/16_modelo_ml_affordability.py`** (novo): espelha o desenho do
  script 09 (HistGradientBoostingRegressor, treino ≤2016, holdout 2017-2022,
  mesmos hiperparâmetros e regressores), trocando o alvo de cobertura para
  ICR-SM, com `icr_sm_lag1` como termo autorregressivo no lugar de
  `cobertura_lag1`. Resultado real (não estimado, rodado de fato):
  - Persistência: MAE 0.48 p.p., RMSE 1.26 p.p.
  - Gradient boosting (ML): MAE 0.56 p.p., RMSE 1.28 p.p.
  - Extrapolação linear por município: MAE 1.97 p.p., RMSE 2.89 p.p.
  - O ML perde para a persistência (mesmo padrão do modelo de cobertura), mas
    bate a extrapolação linear por larga margem.
  - Permutation importance mostra uma diferença qualitativa real frente ao
    modelo de cobertura: `log_pib_per_capita` (0.015), `investimento_percapita_lag1`
    (0.009), `indice_perda_faturamento_lag1` (0.004) e `cv_investimento_5a_lag1`
    (0.001) têm contribuição pequena mas genuinamente positiva (não apenas
    ruído negativo como no modelo de cobertura), enquanto financiamento
    oneroso, crescimento de serviços e precipitação seguem negativos/nulos.
  - Saídas: `holdout_predicoes_ml_icr.csv`, `validacao_ml_icr.csv`,
    `importancia_features_ml_icr.csv`.
- **`scripts/17_grafico_predicoes_ml_icr.py`** (novo): gráfico previsto vs.
  observado para ICR-SM (holdout 2017-2022), espelhando o script 15, salvo em
  `figuras/18_previsto_vs_observado_icr.png` (300 dpi).
- **`sn-article.tex` atualizado:**
  - Methods (3.2): nova equação `eq_ml_icr` e parágrafo descrevendo o segundo
    modelo (mesma arquitetura, alvo ICR-SM).
  - Results 4.2 (fim da subseção, antes de 4.3): novo parágrafo + Table 6
    (validação MAE/RMSE) + Table 7 (permutation importance) + Figure 4
    (previsto vs. observado), apresentando o forecast de affordability como
    "teste direto do achado do painel, não por analogia".
  - Resumo, Discussion (parágrafo de ML) e Conclusion atualizados para
    refletir que agora HÁ dois exercícios de forecasting (cobertura E
    affordability), ambos batidos pela persistência, mas com o modelo de
    affordability mostrando um sinal pequeno e genuíno vindo de PIB per
    capita e investimento per capita, nuance que não existia antes.
- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 31 páginas, sem
  erros nem referências indefinidas), páginas 16-18 (nova seção, tabelas e
  Figure 4) inspecionadas visualmente via `pdftoppm`.

### Índice de scripts atualizado (16-19)

| # | Script | Função |
|---|---|---|
| 16 | `modelo_ml_affordability.py` | Gradient boosting prevendo ICR-SM (não cobertura) 1 passo à frente, validação contra persistência e extrapolação linear, + forecast recursivo 2023-2033 |
| 17 | `grafico_predicoes_ml_icr.py` | Previsto vs. observado de ICR-SM no holdout 2017-2022 (Fig. 4) |
| 18 | `projecao_icr_2033_linear.py` | Extrapolação linear do ICR-SM por município até 2033 (espelha script 06 p/ cobertura) |
| 19 | `grafico_projecao_icr_2033.py` | Trajetória nacional observada (1995-2022) + 2 cenários projetados até 2033 (Fig. 7) |

## 15. Projeção da affordability (ICR-SM) até 2033: os dois cenários

Usuário apontou que a Fig. 4 (previsto vs. observado no holdout) já respondia
apenas "quão bem o modelo acerta 1 ano à frente", não "como a affordability
pode estar em 2033" — que é o objetivo final do estudo, ligado diretamente ao
tema da special issue. Faltava projetar o ICR-SM até 2033, como já fazíamos
para cobertura (scripts 06 e 09). Implementado:

- **`scripts/18_projecao_icr_2033_linear.py`** (novo): extrapolação linear
  OLS do ICR-SM por município até 2033 (mesma lógica do script 06, função
  `extrapola`, aplicada a `ICR_SM`). Resultado real: média nacional cai de
  5,69% (último ano observado por município) para 4,47% em 2033, com 36,3%
  dos municípios ainda acima do teto internacional de 5%.
- **`scripts/16_modelo_ml_affordability.py`** estendido com uma parte 4
  (forecast recursivo 2023→2033, mesmo desenho da parte 3 do script 09,
  reusando o modelo já treinado em ≤2016, sem reajuste). Resultado real:
  média nacional SOBE de 5,69% para 6,97% em 2033, com 76,0% dos municípios
  acima do teto internacional — **direção oposta** à extrapolação linear.
- **`scripts/19_grafico_projecao_icr_2033.py`** (novo): reconstrói a
  trajetória ano a ano de ambos os cenários (linear via refit OLS por
  município ano a ano; ML via as colunas anuais 2023-2033 já salvas por
  `16_modelo_ml_affordability.py`) e plota junto com a série observada
  1995-2022, com linha pontilhada no teto internacional de 5%. Salvo em
  `figuras/19_projecao_icr_2033.png` (300 dpi).
- **`sn-article.tex` atualizado** com um novo bloco no fim da Results 4.4
  ("What the affordability trajectory to 2033 could look like"), Table 10
  (breakdown por região, 3 colunas: último observado, linear 2033, ML 2033)
  e Figure 7 (a trajetória). Texto trata a divergência entre os dois métodos
  como incerteza genuína (não um defeito a resolver), explicando os
  mecanismos distintos (linear herda a tendência histórica de valorização
  real do salário mínimo; ML recursivo composta o relacionamento estimado
  ano a ano ao longo de 11 iterações, podendo acumular viés). Resumo,
  Discussion (novo parágrafo respondendo diretamente ao tema da special
  issue) e Conclusion também atualizados para incorporar esse achado.
- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 33 páginas, sem
  erros nem referências indefinidas), páginas 21-23 (nova seção, Table 10,
  Figure 7) inspecionadas visualmente via `pdftoppm`.

## 16. Random Forest + projeção oficial de população do IBGE (correção da Fig. 19)

Usuário notou que a curva do gradient boosting na Fig. 19 parecia "linear
demais" e questionou (a) por que não olhamos mais de perto a curvatura, (b) se
a suposição de crescimento populacional era realista dado o declínio
demográfico brasileiro, e (c) por que não usamos LSTM. Investigação e decisão:

- **A curva do GB não é linear, é côncava/desacelerando** (incrementos anuais
  caindo de +0,16 p.p./ano para +0,07 p.p./ano), convergindo para um ponto
  fixo implícito — só parecia reta pela escala do eixo Y. Confirmado
  numericamente antes de qualquer mudança.
- **LSTM descartada, Random Forest escolhida no lugar**: cada município tem
  no máximo ~27-28 pontos anuais, sequência curta demais para LSTM aprender
  padrão temporal sem overfit. Random Forest é ensemble de árvore (mesma
  família do gradient boosting) mas via bagging (médias de árvores
  independentes) em vez de boosting sequencial, dando uma checagem de
  robustez mais informativa e barata computacionalmente.
- **`scripts/20_ibge_projecao_populacao_uf.py`** (novo): busca a projeção
  oficial de população do IBGE por UF via SIDRA (tabela 7358, "Projeção da
  População", variável 606), anos 2022 e 2033, calcula o CAGR oficial por UF
  (0,09% a 1,49% a.a., média nacional simples 0,685% a.a.). Ainda positivo em
  toda UF nesse horizonte (Brasil só declina após ~2041), mas mais baixo e
  mais realista que o CAGR histórico por município do próprio painel SNIS
  (que não captura a desaceleração). Cache salvo em
  `dados_brutos_externos/ibge_projecao_populacao_uf_raw.json`.
- **`scripts/16_modelo_ml_affordability.py`** reescrito: adiciona
  `RandomForestRegressor` (300 árvores, one-hot + imputação por mediana do
  treino) como 4º método na validação 1-passo-à-frente, e roda o forecast
  recursivo 2023-2033 para os DOIS modelos (GB e RF), agora usando a
  expectativa de crescimento populacional do IBGE por UF em vez do CAGR
  histórico municipal. Resultado real:
  - Validação 1 passo à frente: persistência 0,48 p.p. < RF 0,54 p.p. < GB
    0,56 p.p. << linear 1,97 p.p. (RF bate GB, mas ainda perde pra persistência)
  - Recursivo 2033: GB 5,69%→6,96% (quase idêntico à versão anterior com CAGR
    histórico, confirmando que crescimento populacional tem baixa importância
    no modelo); **RF 5,69%→6,03%**, bem mais conservador.
- **`scripts/19_grafico_projecao_icr_2033.py`** atualizado com 3 linhas
  (linear, RF, GB). A curva do RF agora é visivelmente côncava/saturando (sobe
  rápido e estabiliza perto de 6%), tornando a não-linearidade óbvia
  visualmente — resolve a desconfiança original do usuário.
- **`sn-article.tex` atualizado**: Methods (3.2) ganha parágrafo explicando
  RF + rejeição da LSTM + troca da fonte de crescimento populacional; Table 6
  (validação) ganha linha RF; Table 10 e Figure 7 (Results 4.4) agora têm 3
  cenários; Discussion e Conclusion atualizados para descrever a discordância
  GB×RF como informativa por si só (boosting extrapola tendência, bagging
  puxa para um ponto estável).
- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 34 páginas, sem
  erros nem referências indefinidas), páginas 21-23 inspecionadas
  visualmente via `pdftoppm`.

### Índice de scripts atualizado (20-21)

| # | Script | Função |
|---|---|---|
| 20 | `ibge_projecao_populacao_uf.py` | Busca projeção oficial de população do IBGE por UF (SIDRA 7358), calcula CAGR 2022-2033 |
| 21 | `mapa_projecao_icr_2033.py` | Mapa coroplético do ICR-SM projetado 2033 por UF (média dos 3 métodos) |

## 17. Mapa de projeção 2033 por estado + interpretação de população e renda

Usuário pediu um mapa por UF da projeção de affordability 2033 (no mesmo
estilo do mapa histórico), com uma curva Brasil, e interpretação ligada ao
horizonte populacional e ao IDH. Não achei fonte de IDH por UF acessível sem
autenticação (Atlas Brasil bloqueia scraping com 403, sem tabela no SIDRA,
Kaggle/basedosdados exigem login). Avisei o usuário e usei nível/crescimento
de renda (PIB per capita, já no painel, fonte IBGE SIDRA já citada) como
proxy, nomeado explicitamente como "income", não como IDH, para não
misrepresentar a fonte no texto do artigo.

- **`scripts/21_mapa_projecao_icr_2033.py`** (novo): mesmo estilo/paleta do
  mapa histórico (script 12), mas colorindo pela média dos 3 métodos de
  projeção 2033 (linear, RF, GB) por UF. Salvo em
  `figuras/20_mapa_projecao_icr_2033_uf.png` (300dpi).
- **`scripts/19_grafico_projecao_icr_2033.py`** ajustado: eixo X estendido até
  2034 (antes ia só até 2033), dando respiro visual ao último ponto projetado.
- **Correlações calculadas** (por UF, N=27) entre o ICR-SM projetado 2033
  (média dos 3 métodos) e:
  - crescimento populacional oficial do IBGE 2022-2033: **r = -0,09**
    (praticamente nula) — ex. Amazonas, Acre e Roraima estão entre os
    estados de crescimento populacional mais rápido do país mas têm a
    projeção de affordability mais leve; Rio de Janeiro tem crescimento
    populacional baixo mas projeção pesada. Consistente com o achado do
    painel de que crescimento demográfico pressiona cobertura, não preço.
  - nível médio de renda (PIB per capita) 1995-2022: **r = +0,60** (moderada
    positiva) — estados mais ricos tendem a projeção mais pesada, consistente
    com o padrão já identificado de sistemas full-cost-recovery.
  - crescimento médio de renda per capita: **r = -0,02** (nula) — não é a
    velocidade de crescimento da renda que importa, é o nível.
- **Caveats identificados e registrados no texto**: Distrito Federal (único
  município da UF) tem extrapolação linear colapsando para 0% (declínio
  histórico íngreme extrapolado), enquanto RF e GB projetam >11%, então a
  média de 3 métodos no mapa subestima a discordância nesse caso. Mato
  Grosso do Sul é o estado mais escuro do mapa porque alguns municípios têm
  extrapolações lineares implausivelmente altas (>20%, acima de qualquer
  valor já observado no painel).
- **`sn-article.tex` atualizado**: novo parágrafo + Figure 7 (mapa) inserido
  em Results 4.4 logo após a Table 10, antes da Figure 8 (curva nacional,
  renumerada, agora com eixo até 2034).
- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 35 páginas, sem
  erros nem referências indefinidas), páginas 22-25 inspecionadas
  visualmente via `pdftoppm`.

## 18. IDHM real substitui o proxy de renda (dados fornecidos pelo usuário)

Usuário colocou 6 CSVs exportados do IPEAdata na raiz do projeto (IDHM-renda
por UF 1991-2024, população por UF, e 4 séries só nacionais: Gini Censo,
Gini PNADC, IVS, % população com água encanada). Movidos para
`dados_brutos_externos/` com nomes descritivos.

- **`scripts/22_ipea_idhm_renda_uf.py`** (novo): processa
  `ipeadata_idhm_renda_uf.csv` (27 UFs, 1991/2000/2010 + anual 2012-2024).
  Confirmado numericamente que **nenhum estado teve IDHM-renda em declínio
  1991-2010** (0 de 27). Salvo em `br_idhm_renda_uf.csv`.
- **Correlação real recalculada** (substituindo o proxy de PIB per capita
  usado antes) entre o ICR-SM projetado 2033 (média dos 3 métodos) e:
  - IDHM-renda 2010 (censo): **r = 0,66**
  - IDHM-renda 2024 (mais recente): **r = 0,72** (mais forte que o proxy de
    renda usado antes, r=0,60)
  - crescimento do IDHM-renda 2010-2024: **r = -0,25** (fraca, negativa)
  - Reescrita a seção 4.4 do artigo (parágrafo do mapa) trocando a linguagem
    de "income level/growth proxy" para o índice real, citado com nota de
    rodapé para o IPEAdata. Mencionado especificamente que o Distrito
    Federal tem o maior IDHM-renda do país, consistente com seu maior peso
    tarifário histórico já documentado em 4.1.
- **`ipeadata_agua_encanada_br.csv`** (Atlas DH/Censo, só nacional, 1991:
  71,3% → 2000: 81,8% → 2010: 92,7% de domicílios com água encanada) usado
  como corroboração independente do "near universal water coverage" já
  citado na Introdução, com nota de rodapé.
- **Não usados** (por ora): Gini (Censo e PNADC) e IVS — são só nacionais
  (não têm quebra por UF/município), e não achei um encaixe limpo no texto
  sem misturar níveis de análise (desigualdade de renda domiciliar nacional
  vs. dispersão do peso tarifário médio entre municípios). Ficam disponíveis
  em `dados_brutos_externos/` para uso futuro se surgir um ângulo específico.
- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 36 páginas, sem
  erros nem referências indefinidas), páginas 2, 22 e 23 inspecionadas
  visualmente via `pdftoppm`.

### Índice de scripts atualizado (22)

| # | Script | Função |
|---|---|---|
| 22 | `ipea_idhm_renda_uf.py` | Processa IDHM-renda por UF (IPEAdata), 1991-2024 |

## 19. Rodada de revisão externa: 4 correções estruturais

Usuário trouxe um parecer de revisor com 4 recomendações concretas e pediu
para implementá-las sem adicionar complexidade desnecessária (nada de
variável instrumental, LSTM, GAM, ridge). Todas as 4 foram feitas:

**1) Corrigir a interpretação do resultado principal.** Removida a
linguagem "structural finding" / "affordability behaves as a condition
attached to a place" em Results 4.2, 4.3 e na abertura da Discussion.
Trocado por formulações que não excedem o que o desenho identifica, ex.
"no detectable within municipality association... at an annual horizon",
deixando explícito que o painel com defasagem de 1 ano e 4 variáveis não
testa (nem refuta) planejamento em outros horizontes. Resumo também ganhou
uma cláusula sobre a não uniformidade temporal do resultado.

**2) Tratar o período 2012-2022 com tabela, não só ressalva narrativa.**
Nova **Table 6** ("Planning variable coefficients... full panel and 2012 to
2022") com os coeficientes reais das 3 especificações lado a lado (painel
completo N=41.720, 2012-2022 com ICR-SM original N=29.150, 2012-2022 com
denominador de renda estadual N=25.846), extraídos dos outputs já salvos
(`resultados_modelo_painel.txt`, `robustez_renda_estadual_modelo.txt`).
Texto reescrito para a interpretação sugerida ("o resultado nulo predomina
mas não é temporalmente uniforme... reflete possíveis mudanças
institucionais ou financeiras").

**3) Simplificar radicalmente a seção 2033.** Mudança mais substancial:
- **Removida a média entre os 3 métodos** e o mapa que dependia dela
  (Figure 7 antiga, `20_mapa_projecao_icr_2033_uf.png`, e todo o parágrafo
  de correlação com IDHM-renda/crescimento populacional construído na
  rodada anterior). O script 21 e a análise de IDHM (script 22) NÃO foram
  apagados (mandato de nunca apagar código), mas ficam documentados como
  "construído, não usado no artigo final" no novo `scripts/README.md`.
- **Table 10 antiga (breakdown regional 3 métodos) removida**, substituída
  por uma tabela nacional simples de 3 linhas (Método | ICR-SM 2033 |
  Interpretação), exatamente como sugerido pelo usuário.
- Linguagem de "range provável" removida do resumo, Discussion e Conclusion
  (ex. "bracketed range of genuine uncertainty" → "three conditional
  scenarios... none is offered as a central estimate or a likely range").
  Caption da Figure (curva nacional, agora Fig. 7) declara explicitamente
  "None of the three is validated as an eleven year forecast".
- DF e MS reduzidos a uma frase curta (antes: parágrafo inteiro).
- Nenhum modelo novo adicionado (LSTM/GAM/ridge descartados, como pedido).

**4) Disponibilização de código.** Não consigo criar um depósito Zenodo de
fato (ação externa, requer conta/upload manual do usuário). Texto do
Data/Code availability atualizado para declarar intenção de depósito no
Zenodo com DOI antes da publicação. Criado **`scripts/README.md`** real e
completo: ordem de execução de todos os 22 scripts, o que cada um lê/escreve,
versões exatas do ambiente (Python 3.12.10, pandas 2.3.3, numpy 2.5.1,
scikit-learn 1.9.0, matplotlib 3.11.1, geopandas 1.1.4, linearmodels 7.0),
seeds usadas (`random_state=42` em todos os modelos estocásticos) e lista de
fontes externas com URLs. Isso deixa o depósito pronto para quando o usuário
efetivamente subir no Zenodo e me passar o DOI real para inserir no artigo.

- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 35 páginas,
  sem erros nem referências indefinidas), páginas 17 (Table 6), 23-24
  (seção 2033 simplificada) inspecionadas visualmente via `pdftoppm`.

## 20. Segunda rodada do mesmo revisor: 4 ajustes objetivos finais

Revisor confirmou que os 4 pontos maiores (interpretação causal, período
2012-2022, cenários 2033, reprodutibilidade) foram corrigidos, e pediu 4
ajustes menores antes de considerar o artigo pronto para submissão:

**A) Título trocado.** De "Testing Whether Utility Planning Moves Water and
Sanitation Affordability A Three Decade Municipal Panel and Coverage
Forecast for Brazil" (sem pontuação, "moves" sugeria causalidade, só citava
coverage forecast) para "Utility Planning and Water and Sanitation Tariff
Burdens in Brazil: A Three-Decade Municipal Panel and Conditional Scenarios
to 2033" (a opção que o próprio revisor indicou como a que melhor
representa o artigo atual). Esse título usa dois-pontos e hífen
propositalmente, é a exceção já aceita de que a regra "sem travessão/dois
pontos" vale para a prosa do corpo do texto, não para o título.

**B) Resumo reduzido.** Cortado de ~9 frases cobrindo praticamente todos os
achados secundários (trade-off regional, crescimento, clima, água x esgoto)
para 4 frases focadas exatamente nos 4 resultados centrais pedidos: (1)
ausência de associação robusta no painel completo, (2) não uniformidade
2012-2022, (3) gradiente por porte municipal, (4) fraco desempenho preditivo
+ divergência dos 3 cenários 2033.

**C) "customer facing equity gradient" → "municipal-size tariff-burden
gradient"** em todas as 5 ocorrências (resumo, introdução, resultados 4.1,
discussão, conclusão), evitando a insinuação de que o painel mede equidade
entre clientes diretamente (só mede dispersão do indicador agregado por
porte de município).

**D) Erros-padrão agrupados na Table 6.** Adicionados abaixo de cada
coeficiente (clustered at municipality level, os mesmos já usados no resto
do artigo), extraídos dos mesmos outputs salvos
(`resultados_modelo_painel.txt`, `robustez_renda_estadual_modelo.txt`).

- Compilação final verificada limpa (`pdflatex`×2 + `bibtex`, 35 páginas,
  sem erros nem referências indefinidas), página 1 (título/resumo) e página
  17 (Table 6 com SEs) inspecionadas visualmente via `pdftoppm`.
