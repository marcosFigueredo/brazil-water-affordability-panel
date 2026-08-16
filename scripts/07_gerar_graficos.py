"""
Gera os graficos (PNG) dos resultados descritivos, do modelo de painel e da
projecao 2033, usando a paleta validada da skill dataviz.

Entrada: br_painel_icr_sm.csv, descritiva_icr_*.csv, resultados_modelo_painel.txt
         (coeficientes reproduzidos aqui manualmente a partir do script 05),
         br_projecao_cobertura_2033*.csv
Saida: figuras/*.png
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

# paleta validada (skill dataviz, references/palette.md)
CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#4a3aa7"]
STATUS = {"on_track": "#0ca30c", "at_risk": "#fab219", "will_not_meet": "#d03b3b"}
TEXT = "#0b0b0b"
TEXT_MUTED = "#52514e"
GRID = "#e3e2dc"

plt.rcParams.update({
    "font.size": 11, "text.color": TEXT, "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT, "xtick.color": TEXT_MUTED, "ytick.color": TEXT_MUTED,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
})

REGIOES_ORDEM = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
PORTE_ORDEM = ["<5 mil", "5-20 mil", "20-50 mil", "50-100 mil", "100-500 mil", "500 mil+"]

# =====================================================================
# FIGURA 1 — trajetoria nacional do ICR_SM, 1995-2022
# =====================================================================
por_ano = pd.read_csv(f"{BASE}\\descritiva_icr_por_ano.csv")
fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(por_ano["ano"], por_ano["median"], color=CAT[0], linewidth=2.5, label="Mediana")
ax.fill_between(por_ano["ano"], por_ano["median"], color=CAT[0], alpha=0.08)
ax.axhline(5, color=STATUS["will_not_meet"], linewidth=1.2, linestyle="--", alpha=0.7)
ax.text(1995.3, 5.3, "banda internacional 3-5% (World Bank/ONU)", fontsize=9, color=TEXT_MUTED)
ax.axhline(3, color=STATUS["will_not_meet"], linewidth=1.2, linestyle="--", alpha=0.7)
ax.set_title("ICR-SM mediano no Brasil, 1995-2022", fontsize=13, fontweight="bold", loc="left")
ax.set_ylabel("ICR-SM (% do salário mínimo)")
ax.set_xlabel("Ano")
ax.yaxis.set_major_formatter(mticker.FormatStrFormatter("%.0f%%"))
fig.tight_layout()
fig.savefig(f"{FIG}\\01_trajetoria_nacional_icr.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 2 — ICR_SM por regiao (media do periodo)
# =====================================================================
por_regiao = pd.read_csv(f"{BASE}\\descritiva_icr_por_regiao.csv").set_index("regiao").loc[REGIOES_ORDEM]
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(por_regiao.index, por_regiao["median"], color=CAT[:5], width=0.6)
for b, v in zip(bars, por_regiao["median"]):
    ax.text(b.get_x() + b.get_width()/2, v + 0.1, f"{v:.1f}%", ha="center", fontsize=10, color=TEXT)
ax.set_title("ICR-SM mediano por região, 1995-2022 (média do período)", fontsize=13, fontweight="bold", loc="left")
ax.set_ylabel("ICR-SM (% do salário mínimo)")
fig.tight_layout()
fig.savefig(f"{FIG}\\02_icr_por_regiao.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 3 — ICR_SM por porte de municipio
# =====================================================================
por_porte = pd.read_csv(f"{BASE}\\descritiva_icr_por_porte.csv").set_index("porte").loc[PORTE_ORDEM]
fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(por_porte.index, por_porte["median"], color=CAT[0], width=0.6)
for b, v in zip(bars, por_porte["median"]):
    ax.text(b.get_x() + b.get_width()/2, v + 0.15, f"{v:.1f}%", ha="center", fontsize=10, color=TEXT)
ax.set_title("ICR-SM mediano por porte de município (média do período)", fontsize=13, fontweight="bold", loc="left")
ax.set_ylabel("ICR-SM (% do salário mínimo)")
plt.setp(ax.get_xticklabels(), rotation=20, ha="right")
fig.tight_layout()
fig.savefig(f"{FIG}\\03_icr_por_porte.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 4 — coeficientes do Modelo 1 (H1+H2), com IC 95%
# =====================================================================
modelo1 = pd.DataFrame({
    "variavel": ["Investimento per capita\n(defasado)", "Instabilidade do\ninvestimento (CV, defasado)",
                 "% Financiamento\noneroso (defasado)", "Perdas de\nfaturamento (defasado)"],
    "coef": [-2.339e-05 * 1000, -0.0154, 0.0345, -0.0012 * 100],  # escalas ajustadas p/ leitura visual
    "erro": [3.87e-05 * 1000, 0.0262, 0.0357, 0.0009 * 100],
    "p": [0.5456, 0.5571, 0.3338, 0.1984],
})
fig, ax = plt.subplots(figsize=(8, 5))
cores = [STATUS["will_not_meet"] if p < 0.05 else "#b5b4ad" for p in modelo1["p"]]
y = np.arange(len(modelo1))
ax.errorbar(modelo1["coef"], y, xerr=1.96 * modelo1["erro"], fmt="o", color=TEXT, ecolor="#b5b4ad",
            elinewidth=2, capsize=4, markersize=7)
for i, c in enumerate(cores):
    ax.scatter(modelo1["coef"][i], y[i], color=c, s=90, zorder=5)
ax.axvline(0, color=TEXT_MUTED, linewidth=1)
ax.set_yticks(y)
ax.set_yticklabels(modelo1["variavel"])
ax.set_xlabel("Coeficiente (IC 95%) — nenhum estatisticamente significativo (p>0,19)")
ax.set_title("Modelo 1 (H1+H2): planejamento defasado → ICR-SM\nNenhuma variável significativa — achado nulo", fontsize=12, fontweight="bold", loc="left")
fig.tight_layout()
fig.savefig(f"{FIG}\\04_coeficientes_modelo1_h1h2.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 5 — R² between vs within (achado central)
# valores reais do Modelo 1 (linearmodels PanelOLS): R2.between=0.8492, R2.within=-0.0128
# plotados sem gambiarra: eixo aceita negativo, a barra "within" fica no lugar certo
# (achatada, ligeiramente abaixo de zero), nao inflada para "aparecer".
# =====================================================================
fig, ax = plt.subplots(figsize=(7, 5))
labels = ["Between\n(entre municípios)", "Within\n(dentro do mesmo\nmunicípio ao longo do tempo)"]
valores_real = [0.8492, -0.0128]
bars = ax.bar(labels, valores_real, color=[CAT[0], "#b5b4ad"], width=0.5)
ax.text(0, 0.8492 + 0.03, "R² = 0,85", ha="center", fontsize=12, fontweight="bold", color=TEXT)
ax.text(1, -0.0128 - 0.05, "R² = −0,01\n(estatisticamente zero)", ha="center", fontsize=11, color=TEXT)
ax.axhline(0, color=TEXT_MUTED, linewidth=1)
ax.set_ylim(-0.15, 1)
ax.set_ylabel("R² do Modelo 1 (ICR-SM)")
ax.set_title("Achado central: affordability é estrutural, não gerencial",
              fontsize=12, fontweight="bold", loc="left")
ax.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=1))
fig.tight_layout()
fig.savefig(f"{FIG}\\05_r2_between_within.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 6 — projecao 2033 (agua) por regiao, barras empilhadas
# =====================================================================
proj = pd.read_csv(f"{BASE}\\br_projecao_cobertura_2033.csv")
tab = pd.crosstab(proj["regiao"], proj["classificacao_2033"], normalize="index") * 100
tab = tab.reindex(REGIOES_ORDEM)[["on_track", "at_risk", "will_not_meet"]]

fig, ax = plt.subplots(figsize=(9, 5.5))
left = np.zeros(len(tab))
for col in ["on_track", "at_risk", "will_not_meet"]:
    vals = tab[col].values
    ax.barh(tab.index, vals, left=left, color=STATUS[col], label=col.replace("_", " "), height=0.6)
    for i, (v, l) in enumerate(zip(vals, left)):
        if v > 4:
            ax.text(l + v/2, i, f"{v:.0f}%", ha="center", va="center", fontsize=9,
                     color="white" if col != "at_risk" else TEXT)
    left += vals
ax.set_xlim(0, 100)
ax.set_xlabel("% dos municípios da região")
ax.set_title("Projeção de cobertura de água até 2033, por região\n(meta legal: 99% — Lei 14.026/2020)",
              fontsize=12, fontweight="bold", loc="left")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=3, frameon=False)
fig.tight_layout()
fig.savefig(f"{FIG}\\06_projecao_2033_agua_regiao.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 7 — projecao 2033 agua vs esgoto, comparativo por regiao
# =====================================================================
proj_esg = pd.read_csv(f"{BASE}\\br_projecao_cobertura_2033_esgoto.csv")
wnm_agua = (proj.groupby("regiao")["classificacao_2033"]
            .apply(lambda s: (s == "will_not_meet").mean() * 100).reindex(REGIOES_ORDEM))
wnm_esgoto = (proj_esg.groupby("regiao")["classificacao_2033_esgoto"]
              .apply(lambda s: (s == "will_not_meet").mean() * 100).reindex(REGIOES_ORDEM))

fig, ax = plt.subplots(figsize=(9, 5.8))
x = np.arange(len(REGIOES_ORDEM))
w = 0.35
ax.bar(x - w/2, wnm_agua.values, width=w, color=CAT[0], label="Água (meta 99%)")
ax.bar(x + w/2, wnm_esgoto.values, width=w, color=CAT[1], label="Esgoto (meta 90%)")
for i, v in enumerate(wnm_agua.values):
    ax.text(i - w/2, v + 1.2, f"{v:.0f}%", ha="center", fontsize=9)
for i, v in enumerate(wnm_esgoto.values):
    ax.text(i + w/2, v + 1.2, f"{v:.0f}%", ha="center", fontsize=9)
ax.set_xticks(x)
ax.set_xticklabels(REGIOES_ORDEM)
ax.set_ylim(0, max(wnm_agua.max(), wnm_esgoto.max()) * 1.22)
ax.set_ylabel("% de municípios 'will not meet' a meta 2033")
ax.set_title("Água vs. esgoto: trajetórias desacopladas até a meta 2033",
              fontsize=12, fontweight="bold", loc="left")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=2, frameon=False)
fig.tight_layout()
fig.savefig(f"{FIG}\\07_agua_vs_esgoto_2033.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 8 — validacao 1-passo-a-frente: ML vs persistencia vs linear
# =====================================================================
val = pd.read_csv(f"{BASE}\\validacao_ml_vs_linear.csv")
fig, ax = plt.subplots(figsize=(8, 5))
cores8 = [CAT[0], STATUS["on_track"], CAT[1]]
bars = ax.barh(val["metodo"], val["MAE"], color=cores8, height=0.55)
for b, v in zip(bars, val["MAE"]):
    ax.text(v + 0.1, b.get_y() + b.get_height()/2, f"{v:.2f} p.p.", va="center", fontsize=10)
ax.set_xlabel("Erro absoluto médio (p.p. de cobertura), teste 2017-2022")
ax.set_title("Validação 1 ano à frente: o modelo de ML NÃO supera\no baseline ingênuo (repetir o último valor)",
              fontsize=12, fontweight="bold", loc="left")
fig.tight_layout()
fig.savefig(f"{FIG}\\08_validacao_ml_vs_baselines.png", dpi=150)
plt.close(fig)

# =====================================================================
# FIGURA 9 — comparacao classificacao 2033: linear vs ML
# =====================================================================
comp = pd.read_csv(f"{BASE}\\comparacao_metodos_2033.csv")
tab_lin = comp["classificacao_2033"].value_counts(normalize=True).reindex(["on_track", "at_risk", "will_not_meet"]) * 100
tab_ml = comp["classificacao_2033_ml"].value_counts(normalize=True).reindex(["on_track", "at_risk", "will_not_meet"]) * 100

fig, ax = plt.subplots(figsize=(8, 5.5))
x = np.arange(3)
w = 0.35
labels9 = ["on track", "at risk", "will not meet"]
ax.bar(x - w/2, tab_lin.values, width=w, color=CAT[0], label="Extrapolação linear")
ax.bar(x + w/2, tab_ml.values, width=w, color=CAT[3], label="Gradient Boosting (ML)")
for i, v in enumerate(tab_lin.values):
    ax.text(i - w/2, v + 1.5, f"{v:.0f}%", ha="center", fontsize=9)
for i, v in enumerate(tab_ml.values):
    ax.text(i + w/2, v + 1.5, f"{v:.0f}%", ha="center", fontsize=9)
ax.set_xticks(x)
ax.set_xticklabels(labels9)
ax.set_ylim(0, max(tab_lin.max(), tab_ml.max()) * 1.25)
ax.set_ylabel("% dos municípios (N=5.431 comparáveis)")
ax.set_title("Os dois métodos discordam bastante:\nconcordância exata de apenas 33,6%",
              fontsize=12, fontweight="bold", loc="left")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.15), ncol=2, frameon=False)
fig.tight_layout()
fig.savefig(f"{FIG}\\09_comparacao_2033_linear_vs_ml.png", dpi=150)
plt.close(fig)

print("Graficos salvos em", FIG)
import os
for f in sorted(os.listdir(FIG)):
    print(" -", f)
