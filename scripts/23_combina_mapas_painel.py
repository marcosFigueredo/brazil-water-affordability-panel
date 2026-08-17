"""
Combina os 4 mapas coropleticos por UF ja existentes (ICR-SM historico,
projecao 2033 agua, projecao 2033 esgoto, gap esgoto-agua) em uma unica
figura de 4 paineis, para uso no manuscrito Elsevier condensado, que
precisa economizar espaco/figuras sem perder as evidencias visuais.

Entrada: figuras/10_mapa_icr_sm_uf.png, 11_mapa_2033_agua_uf.png,
         12_mapa_2033_esgoto_uf.png, 13_mapa_gap_agua_esgoto_uf.png
Saida: figuras/21_paineis_mapas_uf.png
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

paineis = [
    ("a", "10_mapa_icr_sm_uf.png"),
    ("b", "11_mapa_2033_agua_uf.png"),
    ("c", "12_mapa_2033_esgoto_uf.png"),
    ("d", "13_mapa_gap_agua_esgoto_uf.png"),
]

fig, axes = plt.subplots(2, 2, figsize=(11, 11.5))
for ax, (letra, fname) in zip(axes.flat, paineis):
    img = mpimg.imread(f"{FIG}\\{fname}")
    ax.imshow(img)
    ax.axis("off")
    ax.text(0.0, 1.02, f"({letra})", transform=ax.transAxes, fontsize=15,
             fontweight="bold", color="#0b0b0b", va="bottom", ha="left")

fig.subplots_adjust(wspace=0.02, hspace=0.08, left=0.01, right=0.99, top=0.96, bottom=0.01)
fig.savefig(f"{FIG}\\21_paineis_mapas_uf.png", dpi=300, bbox_inches="tight")
print("Salvo: 21_paineis_mapas_uf.png")
