"""
Grafico previsto vs observado no conjunto de teste (holdout 2017-2022), para
mostrar as previsoes de fato, nao so as metricas agregadas de MAE/RMSE.
Complementa a Tabela de validacao do modelo de ML com uma visualizacao das
previsoes individuais.

Entrada: holdout_predicoes_ml.csv
Saida: figuras/16_previsto_vs_observado.png
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

df = pd.read_csv(f"{BASE}\\holdout_predicoes_ml.csv")

TEXT = "#0b0b0b"
MUTE = "#52514e"
GRID = "#e3e2dc"
CAT0 = "#2a78d6"   # ML
CAT1 = "#eb6834"   # persistencia
LINE45 = "#9b9a91"

plt.rcParams.update({
    "font.size": 10, "text.color": TEXT, "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT, "xtick.color": MUTE, "ytick.color": MUTE,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
})

fig, axes = plt.subplots(1, 2, figsize=(11, 5.2))

# --------- painel 1: ML previsto vs observado ---------
ax = axes[0]
ax.scatter(df["observado"], df["previsto_ml"], s=6, alpha=0.15, color=CAT0, linewidths=0)
lims = [0, 100]
ax.plot(lims, lims, color=LINE45, linewidth=1.2, linestyle="--")
mae_ml = np.mean(np.abs(df["observado"] - df["previsto_ml"]))
ax.set_xlim(lims); ax.set_ylim(lims)
ax.set_xlabel("Observed water coverage (%)")
ax.set_ylabel("Predicted water coverage (%)")
ax.set_title(f"Gradient boosting\nMAE = {mae_ml:.2f} p.p., N = {len(df):,}", fontsize=11, fontweight="bold", loc="left")

# --------- painel 2: persistencia previsto vs observado ---------
ax = axes[1]
ax.scatter(df["observado"], df["previsto_persistencia"], s=6, alpha=0.15, color=CAT1, linewidths=0)
ax.plot(lims, lims, color=LINE45, linewidth=1.2, linestyle="--")
mae_p = np.mean(np.abs(df["observado"] - df["previsto_persistencia"]))
ax.set_xlim(lims); ax.set_ylim(lims)
ax.set_xlabel("Observed water coverage (%)")
ax.set_ylabel("Predicted water coverage (%)")
ax.set_title(f"Persistence baseline\nMAE = {mae_p:.2f} p.p., N = {len(df):,}", fontsize=11, fontweight="bold", loc="left")

fig.suptitle("One year ahead predictions on the holdout period, 2017 to 2022", fontsize=12, y=1.01)
fig.tight_layout()
fig.savefig(f"{FIG}\\16_previsto_vs_observado.png", dpi=150, bbox_inches="tight")
print("Salvo: 16_previsto_vs_observado.png")
print(f"MAE ML: {mae_ml:.3f}  MAE persistencia: {mae_p:.3f}")
