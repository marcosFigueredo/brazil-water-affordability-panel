# Planejamento estrutural, não gerencial: affordability de água e esgoto no Brasil, 1995–2022

*Rascunho — Edição Especial "Water Utility Planning for Customer Equity Outcomes"*

## Texto curto (leapSpace, 499 caracteres)

> Affordability é discurso comum em saneamento, raramente testada como resultado de
> planejamento. Com 28 anos de dados de 5.549 municípios brasileiros, mostramos que
> investimento, financiamento e perdas não explicam affordability dentro de um mesmo
> município: 85% da diferença está entre municípios, quase 0% no tempo. Há trade-off
> cobertura-tarifa só em Norte e Centro-Oeste; crescimento populacional pressiona o acesso,
> não o preço; água e esgoto seguem trajetórias desacopladas rumo à meta de 2033.

## Palavras-chave para busca de literatura correlata (a resolver referências)

**Inglês:** water affordability; water tariff burden / water pricing equity; water utility
planning; sanitation equity / water justice; income-based water pricing threshold; water
poverty line; household water expenditure share; utility investment panel data; water and
sanitation universal access; customer assistance programs water utilities; water utility
governance Brazil.

**Português:** affordability em saneamento; tarifa social de água; comprometimento de renda
com água e esgoto; planejamento tarifário saneamento básico; universalização do saneamento
Brasil; Marco Legal do Saneamento; SNIS indicadores financeiros; equidade hídrica Brasil;
política tarifária água e esgoto; investimento em saneamento básico municipal.

**Combinações específicas:** "affordability" AND "water utility" AND "Brazil"; "income
commitment ratio" water OR "ICR" saneamento; "Hutton 2012" affordability water sanitation;
"Novo Marco do Saneamento" tarifa OR affordability.

## Resumo

Affordability tornou-se central na agenda de políticas de saneamento, mas o pressuposto de
que o planejamento das prestadoras — nível de investimento, fonte de financiamento, controle
de perdas — determina resultados de affordability raramente é testado em painel longo. Este
artigo testa essa premissa usando 28 anos de dados de praticamente todos os municípios
brasileiros atendidos por serviços de água e esgoto (1995–2022, N até 96.057 observações
válidas, 5.549 municípios). Construímos uma métrica de affordability adaptada do Índice de
Comprometimento de Renda brasileiro — tarifa residencial média como proporção do salário
mínimo nacional (ICR-SM) — e estimamos um painel com efeitos fixos duplos de município e ano.
O resultado central é que as alavancas de planejamento observáveis no principal sistema de
informação do setor (o SNIS) não explicam a variação de affordability dentro do mesmo
município ao longo do tempo: 85% da variância do ICR-SM está entre municípios, e a
componente intramunicipal é estatisticamente nula, um padrão robusto a quatro especificações
alternativas. Encontramos, no entanto, um trade-off cobertura-affordability concentrado nas
regiões Norte e Centro-Oeste; evidência de que a pressão de crescimento populacional afeta o
acesso, não o preço; e trajetórias de água e esgoto substancialmente desacopladas, inclusive
na região com melhor desempenho em água (Sul). Uma projeção da meta legal de universalização
de 2033 mostra incerteza metodológica considerável — dois métodos de projeção concordam em
apenas um terço dos municípios. Argumentamos que affordability, no caso brasileiro, é melhor
compreendida como resultado de condições estruturais herdadas do que como produto de escolha
gerencial de curto prazo — o que tem implicações diretas para o desenho de políticas de
equidade em saneamento.

**Palavras-chave:** affordability; saneamento; planejamento de utilities; equidade hídrica;
Brasil.

---

## 1. Introdução

Affordability é hoje um termo quase obrigatório no vocabulário de políticas de saneamento.
Poucos gestores de utilities negam sua importância; a maioria das agências reguladoras
brasileiras mantém alguma forma de tarifa social; e a literatura internacional consolidou,
desde pelo menos Hutton (2012), uma família de métricas para medi-la. O que permanece pouco
testado é uma premissa mais forte, implícita em boa parte do debate regulatório: a de que
affordability é, em alguma medida relevante, um *produto* do planejamento da prestadora —
que investir de forma mais estável, financiar expansão com recurso próprio em vez de dívida,
e controlar perdas de faturamento deveriam se traduzir em contas mais acessíveis ao longo do
tempo.

