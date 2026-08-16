"""
Series temporais (medias nacionais anuais) das variaveis que alimentam o modelo
de gradient boosting (Secao 3.7 do artigo), para ilustrar visualmente como os
dados de entrada se comportam ao longo do tempo antes de qualquer tratamento
especifico do modelo (defasagem, missing handling, encoding categorico).

Entrada: br_painel_analise_final.csv
Saida: figuras/15_series_temporais_ml.png
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")

CAT0 = "#2a78d6"
TEXT = "#0b0b0b"
MUTE = "#52514e"
GRID = "#e3e2dc"

plt.rcParams.update({
    "font.size": 9, "text.color": TEXT, "axes.edgecolor": GRID,
    "axes.labelcolor": TEXT, "xtick.color": MUTE, "ytick.color": MUTE,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white",
})

# ordem fixa (a)-(f), sem titulo/subtitulo embutido na imagem -- a explicacao de
# cada painel e o periodo comum vao no \caption do LaTeX, nao na propria figura
series = [
    ("a", "indice_atendimento_urbano_agua"),
    ("b", "investimento_percapita"),
    ("c", "prop_financiamento_oneroso"),
    ("d", "indice_perda_faturamento"),
    ("e", "crescimento_populacional_pct_aa"),
    ("f", "crescimento_va_servicos_pct_aa"),
]

fig, axes = plt.subplots(2, 3, figsize=(13, 7.2))
for ax, (letra, col) in zip(axes.flat, series):
    # media, nao mediana: prop_financiamento_oneroso tem massa em zero (a maioria dos
    # municipios nao usa financiamento oneroso em um dado ano), entao a mediana fica
    # degenerada em 0 mesmo havendo variacao real capturada pela media
    yearly = df.groupby("ano")[col].mean()
    n_obs = df.groupby("ano")[col].apply(lambda s: s.notna().sum())
    valid_years = n_obs[n_obs >= 30].index
    yearly = yearly.loc[valid_years]
    ax.plot(yearly.index, yearly.values, color=CAT0, linewidth=2.0)
    ax.fill_between(yearly.index, yearly.values, color=CAT0, alpha=0.08)
    ax.axvline(2016, color=MUTE, linewidth=0.9, linestyle="--", alpha=0.6)
    ax.text(0.03, 0.92, f"({letra})", transform=ax.transAxes, fontsize=13,
             fontweight="bold", color=TEXT, va="top", ha="left")
    ax.set_xticklabels([])
    ax.tick_params(axis="x", length=0)
    ax.tick_params(axis="y", labelsize=9)

fig.tight_layout()
fig.savefig(f"{FIG}\\15_series_temporais_ml.png", dpi=300)
print("Salvo: 15_series_temporais_ml.png (300 dpi)")
