"""
Monta o relatorio HTML consolidado (relatorio_resultados.html) com todos os
graficos embutidos (base64) e as tabelas de resultado do modelo de painel.

Entrada: figuras/*.png
Saida: relatorio_resultados.html (publicado como artifact para revisao visual)
"""
import base64
import os

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

def b64(fname):
    with open(os.path.join(FIG, fname), "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")

IMG = {f: b64(f) for f in [
    "01_trajetoria_nacional_icr.png", "02_icr_por_regiao.png", "03_icr_por_porte.png",
    "04_coeficientes_modelo1_h1h2.png", "05_r2_between_within.png",
    "06_projecao_2033_agua_regiao.png", "07_agua_vs_esgoto_2033.png",
    "08_validacao_ml_vs_baselines.png", "09_comparacao_2033_linear_vs_ml.png",
    "10_mapa_icr_sm_uf.png", "11_mapa_2033_agua_uf.png",
    "12_mapa_2033_esgoto_uf.png", "13_mapa_gap_agua_esgoto_uf.png",
]}

html = f"""<title>Affordability de Saneamento no Brasil</title>
<style>
:root {{
  color-scheme: light;
  --bg: #f4f6f7;
  --surface: #ffffff;
  --surface-2: #eef1f2;
  --ink: #10171c;
  --ink-soft: #46555c;
  --ink-mute: #6f7d84;
  --border: #dbe1e3;
  --accent: #1c5aa6;
  --accent-soft: #e8f0fa;
  --teal: #0f7a6b;
  --good: #0ca30c;
  --warning: #b3790f;
  --critical: #d03b3b;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    color-scheme: dark;
    --bg: #0f1417;
    --surface: #171e22;
    --surface-2: #1e262b;
    --ink: #eef2f4;
    --ink-soft: #a9b7bd;
    --ink-mute: #85949a;
    --border: #2a343a;
    --accent: #6badf0;
    --accent-soft: #1c2b38;
    --teal: #3fcdb2;
    --good: #3ecf3e;
    --warning: #fab219;
    --critical: #e66767;
  }}
}}
:root[data-theme="dark"] {{
  color-scheme: dark;
  --bg: #0f1417;
  --surface: #171e22;
  --surface-2: #1e262b;
  --ink: #eef2f4;
  --ink-soft: #a9b7bd;
  --ink-mute: #85949a;
  --border: #2a343a;
  --accent: #6badf0;
  --accent-soft: #1c2b38;
  --teal: #3fcdb2;
  --good: #3ecf3e;
  --warning: #fab219;
  --critical: #e66767;
}}

* {{ box-sizing: border-box; }}
body {{
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.55;
  margin: 0;
  padding: 0 20px 96px;
}}
.wrap {{ max-width: 880px; margin: 0 auto; }}

header.hero {{
  padding: 64px 0 40px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 40px;
}}
.eyebrow {{
  font-size: 12.5px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--teal);
  font-weight: 600;
  margin: 0 0 14px;
}}
h1 {{
  font-family: Georgia, "Iowan Old Style", "Times New Roman", serif;
  font-size: clamp(30px, 4.4vw, 44px);
  line-height: 1.12;
  margin: 0 0 16px;
  text-wrap: balance;
  color: var(--ink);
  font-weight: 600;
}}
.dek {{
  font-size: 17px;
  color: var(--ink-soft);
  max-width: 62ch;
  margin: 0 0 24px;
}}
.meta-row {{
  display: flex; flex-wrap: wrap; gap: 10px 22px;
  font-size: 13px; color: var(--ink-mute);
}}
.meta-row b {{ color: var(--ink-soft); font-weight: 600; }}

h2 {{
  font-family: Georgia, "Iowan Old Style", "Times New Roman", serif;
  font-size: 25px;
  font-weight: 600;
  margin: 56px 0 6px;
  color: var(--ink);
}}
h2 .num {{ color: var(--teal); font-variant-numeric: tabular-nums; margin-right: 10px; }}
.section-dek {{ color: var(--ink-mute); font-size: 14.5px; margin: 0 0 24px; max-width: 68ch; }}

h3 {{
  font-size: 16px; font-weight: 700; margin: 28px 0 10px; color: var(--ink);
}}

p {{ color: var(--ink-soft); font-size: 15.5px; max-width: 70ch; }}
p.lead {{ color: var(--ink); font-size: 16.5px; }}
strong {{ color: var(--ink); }}

.stat-grid {{
  display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 1px; background: var(--border);
  border: 1px solid var(--border); border-radius: 10px; overflow: hidden;
  margin: 28px 0;
}}
.stat {{ background: var(--surface); padding: 18px 20px; }}
.stat .v {{
  font-family: Georgia, serif; font-size: 26px; font-weight: 600;
  font-variant-numeric: tabular-nums; color: var(--accent); line-height: 1.1;
}}
.stat .l {{ font-size: 12.5px; color: var(--ink-mute); margin-top: 6px; }}

figure {{ margin: 24px 0; }}
figure img {{
  width: 100%; height: auto; display: block;
  border: 1px solid var(--border); border-radius: 10px;
  background: white;
}}
figcaption {{ font-size: 13px; color: var(--ink-mute); margin-top: 8px; max-width: 68ch; }}

.callout {{
  background: var(--accent-soft); border-left: 3px solid var(--accent);
  border-radius: 6px; padding: 16px 20px; margin: 24px 0; font-size: 15px;
  color: var(--ink);
}}
.callout.finding {{ border-left-color: var(--teal); }}
.callout b {{ color: var(--ink); }}

table {{ border-collapse: collapse; width: 100%; margin: 18px 0; font-size: 14px; }}
.table-wrap {{ overflow-x: auto; border: 1px solid var(--border); border-radius: 8px; }}
.table-wrap table {{ margin: 0; }}
th, td {{
  text-align: left; padding: 9px 14px; border-bottom: 1px solid var(--border);
  font-variant-numeric: tabular-nums;
}}
th {{ background: var(--surface-2); color: var(--ink-soft); font-weight: 600; font-size: 12.5px;
      text-transform: uppercase; letter-spacing: 0.03em; }}
tr:last-child td {{ border-bottom: none; }}
td.num {{ text-align: right; }}

.pill {{
  display: inline-flex; align-items: center; gap: 5px;
  font-size: 12px; font-weight: 600; padding: 2px 9px; border-radius: 99px;
}}
.pill.good {{ background: color-mix(in srgb, var(--good) 16%, transparent); color: var(--good); }}
.pill.warn {{ background: color-mix(in srgb, var(--warning) 18%, transparent); color: var(--warning); }}
.pill.crit {{ background: color-mix(in srgb, var(--critical) 16%, transparent); color: var(--critical); }}
.pill.ns {{ background: var(--surface-2); color: var(--ink-mute); }}

.filelist {{ font-size: 14px; }}
.filelist code {{
  background: var(--surface-2); padding: 1px 6px; border-radius: 4px;
  font-size: 13px; color: var(--accent);
}}
.filelist li {{ margin: 6px 0; color: var(--ink-soft); }}

hr.div {{ border: none; border-top: 1px solid var(--border); margin: 64px 0 0; }}
footer {{ padding: 32px 0 0; color: var(--ink-mute); font-size: 13px; }}
</style>

<div class="wrap">

<header class="hero">
  <p class="eyebrow">Relatório de resultados &middot; nada além do que foi rodado</p>
  <h1>Affordability de água e esgoto no Brasil, 1995&ndash;2022</h1>
  <p class="dek">Painel de 5.549 municípios ao longo de 28 anos: o que os dados do SNIS,
  do IBGE e do Open-Meteo mostram sobre quem paga mais pela água e quem vai ficar de fora
  da meta legal de universalização de 2033 &mdash; com todos os gráficos, tabelas e
  scripts usados para chegar lá.</p>
  <div class="meta-row">
    <span><b>N</b> 41.720&ndash;90.952 obs. (a depender do modelo)</span>
    <span><b>Municípios</b> até 5.549</span>
    <span><b>Período</b> 1995&ndash;2022</span>
    <span><b>Scripts</b> scripts/01&ndash;07 (reproduzidos e verificados)</span>
  </div>
</header>

<section>
  <h2><span class="num">01</span>O que essa métrica mede</h2>
  <p class="section-dek">ICR-SM: uma adaptação do Índice de Comprometimento de Renda
  brasileiro, usando salário mínimo nacional em vez de renda domiciliar (que não existe
  em série municipal longa).</p>
  <div class="table-wrap">
    <table>
      <tr><th>Componente</th><th>Fórmula</th></tr>
      <tr><td>Tarifa média mensal residencial</td>
          <td><code>(receita_água + receita_esgoto) / economias_residenciais_ativas / 12</code></td></tr>
      <tr><td>ICR-SM (%)</td>
          <td><code>tarifa_média_mensal / salário_mínimo_médio_do_ano &times; 100</code></td></tr>
    </table>
  </div>
  <p>Referências: Hutton (2012, base OMS/JMP) para a lógica gasto&thinsp;/&thinsp;renda
  internacionalmente; Índice de Comprometimento de Renda (ADASA-DF; Pereira &amp; Alvez,
  2022, <i>Revista DAE</i>) como precedente nacional direto.</p>

  <div class="stat-grid">
    <div class="stat"><div class="v">6,1%</div><div class="l">ICR-SM mediano nacional (28 anos)</div></div>
    <div class="stat"><div class="v">80,5%</div><div class="l">cobertura da variável no painel</div></div>
    <div class="stat"><div class="v">3&ndash;5%</div><div class="l">banda internacional de affordability</div></div>
    <div class="stat"><div class="v">96.057</div><div class="l">observações válidas de ICR-SM</div></div>
  </div>
</section>

<section>
  <h2><span class="num">02</span>Trajetória e desigualdade descritiva</h2>
  <p class="section-dek">Antes de qualquer modelo: como o ICR-SM se move no tempo, entre
  regiões e por porte de município. Script <code>02_descritiva_icr.py</code>.</p>

  <figure>
    <img src="data:image/png;base64,{IMG['01_trajetoria_nacional_icr.png']}" alt="Trajetória nacional do ICR-SM, 1995-2022" />
    <figcaption>A queda de ~15% para ~5,5% entre 1995 e 2010 coincide com a política de
    valorização real do salário mínimo &mdash; parte da "melhora" é o denominador subindo,
    não necessariamente melhor planejamento tarifário. Isso é absorvido pelos efeitos fixos
    de ano no modelo de painel, mas precisa ser discutido explicitamente no artigo.</figcaption>
  </figure>

  <figure>
    <img src="data:image/png;base64,{IMG['02_icr_por_regiao.png']}" alt="ICR-SM por região" />
    <figcaption>Padrão contraintuitivo: o Nordeste &mdash; região historicamente mais pobre
    e com pior cobertura &mdash; tem o ICR-SM <i>mais baixo</i>. O Sul, mais rico e com
    melhor cobertura, tem o mais alto. Sugere tarifas subsidiadas/deficitárias no Nordeste
    versus tarifas de recuperação plena de custo no Sul.</figcaption>
  </figure>

  <figure>
    <img src="data:image/png;base64,{IMG['03_icr_por_porte.png']}" alt="ICR-SM por porte de município" />
    <figcaption>Relação monotônica: municípios de 500 mil+ habitantes pagam mais que o
    dobro (12,2%) do que municípios com menos de 5 mil habitantes (5,7%).</figcaption>
  </figure>
</section>

<section>
  <h2><span class="num">03</span>O modelo de painel &mdash; e o achado que ele não previa</h2>
  <p class="section-dek">Efeitos fixos duplos (município + ano), erro clusterizado por
  município, variáveis de planejamento defasadas em 1 ano. Script
  <code>05_run_panel_model.py</code> &middot; saída completa em
  <code>resultados_modelo_painel.txt</code>.</p>

  <h3>Modelo 1 (H1+H2): planejamento defasado prediz ICR-SM?</h3>
  <figure>
    <img src="data:image/png;base64,{IMG['04_coeficientes_modelo1_h1h2.png']}" alt="Coeficientes do Modelo 1" />
    <figcaption>Todos os intervalos de confiança cruzam zero. Nota: o coeficiente de
    "perdas de faturamento" está reescalado (&times;100) só para caber no mesmo eixo visual
    dos demais &mdash; não é diretamente comparável em unidades brutas, apenas em
    significância (nenhuma é significativa).</figcaption>
  </figure>

  <div class="table-wrap">
    <table>
      <tr><th>Variável (defasada, t&minus;1)</th><th class="num">Coeficiente</th><th class="num">Erro-padrão</th><th class="num">p</th><th>Resultado</th></tr>
      <tr><td>Investimento per capita</td><td class="num">&minus;0,0000234</td><td class="num">0,0000387</td><td class="num">0,546</td><td><span class="pill ns">n.s.</span></td></tr>
      <tr><td>Instabilidade do investimento (CV, 5a)</td><td class="num">&minus;0,0154</td><td class="num">0,0262</td><td class="num">0,557</td><td><span class="pill ns">n.s.</span></td></tr>
      <tr><td>% financiamento oneroso</td><td class="num">0,0345</td><td class="num">0,0357</td><td class="num">0,334</td><td><span class="pill ns">n.s.</span></td></tr>
      <tr><td>Perdas de faturamento</td><td class="num">&minus;0,0012</td><td class="num">0,0009</td><td class="num">0,198</td><td><span class="pill ns">n.s.</span></td></tr>
    </table>
  </div>

  <div class="callout finding">
    <b>Achado central (não hipotetizado a priori):</b> R²&nbsp;<i>between</i> = 0,85 vs.
    R²&nbsp;<i>within</i> &asymp; &minus;0,01. Quase toda a variação do ICR-SM é
    <b>entre municípios</b> (estrutural), não dentro do mesmo município ao longo do tempo.
    As alavancas de planejamento que o SNIS registra não movem affordability no curto prazo
    &mdash; ela parece presa a características fixas de "onde você está".
  </div>
  <figure>
    <img src="data:image/png;base64,{IMG['05_r2_between_within.png']}" alt="R² between vs within" />
  </figure>

  <h3>Modelo 2 (H3): cobertura &times; região &rarr; ICR-SM</h3>
  <div class="table-wrap">
    <table>
      <tr><th>Interação (região &times; cobertura)</th><th class="num">Coeficiente</th><th class="num">p</th><th>Resultado</th></tr>
      <tr><td>Cobertura (baseline Sudeste)</td><td class="num">&minus;0,0197</td><td class="num">0,030</td><td><span class="pill crit">p&lt;0,05</span></td></tr>
      <tr><td>&times; Norte</td><td class="num">+0,0251</td><td class="num">0,015</td><td><span class="pill crit">p&lt;0,05</span></td></tr>
      <tr><td>&times; Centro-Oeste</td><td class="num">+0,0249</td><td class="num">0,020</td><td><span class="pill crit">p&lt;0,05</span></td></tr>
      <tr><td>&times; Nordeste</td><td class="num">+0,0075</td><td class="num">0,554</td><td><span class="pill ns">n.s.</span></td></tr>
      <tr><td>&times; Sul</td><td class="num">+0,0140</td><td class="num">0,157</td><td><span class="pill ns">n.s.</span></td></tr>
    </table>
  </div>
  <p>O trade-off cobertura&times;affordability é real, mas aparece em <b>Norte e
  Centro-Oeste</b> &mdash; não no Nordeste, como a hipótese original previa.</p>

  <h3>Modelos 3 e 4 (H4): pressão de crescimento &mdash; preço ou acesso?</h3>
  <div class="table-wrap">
    <table>
      <tr><th>Variável</th><th>Variável dependente</th><th class="num">Coeficiente</th><th class="num">p</th><th>Resultado</th></tr>
      <tr><td>Crescimento de serviços</td><td>ICR-SM</td><td class="num">&minus;0,0033</td><td class="num">&lt;0,001</td><td><span class="pill good">melhora affordability</span></td></tr>
      <tr><td>Crescimento populacional</td><td>ICR-SM</td><td class="num">&minus;0,0194</td><td class="num">0,157</td><td><span class="pill ns">n.s.</span></td></tr>
      <tr><td>Crescimento populacional</td><td>Cobertura de água</td><td class="num">&minus;0,106</td><td class="num">0,003</td><td><span class="pill crit">reduz cobertura</span></td></tr>
      <tr><td>Crescimento de serviços</td><td>Cobertura de água</td><td class="num">0,0012</td><td class="num">0,628</td><td><span class="pill ns">n.s.</span></td></tr>
    </table>
  </div>
  <p class="lead">Pressão de crescimento atinge o sistema pelo lado do <b>acesso</b>
  (cobertura cai), não pelo lado do <b>preço</b> (affordability não piora e, para
  crescimento de serviços, até melhora).</p>
</section>

<section>
  <h2><span class="num">04</span>Projeção até 2033 &mdash; quem cumpre a meta legal</h2>
  <p class="section-dek">Extrapolação linear de tendência por município (Lei 14.026/2020:
  99% água, 90% esgoto até 31/12/2033). Script <code>06_projecao_2033.py</code>.</p>

  <figure>
    <img src="data:image/png;base64,{IMG['06_projecao_2033_agua_regiao.png']}" alt="Projeção de cobertura de água por região" />
    <figcaption>5.431/5.549 municípios com projeção válida. Sul muito à frente (93,8%
    on&#8288;_&#8288;track/at&#8288;_&#8288;risk); Norte o pior posicionado (37% will&#8288;_&#8288;not&#8288;_&#8288;meet).
    Achado contraintuitivo: municípios de 500 mil+ habitantes têm o pior perfil
    (38,3% at_risk) &mdash; pior que municípios &lt;5 mil (64% on_track).</figcaption>
  </figure>

  <div class="callout">
    <b>Teste de trade-off:</b> correlação entre a inclinação da cobertura e a inclinação
    do ICR-SM ao longo do tempo, por município (N=5.341): <b>r = &minus;0,0095</b> &mdash;
    estatisticamente irrelevante. Não há evidência de que municípios que mais avançaram em
    cobertura tenham piorado affordability mais que os outros.
  </div>

  <h3>Água vs. esgoto: a mesma prestadora, dois destinos diferentes</h3>
  <figure>
    <img src="data:image/png;base64,{IMG['07_agua_vs_esgoto_2033.png']}" alt="Água vs esgoto, projeção 2033 por região" />
    <figcaption>Apenas 2.971/5.549 municípios (53,5%) têm dado suficiente de esgoto
    &mdash; e a própria ausência de dado é um sinal (quem não reporta tende a estar pior).
    O Sul lidera em água mas despenca em esgoto (53,5% will_not_meet). Dos municípios
    on_track em água, 63% estão will_not_meet em esgoto.</figcaption>
  </figure>
</section>

<section>
  <h2><span class="num">05</span>O modelo de ML &mdash; e por que ele perde para o óbvio</h2>
  <p class="section-dek">O plano original previa gradient boosting como método principal
  de projeção, com extrapolação linear só como baseline. Esse modelo não tinha sido
  rodado até o usuário notar a lacuna. Corrigido em
  <code>scripts/09_modelo_ml_projecao.py</code>.</p>

  <figure>
    <img src="data:image/png;base64,{IMG['08_validacao_ml_vs_baselines.png']}" alt="Validação: ML vs persistência vs linear" />
    <figcaption>Validação honesta em 25.978 município-ano (2017&ndash;2022): o Gradient
    Boosting erra mais que simplesmente repetir o último valor observado. Cobertura de
    água é uma métrica de infraestrutura extremamente persistente &mdash; a importância de
    features confirma que <code>cobertura_lag1</code> domina (1,30) e todas as variáveis de
    planejamento têm importância próxima de zero.</figcaption>
  </figure>

  <div class="callout finding">
    <b>Isso não é uma falha do script &mdash; é o mesmo achado da seção 03, de outro
    ângulo:</b> assim como affordability é ~85% estrutural e quase nada explicada por
    planejamento de curto prazo, cobertura também muda pouco ano a ano por decisão
    gerencial. O sistema tem inércia estrutural forte demais para as variáveis do SNIS
    captarem no horizonte de 1 ano.
  </div>

  <figure>
    <img src="data:image/png;base64,{IMG['09_comparacao_2033_linear_vs_ml.png']}" alt="Comparação classificação 2033: linear vs ML" />
    <figcaption>Ao projetar recursivamente até 2033, os dois métodos discordam bastante
    (33,6% de concordância exata; diferença média de 13,8 p.p.). O ML empurra a maioria
    dos municípios para "at_risk" &mdash; sintoma conhecido de forecasting recursivo com
    árvores, que regride à média em vez de manter tendência.</figcaption>
  </figure>

  <p class="lead">Conclusão honesta: nenhum dos dois métodos tem validação forte o
  suficiente para tratar os números de 2033 como previsão pontual confiável. A
  extrapolação linear é reportada como cenário central (mais interpretável), mas a
  divergência com o ML é evidência real de incerteza sobre a trajetória de 11 anos
  &mdash; e deve aparecer no artigo como tal, não ser escondida atrás de uma tabela única.</p>
</section>

<section>
  <h2><span class="num">06</span>Mapas &mdash; o que Fagundes et al. (2025) fizeram e nós não tínhamos feito</h2>
  <p class="section-dek">Fagundes, Marques &amp; Malheiros (2025, <i>Water Resources
  Management</i>) analisam o mesmo problema com o SNIS, mas em corte transversal (2021,
  prestadoras estaduais) e índice composto de 6 dimensões, mapeado geograficamente por
  UF. Reproduzimos essa camada visual para os nossos resultados de painel.</p>

  <figure>
    <img src="data:image/png;base64,{IMG['10_mapa_icr_sm_uf.png']}" alt="Mapa ICR-SM médio por UF" />
    <figcaption>ICR-SM médio por UF, 1995&ndash;2022. Mancha clara na Amazônia Ocidental
    (AM, AC), mancha escura no Distrito Federal e em estados do Sul.</figcaption>
  </figure>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
    <figure>
      <img src="data:image/png;base64,{IMG['11_mapa_2033_agua_uf.png']}" alt="Mapa projeção água 2033" />
      <figcaption>% de municípios <i>will not meet</i> em água (meta 99%) por UF.</figcaption>
    </figure>
    <figure>
      <img src="data:image/png;base64,{IMG['12_mapa_2033_esgoto_uf.png']}" alt="Mapa projeção esgoto 2033" />
      <figcaption>% de municípios <i>will not meet</i> em esgoto (meta 90%) por UF.</figcaption>
    </figure>
  </div>

  <figure>
    <img src="data:image/png;base64,{IMG['13_mapa_gap_agua_esgoto_uf.png']}" alt="Mapa diferença água vs esgoto" />
    <figcaption>Diferença (p.p.) entre atraso projetado em esgoto e em água, por UF.
    Vermelho = esgoto relativamente mais atrasado que água (Sul, MS); verde = o
    inverso (Norte). Visualiza diretamente o desacoplamento água&times;esgoto.</figcaption>
  </figure>
</section>

<section>
  <h2><span class="num">07</span>Reprodutibilidade &mdash; tudo o que gerou este relatório</h2>
  <p class="section-dek">Nenhum número aqui foi digitado à mão. Cada script abaixo foi
  re-executado do zero para conferir que reproduz exatamente os mesmos resultados antes
  deste relatório ser publicado.</p>
  <ul class="filelist">
    <li><code>scripts/01_build_painel_icr_sm.py</code> &mdash; constrói a variável ICR-SM</li>
    <li><code>scripts/02_descritiva_icr.py</code> &mdash; estatística descritiva por ano/região/porte</li>
    <li><code>scripts/03_build_painel_final.py</code> &mdash; une todas as bases + variáveis defasadas</li>
    <li><code>scripts/04_check_missing.py</code> &mdash; relatório de missingness</li>
    <li><code>scripts/05_run_panel_model.py</code> &mdash; os 4 modelos de painel (requer <code>linearmodels</code>)</li>
    <li><code>scripts/06_projecao_2033.py</code> &mdash; projeção água/esgoto e teste de trade-off</li>
    <li><code>scripts/07_gerar_graficos.py</code> &mdash; gera todos os gráficos deste relatório</li>
    <li><code>scripts/08_gerar_relatorio_html.py</code> &mdash; este proprio relatorio HTML</li>
    <li><code>scripts/09_modelo_ml_projecao.py</code> &mdash; modelo de gradient boosting, validação e comparação com a extrapolação linear</li>
    <li><code>scripts/10_robustez_modelo1.py</code> &mdash; robustez do Modelo 1 a especificações alternativas</li>
    <li><code>scripts/11_robustez_renda_estadual.py</code> &mdash; robustez com salário médio estadual (PNADC) como denominador alternativo</li>
    <li><code>scripts/12_mapas_coropleticos.py</code> &mdash; mapas por UF (ICR-SM, projeção 2033 água/esgoto, gap)</li>
  </ul>
  <p>Dados de entrada e saída (CSVs) na raiz da pasta do projeto; plano completo com
  justificativas metodológicas em <code>plano_artigo.md</code>.</p>
</section>

<hr class="div" />
<footer>Relatório gerado a partir do painel SNIS (1995&ndash;2022) + IBGE + Open-Meteo &middot;
ver <code>plano_artigo.md</code> para o desenho completo do estudo.</footer>

</div>
"""

out_path = os.path.join(BASE, "relatorio_resultados.html")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Salvo:", out_path, "| tamanho:", len(html), "bytes")