Este artigo testa essa premissa diretamente, para o universo de municípios brasileiros
atendidos por serviços de água e esgoto entre 1995 e 2022. Usamos o painel do Sistema
Nacional de Informações sobre Saneamento (SNIS), cruzado com a série do salário mínimo
nacional, PIB e população municipal (IBGE) e uma série climática construída para o período,
para estimar até que ponto a trajetória de affordability de um município é explicada pelas
escolhas de planejamento que o próprio SNIS registra.

A resposta, apresentada em detalhe na Seção 5, é que **não é** — pelo menos não pelas
variáveis e no horizonte que esses dados permitem observar. A variação de affordability entre
municípios brasileiros é ampla e persistente; a variação *dentro* do mesmo município ao longo
do tempo, uma vez controlados os efeitos fixos de local e ano, é estatisticamente
indistinguível de zero. Esse resultado é robusto a diferentes escolhas de janela temporal e
constitui, argumentamos, o achado organizador do artigo: ele desloca a pergunta de pesquisa
de "quais escolhas de planejamento melhoram affordability" — a pergunta que a literatura
regulatória tipicamente faz — para "por que a estrutura parece pesar mais que a escolha, e
o que isso implica para uma agenda de planejamento voltada à equidade".

A partir desse achado central, o artigo examina três extensões que dão conteúdo à resposta:
onde o trade-off entre expandir cobertura e conter tarifas de fato aparece (Seção 5.2); como
a pressão de crescimento populacional e econômico se distribui entre os dois lados do
problema — acesso e preço (Seção 5.3); e o quão previsível é a trajetória de universalização
de água e esgoto até o horizonte legal de 2033 (Seção 5.4), incluindo uma discussão honesta
sobre os limites de qualquer método de projeção sobre um horizonte de onze anos.

---

## 2. Antecedentes

### 2.1 O contexto regulatório brasileiro

O Novo Marco Legal do Saneamento (Lei 14.026/2020) estabeleceu como meta a universalização —
99% de cobertura de água potável e 90% de coleta e tratamento de esgoto — até 31 de dezembro
de 2033, absorvendo o horizonte que já constava do Plano Nacional de Saneamento Básico
(PLANSAB). A lei condiciona a viabilidade econômico-financeira de contratos de concessão ao
cumprimento dessa meta, tornando affordability e universalização formalmente interdependentes
no desenho regulatório — mas sem estabelecer, ela própria, uma métrica ou meta de
affordability equivalente.

### 2.2 Medindo affordability

A literatura internacional sobre affordability de água converge, desde Hutton (2012) — a
referência que orienta o monitoramento da OMS/UNICEF (JMP) —, para métricas de "gasto sobre
renda", com thresholds que variam por instituição: 2,5–4,5% da renda mediana domiciliar para
a EPA americana; cerca de 3–4% para a OCDE; 5% para o Banco Mundial e para o relator especial
da ONU para o direito à água. No Brasil, o precedente direto é o Índice de Comprometimento de
Renda (ICR), usado por agências reguladoras estaduais — a ADASA, do Distrito Federal, entre
elas — e presente na literatura acadêmica nacional (Pereira & Alvez, 2022), definido como a
razão entre a tarifa e a renda domiciliar.

A ausência de uma série longa e municipalizada de renda domiciliar no Brasil — o Censo
Demográfico ocorre a cada década, insuficiente para um painel anual — nos leva a adaptar essa
métrica, substituindo renda domiciliar por salário mínimo nacional no denominador. A escolha
tem precedente indireto na própria prática do IBGE, que define linhas de pobreza em frações
de salário mínimo, e permite construir uma série contínua e comparável para 1995–2022. Essa
adaptação — chamada aqui de ICR-SM — é declarada como limitação de escopo, não como
equivalência ao ICR clássico: descrevemos o peso da tarifa sobre um piso de renda nacional,
não sobre a renda efetiva de cada domicílio.

