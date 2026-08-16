"""
Grafico da trajetoria nacional media do ICR-SM (affordability), 1995-2022
observado, com os tres cenarios projetados ate 2033, extrapolacao linear por
municipio, forecast recursivo de gradient boosting e forecast recursivo de
random forest, para visualizar quao distintos os metodos ficam quando
aplicados a affordability (ao contrario de cobertura, aqui os metodos
discordam ate na direcao da tendencia, e o random forest fica entre os
outros dois).

Entrada: br_painel_analise_final.csv, br_projecao_icr_2033_linear.csv,
         br_projecao_icr_2033_ml.csv, br_projecao_icr_2033_rf.csv
Saida: figuras/19_projecao_icr_2033.png
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")
proj_lin = pd.read_csv(f"{BASE}\\br_projecao_icr_2033_linear.csv")
proj_ml = pd.read_csv(f"{BASE}\\br_projecao_icr_2033_ml.csv")
proj_rf = pd.read_csv(f"{BASE}\\br_projecao_icr_2033_rf.csv")

TEXT = "#0b0b0b"
MUTE = "#52514e"
GRID = "#e3e2dc"
CAT_OBS = "#0b0b0b"
CAT_LIN = "#2a78d6"
CAT_ML = "#eb6834"
CAT_RF = "#3f9142"

plt.rcParams.update({
    "font.size": 10, "text.color": TEXT, "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT, "xtick.color": MUTE, "ytick.color": MUTE,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
})

# ---------------- serie observada (media nacional anual, 1995-2022) ----------------
hist = df.groupby("ano")["ICR_SM"].mean().dropna()
n_obs_ano = df.groupby("ano")["ICR_SM"].apply(lambda s: s.notna().sum())
hist = hist.loc[n_obs_ano[n_obs_ano >= 30].index]
ultimo_ano_hist = hist.index.max()
nivel_2022 = hist.loc[ultimo_ano_hist]

# ---------------- cenarios GB e RF: media por ano, 2023-2033 (colunas ja existem no CSV) ----------------
anos_fut = [str(a) for a in range(2023, 2034)]

anos_fut_presentes = [a for a in anos_fut if a in proj_ml.columns]
media_ml_por_ano = proj_ml[anos_fut_presentes].mean()
serie_ml = pd.concat([pd.Series({str(ultimo_ano_hist): nivel_2022}), media_ml_por_ano])
serie_ml.index = serie_ml.index.astype(int)

anos_fut_presentes_rf = [a for a in anos_fut if a in proj_rf.columns]
media_rf_por_ano = proj_rf[anos_fut_presentes_rf].mean()
serie_rf = pd.concat([pd.Series({str(ultimo_ano_hist): nivel_2022}), media_rf_por_ano])
serie_rf.index = serie_rf.index.astype(int)

# ---------------- cenario linear: recomputa a trajetoria ano a ano por municipio ----------------
# (o CSV de extrapolacao linear so guarda o valor final em 2033; aqui refazemos o
# ajuste OLS por municipio, que e rapido, para obter a media nacional por ano)
def slope_intercept(grupo):
    g = grupo.dropna(subset=["ICR_SM"])
    if len(g) < 3:
        return None
    x = g["ano"].values.astype(float)
    y = g["ICR_SM"].values.astype(float)
    slope, intercept = np.polyfit(x, y, 1)
    return slope, intercept

ajustes = {}
for mun, g in df.groupby("id_municipio"):
    r = slope_intercept(g)
    if r is not None:
        ajustes[mun] = r

anos_proj = list(range(ultimo_ano_hist, 2034))
medias_lin = {}
for ano in anos_proj:
    vals = [np.clip(slope * ano + intercept, 0, 100) for slope, intercept in ajustes.values()]
    medias_lin[ano] = np.mean(vals)
serie_lin = pd.Series(medias_lin)

# ---------------- grafico ----------------
fig, ax = plt.subplots(figsize=(9, 5.5))

ax.plot(hist.index, hist.values, color=CAT_OBS, linewidth=2.0, label="Observed, 1995\u2013" + str(ultimo_ano_hist))
ax.plot(serie_lin.index, serie_lin.values, color=CAT_LIN, linewidth=2.0, linestyle="--", marker="o", markersize=3, label="Linear extrapolation per municipality")
ax.plot(serie_rf.index, serie_rf.values, color=CAT_RF, linewidth=2.0, linestyle="--", marker="o", markersize=3, label="Recursive random forest")
ax.plot(serie_ml.index, serie_ml.values, color=CAT_ML, linewidth=2.0, linestyle="--", marker="o", markersize=3, label="Recursive gradient boosting")

ax.axhline(5.0, color=MUTE, linewidth=0.9, linestyle=":", alpha=0.8)
ax.text(1996, 5.15, "Upper bound of international affordability range (5%)", fontsize=8, color=MUTE)

ax.axvline(ultimo_ano_hist, color=GRID, linewidth=1.2)

ax.set_xlabel("Year")
ax.set_ylabel("National average ICR-SM (%)")
ax.legend(loc="upper left", frameon=False, fontsize=9)
# eixo estendido um pouco alem de 2033 (ate 2034) so para dar respiro visual ao
# ultimo ponto projetado, que senao fica colado na borda direita do grafico
ax.set_xlim(1995, 2034)

fig.tight_layout()
fig.savefig(f"{FIG}\\19_projecao_icr_2033.png", dpi=300)
print("Salvo: 19_projecao_icr_2033.png")
print(f"\nNivel {ultimo_ano_hist}: {nivel_2022:.2f}%")
print(f"Projecao linear 2033: {serie_lin.loc[2033]:.2f}%")
print(f"Projecao random forest 2033: {serie_rf.loc[2033]:.2f}%")
print(f"Projecao gradient boosting 2033: {serie_ml.loc[2033]:.2f}%")
