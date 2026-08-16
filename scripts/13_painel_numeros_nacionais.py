"""
Painel de numeros nacionais do setor de agua/esgoto no Brasil, no estilo da
Figura 2 de Fagundes, Marques & Malheiros (2025) -- um resumo visual do
contexto do painel antes de entrar nas equacoes (Secao 3.1 do artigo).

Usa 2021 como ano de referencia porque 2022 nao tem cobertura de agua
reportada na extracao do SNIS usada neste estudo (variavel ausente para
todos os municipios naquele ano).

Entrada: br_painel_analise_final.csv
Saida: figuras/14_painel_numeros_nacionais.png
"""
import pandas as pd
import matplotlib.pyplot as plt

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

df = pd.read_csv(f"{BASE}\\br_painel_analise_final.csv")
ANO_REF = 2021
sub = df[df["ano"] == ANO_REF]

stats = {
    "WATER COVERAGE": f"{sub['indice_atendimento_urbano_agua'].mean():.1f}%",
    "SEWAGE COVERAGE": f"{sub['indice_coleta_esgoto'].mean():.1f}%",
    "BILLING LOSSES": f"{sub['indice_perda_faturamento'].mean():.1f}%",
    "AVG. RESIDENTIAL TARIFF": f"R$ {sub['tarifa_media_mensal_residencial'].mean():.0f}/month",
    "AVG. ICR-SM": f"{sub['ICR_SM'].mean():.1f}%",
    "POPULATION SERVED (WATER)": f"{sub['populacao_atendida_agua'].sum()/1e6:.0f} million",
}

TEXT = "#0b0b0b"
MUTE = "#52514e"
ACCENT = "#2a78d6"
BORDER = "#dbe1e3"

fig, ax = plt.subplots(figsize=(9, 4.2))
ax.set_xlim(0, 3)
ax.set_ylim(0, 2)
ax.axis("off")

positions = [(0, 1), (1, 1), (2, 1), (0, 0), (1, 0), (2, 0)]
for (col, row), (label, value) in zip(positions, stats.items()):
    x, y = col, row
    ax.add_patch(plt.Rectangle((x + 0.03, y + 0.05), 0.94, 0.9, fill=False,
                                 edgecolor=BORDER, linewidth=1))
    ax.text(x + 0.5, y + 0.62, value, ha="center", va="center",
            fontsize=17, fontweight="bold", color=ACCENT)
    ax.text(x + 0.5, y + 0.25, label, ha="center", va="center",
            fontsize=9, color=MUTE, wrap=True)

fig.suptitle(f"Brazilian water and sanitation panel, national averages ({ANO_REF})",
             fontsize=12, fontweight="bold", x=0.13, ha="left", y=0.98)
fig.text(0.13, 0.02, f"Source: authors' elaboration from the SNIS panel ({sub['id_municipio'].nunique()} municipalities, {ANO_REF}).",
          fontsize=8, color=MUTE)
fig.tight_layout(rect=[0, 0.05, 1, 0.93])
fig.savefig(f"{FIG}\\14_painel_numeros_nacionais.png", dpi=150)
print("Salvo: 14_painel_numeros_nacionais.png")
print(stats)