---

## 3. Objetivos e hipóteses

**Objetivo geral.** Testar se as alavancas canônicas de planejamento de utilities — nível e
estabilidade de investimento, fonte de financiamento, controle de perdas — explicam a
variação de affordability (ICR-SM) no painel de municípios brasileiros atendidos por serviços
de água e esgoto (1995–2022) e, dado o resultado desse teste, caracterizar o que de fato
explica essa variação.

As hipóteses abaixo já incorporam o resultado do teste empírico — a Seção 5 documenta como
cada uma foi avaliada e com que evidência.

- **H1 — Affordability é predominantemente estrutural, não gerencial de curto prazo.** As
  alavancas de planejamento registradas pelo SNIS não explicam variação de affordability
  dentro do mesmo município ao longo do tempo.
- **H2 — O trade-off cobertura-affordability é regionalmente concentrado**, não uniforme
  nacionalmente nem específico à região historicamente mais pobre.
- **H3 — Pressão de crescimento atinge o sistema pelo lado do acesso, não do preço.**
- **H4 — Água e esgoto seguem trajetórias de planejamento desacopladas** em relação à meta de
  universalização de 2033.

---

## 4. Dados e método

### 4.1 Fontes

O painel principal é o SNIS (Sistema Nacional de Informações sobre Saneamento, Ministério das
Cidades), com dados de 1995 a 2022 para 5.549 municípios brasileiros, 119.256 observações
município-ano. Complementamos com quatro bases externas: (i) série anual do salário mínimo
nacional, construída a partir de fonte oficial do IBGE e cruzada com fonte secundária para os
anos mais recentes; (ii) PIB e população municipal (IBGE/SIDRA), 2002–2023, com PIB per
capita calculado (não existe tabela pronta em nível municipal); (iii) taxas de crescimento
populacional e do valor adicionado de serviços (proxy de comércio/serviços privados),
derivadas da mesma fonte; (iv) uma série de anomalia de precipitação por unidade federativa,
1995–2022, construída via reanálise climática (Open-Meteo/ERA5), na ausência de acesso
automatizável às fontes oficiais brasileiras de monitoramento de seca.

### 4.2 Variável dependente

$$
\text{ICR-SM}_{it} = \frac{\text{tarifa média mensal residencial}_{it}}{\text{salário mínimo médio do ano}_t} \times 100
$$

onde a tarifa média mensal residencial é a receita operacional direta de água e esgoto
dividida pelo número de economias residenciais ativas e por doze. Valores negativos ou acima
de 100% (0,2% da amostra, atribuíveis a subnotificação do denominador) foram tratados como
ausentes. A variável está disponível para 96.057 das 119.256 observações do painel (80,5%).

### 4.3 Variáveis explicativas

Investimento per capita e sua estabilidade (coeficiente de variação em janela móvel),
proporção de financiamento oneroso sobre o total investido, perdas de faturamento, porte
populacional (log), região, PIB per capita municipal (log), crescimento populacional e de
serviços, e anomalia de precipitação regional. As variáveis de planejamento entram defasadas
em um ano em relação à variável dependente — não contemporâneas —, para que a estimativa
represente associação preditiva e não seja contaminada pela determinação simultânea de tarifa
e investimento dentro do mesmo exercício orçamentário.

### 4.4 Estimação

Painel com efeitos fixos duplos de município e ano, erro-padrão clusterizado por município.
A especificação absorve características fixas do município (geografia, natureza do prestador
não observada) e choques nacionais comuns a cada ano (inflação, mudanças regulatórias como o
Marco Legal de 2020). A amostra com todas as variáveis do modelo principal não ausentes
compreende 41.720 observações, 4.707 municípios (85% do painel original), 2001–2021.

---

## 5. Resultados

### 5.1 Affordability ao longo do tempo, do espaço e do porte

