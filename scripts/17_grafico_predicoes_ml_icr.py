"""
Grafico previsto vs observado no conjunto de teste (holdout 2017-2022) para o
modelo de ML que preve ICR-SM (affordability), espelhando o script 15 (que fez
o mesmo grafico para cobertura). Este e o segundo exercicio de forecasting,
agora sobre a variavel de affordability propriamente dita, nao sobre cobertura.

Entrada: holdout_predicoes_ml_icr.csv
Saida: figuras/18_previsto_vs_observado_icr.png
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

df = pd.read_csv(f"{BASE}\\holdout_predicoes_ml_icr.csv")

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

# limites com base no percentil 99 para nao esmagar o grafico com outliers raros
lim_max = float(np.nanpercentile(df[["observado", "previsto_ml", "previsto_persistencia"]].values, 99))
lims = [0, lim_max]

# --------- painel 1: ML previsto vs observado ---------
ax = axes[0]
ax.scatter(df["observado"], df["previsto_ml"], s=6, alpha=0.15, color=CAT0, linewidths=0)
ax.plot(lims, lims, color=LINE45, linewidth=1.2, linestyle="--")
mae_ml = np.mean(np.abs(df["observado"] - df["previsto_ml"]))
ax.set_xlim(lims); ax.set_ylim(lims)
ax.set_xlabel("Observed ICR-SM (%)")
ax.set_ylabel("Predicted ICR-SM (%)")
ax.set_title(f"Gradient boosting\nMAE = {mae_ml:.2f} p.p., N = {len(df):,}", fontsize=11, fontweight="bold", loc="left")

# --------- painel 2: persistencia previsto vs observado ---------
ax = axes[1]
ax.scatter(df["observado"], df["previsto_persistencia"], s=6, alpha=0.15, color=CAT1, linewidths=0)
ax.plot(lims, lims, color=LINE45, linewidth=1.2, linestyle="--")
mae_p = np.mean(np.abs(df["observado"] - df["previsto_persistencia"]))
ax.set_xlim(lims); ax.set_ylim(lims)
ax.set_xlabel("Observed ICR-SM (%)")
ax.set_ylabel("Predicted ICR-SM (%)")
ax.set_title(f"Persistence baseline\nMAE = {mae_p:.2f} p.p., N = {len(df):,}", fontsize=11, fontweight="bold", loc="left")

fig.suptitle("One year ahead ICR-SM predictions on the holdout period, 2017 to 2022", fontsize=12, y=1.01)
fig.tight_layout()
fig.savefig(f"{FIG}\\18_previsto_vs_observado_icr.png", dpi=300, bbox_inches="tight")
print("Salvo: 18_previsto_vs_observado_icr.png")
print(f"MAE ML: {mae_ml:.3f}  MAE persistencia: {mae_p:.3f}")