O ICR-SM mediano nacional caiu de 15,1% em 1995 (amostra pequena, N=28) para uma
estabilização entre 5,2% e 6,1% a partir de 2010 — patamar já acima da banda internacional de
referência (3–5%). Essa queda coincide com o período de valorização real do salário mínimo
(2003–2015), o que significa que parte da melhora aparente decorre do denominador subir mais
rápido que a tarifa, não necessariamente de melhor planejamento tarifário; os efeitos fixos de
ano no modelo de painel absorvem esse componente comum a todos os municípios.

Regionalmente, o padrão é contraintuitivo: o Nordeste — historicamente a região com pior
cobertura — tem o ICR-SM mediano mais baixo do país (4,8%), e o Sul, com a melhor cobertura,
tem o mais alto (8,0%). A leitura mais plausível é que tarifas no Nordeste tendem a subsidiar
mais fortemente o acesso, enquanto o Sul opera com recuperação de custo mais plena. Por porte,
a relação é monotônica: municípios acima de 500 mil habitantes pagam, em mediana, mais que o
dobro (12,2%) do que municípios com menos de 5 mil habitantes (5,7%).

### 5.2 O achado central: affordability é estrutural

No modelo de painel com efeitos fixos duplos, nenhuma variável de planejamento defasada —
investimento per capita, estabilidade do investimento, proporção de financiamento oneroso,
perdas de faturamento — é estatisticamente significativa (todos p>0,19). O R² *between*
(fração da variância explicada pela heterogeneidade entre municípios) é 0,85; o R² *within*
(fração explicada pela variação dentro do mesmo município ao longo do tempo) é
estatisticamente nulo (−0,013).

Este padrão se mantém robusto a três especificações alternativas de janela temporal — CV de
investimento em 3, 5 e 10 anos —, sempre com R² *between* entre 0,85 e 0,87 e nenhuma
variável de planejamento significativa. A única especificação em que variáveis de
planejamento aparecem significativas é a contemporânea, sem defasagem — precisamente a
especificação mais exposta a causalidade reversa (tarifa e investimento decididos no mesmo
exercício), e cujos sinais (mais perdas associadas a affordability *melhor*) são difíceis de
reconciliar com uma leitura causal de planejamento para resultado. Essa comparação reforça,
em vez de enfraquecer, a interpretação estrutural: uma vez que se controla adequadamente pela
simultaneidade, a variação de curto prazo nas alavancas de planejamento não move
affordability.

Um efeito secundário consistente atravessa as especificações: municípios maiores têm ICR-SM
sistematicamente pior, mesmo controlando por planejamento e efeitos fixos — coerente com o
padrão descritivo da Seção 5.1.

**O achado central vale para o painel histórico completo, mas não para a década mais
recente isoladamente.** Seguindo Fagundes et al. (2025), que usam salário médio estadual
(PNADC) em vez de um piso nacional único, reconstruímos a affordability com esse
denominador alternativo — disponível apenas para 2012–2022. Nesse sub-período, duas
variáveis de planejamento passam a ser significativas: instabilidade do investimento
(β=−0,027, p=0,005) e proporção de financiamento oneroso (β=−0,072, p<0,001), ambas com
sinal oposto ao previsto por H1/H2 originais (mais instabilidade ou mais dívida associadas
a affordability *melhor*, não pior). Uma checagem de isolamento — o mesmo modelo com o
ICR-SM original, restrito à mesma amostra 2012–2022 — mostra que financiamento oneroso já
é significativo mesmo sem trocar o denominador (β=−0,187, p<0,001): a divergência decorre
majoritariamente do recorte temporal, não da escolha de denominador. Uma leitura plausível
é que a década de 2010 incluiu programas de financiamento subsidiado ao saneamento (PAC,
linhas BNDES/Caixa), de modo que "financiamento oneroso" no período pode ter significado
crédito subsidiado viabilizando eficiência, não dívida cara no sentido pressuposto pela
hipótese original — leitura interpretativa, não testada diretamente aqui. O achado
estrutural permanece válido para a trajetória de 28 anos; o padrão recente é distinto e
tratado como qualificação, não como refutação, na Seção 6.

### 5.3 Onde o trade-off cobertura-affordability aparece

Interagindo cobertura de água com região (base: Sudeste), cobertura reduz o ICR-SM no
Sudeste (β=−0,020, p=0,03). As interações com Norte (β=+0,025, p=0,015) e Centro-Oeste
(β=+0,025, p=0,02) são positivas e significativas — nessas regiões, ganhos de cobertura vêm
acompanhados de piora de affordability. A interação com Nordeste não é significativa
(β=+0,008, p=0,55): a região historicamente mais atrasada em cobertura não exibe o mesmo
trade-off, resultado que qualifica H2 — o trade-off é real, mas concentrado em duas regiões
específicas, não generalizável a "regiões que avançam em cobertura".

### 5.4 Crescimento: pressão sobre o acesso, não sobre o preço

Crescimento populacional reduz cobertura de água (β=−0,106, p=0,003) sem efeito
estatisticamente significativo sobre affordability (β=−0,019, p=0,16). Crescimento do valor
adicionado de serviços — proxy de dinamismo econômico local — está associado a affordability
*melhor* (β=−0,0033, p<0,001), plausivelmente porque a ampliação da base de economias
residenciais e da capacidade de pagamento dilui custos fixos mais rápido do que amplia
demanda por expansão de rede. O quadro geral sustenta H3: pressão de crescimento tensiona o
sistema pelo lado do acesso, não do preço.

### 5.5 Água e esgoto até 2033: trajetórias desacopladas e projeção incerta

Uma extrapolação de tendência histórica por município projeta 56,6% dos 5.431 municípios com
dado suficiente como *on track* para a meta de 99% de cobertura de água até 2033, 19,2%
*at risk* e 24,2% *will not meet*. A desigualdade regional é acentuada: 6,2% dos municípios
do Sul estão projetados a não cumprir a meta de água, contra 37,0% no Norte.

Para esgoto (meta de 90%), a cobertura de dado cai para 53,5% dos municípios — a própria
ausência de dado é informativa, dado que municípios sem reporte tendem a ter infraestrutura
mais fraca. Entre os que reportam, 48,9% estão projetados a não cumprir a meta de esgoto,
contra 24,2% em água. Notavelmente, o Sul — líder em água — tem 53,5% dos municípios
projetados a não cumprir a meta de esgoto, taxa próxima à do Nordeste em água. Dos municípios
*on track* em água, 63% estão *will not meet* em esgoto: cobertura de um serviço não prediz
cobertura do outro, confirmando H4.

Testamos ainda se municípios que mais avançaram em cobertura ao longo do tempo pioraram
affordability mais que os demais — o teste direto do trade-off dinâmico. A correlação entre a
inclinação temporal da cobertura e a inclinação temporal do ICR-SM, por município (N=5.341),
é −0,0095: estatisticamente irrelevante. Não há evidência de trade-off sistemático de longo
prazo entre expandir cobertura e conter tarifas.

Por fim, avaliamos a confiabilidade da própria projeção 2033, comparando a extrapolação
linear com um modelo de gradient boosting treinado para prever cobertura um ano à frente
(validado em 2017–2022) e depois projetado recursivamente até 2033. Na validação, o modelo de
aprendizado de máquina foi superado pelo baseline mais simples possível — repetir o último
valor observado (erro médio de 2,16 pontos percentuais contra 3,26 do modelo de ML e 6,47 da
extrapolação linear) —, reforçando que cobertura de infraestrutura é uma métrica de forte
inércia estrutural, pouco sensível a variáveis de planejamento mesmo no horizonte de um ano.
Ao projetar até 2033, os dois métodos concordam em apenas 33,6% dos municípios, com diferença
média de 13,8 pontos percentuais entre as duas projeções de nível. Reportamos a extrapolação
linear como cenário central por ser mais interpretável, mas essa divergência deve ser lida
como evidência de incerteza real sobre a trajetória de onze anos à frente, não como uma
previsão pontual confiável.

---

## 6. Discussão

O conjunto de resultados sustenta uma leitura que se afasta do pressuposto regulatório comum
de que affordability é primariamente um produto de escolhas gerenciais de curto prazo. Ela se
comporta, nos dados brasileiros, muito mais como uma característica estrutural, herdada e
persistente do local — mais próxima de geografia, história de investimento acumulada e porte
do que de decisões anuais de investimento ou financiamento observáveis no SNIS. Isso não
significa que planejamento seja irrelevante: significa que seus efeitos, se existem, operam
em constantes de tempo mais longas, por canais que este desenho — limitado às variáveis que o
sistema de informação nacional registra — não captura, ou through características do
prestador (natureza jurídica, capacidade técnica) que não fazem parte do SNIS agregado por
município e ficam como agenda de pesquisa futura.

Essa leitura ajuda a explicar por que affordability planning é raro, questão levantada na
chamada desta edição especial: é mais fácil medir affordability a posteriori do que produzi-la
deliberadamente, porque as alavancas convencionalmente associadas a bom planejamento — mais
investimento, financiamento próprio, menos perdas — não aparecem, nos dados, como
suficientes para mover o resultado no horizonte observável a um gestor ou regulador.

O trade-off regional concentrado em Norte e Centro-Oeste, e a natureza desacoplada das
trajetórias de água e esgoto, sugerem que uma agenda de equidade em affordability precisa ser
regional e setorialmente específica, não um objetivo único nacional. E a divergência entre
métodos de projeção para 2033 é, ela mesma, um resultado substantivo: comunicar uma única
cifra de "quantos municípios vão universalizar" sem essa margem de incerteza seria enganoso.

---

## 7. Limitações

ICR-SM aproxima affordability pela tarifa residencial média sobre salário mínimo, não pela
conta real de cada domicílio nem por renda domiciliar efetiva — a métrica descreve peso sobre
um piso de renda nacional, sensível a política de valorização do salário mínimo, não variação
de renda local. A cobertura de dado de esgoto é substancialmente menor que a de água (33–38%
do painel), com provável viés de seleção otimista nos resultados de esgoto. PIB per capita,
crescimento e clima cobrem 2002 em diante, não o painel completo desde 1995. O SNIS é
autodeclarado pelas prestadoras, com possível subnotificação em municípios pequenos. A
projeção até 2033 é extrapolação de tendência histórica sob a hipótese de continuidade, não
previsão causal — e a comparação com um método alternativo mostrou divergência substancial,
que deve ser lida como incerteza genuína, não como erro de um dos dois métodos.

---

## 8. Conclusão e implicações de política

Affordability de água e esgoto no Brasil parece ser, majoritariamente, herança estrutural, não
resultado de planejamento de curto prazo observável nos dados que o setor coleta de si mesmo.
Para políticas de equidade hídrica, isso desloca o alvo: intervenções que assumem que
melhorar processos de investimento ou financiamento nos moldes hoje registrados pelo SNIS vai,
por si, mover affordability, encontram nos dados brasileiros pouco suporte. Intervenções
direcionadas a condições estruturais — capacidade fiscal municipal, desenho tarifário
sensível a porte e região, e políticas específicas para municípios sob pressão de crescimento
populacional (onde o problema é de acesso, não de preço) — têm base empírica mais direta.
A meta legal de 2033 permanece um horizonte útil, mas deve ser comunicada com a incerteza que
lhe é inerente, e tratada como duas metas distintas — água e esgoto — não uma.

---

## Referências (a completar)

- Hutton, G. (2012). *Monitoring "Affordability" of water and sanitation services after 2015*.
- Pereira, G. S.; Alvez, C. M. A. (2022). Disparidades no acesso aos serviços de água e esgoto
  no Distrito Federal do Brasil: reflexões sobre comprometimento da renda. *Revista DAE*,
  70(238), 136–153.
- Brasil. Lei nº 14.026, de 15 de julho de 2020 (Novo Marco Legal do Saneamento).
- [demais referências de literatura internacional de affordability e saneamento brasileiro —
  a incorporar na próxima rodada de revisão]
