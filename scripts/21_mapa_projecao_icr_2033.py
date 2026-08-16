"""
Mapa coropletico do ICR-SM (affordability) PROJETADO para 2033 por UF, no
mesmo estilo do mapa historico 1995-2022 (script 12), mas usando a media dos
tres metodos de projecao (extrapolacao linear, random forest recursivo,
gradient boosting recursivo) como estimativa central por estado, ja que o
artigo trata os tres como cenarios que balizam uma faixa de incerteza, nao
elege um "vencedor".

Entrada: dados_brutos_externos/malha_uf.geojson,
         br_projecao_icr_2033_linear.csv, br_projecao_icr_2033_rf.csv,
         br_projecao_icr_2033_ml.csv
Saida: figuras/20_mapa_projecao_icr_2033_uf.png
"""
import json
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from shapely.geometry import shape

BASE = r"G:\My Drive\UNEB\PPGMSB\MarcosProducaoCientifica\2026\specialIssues\UP"
FIG = f"{BASE}\\figuras"

codigo_para_sigla = {
    "11": "RO", "12": "AC", "13": "AM", "14": "RR", "15": "PA", "16": "AP", "17": "TO",
    "21": "MA", "22": "PI", "23": "CE", "24": "RN", "25": "PB", "26": "PE", "27": "AL",
    "28": "SE", "29": "BA", "31": "MG", "32": "ES", "33": "RJ", "35": "SP",
    "41": "PR", "42": "SC", "43": "RS", "50": "MS", "51": "MT", "52": "GO", "53": "DF",
}

with open(f"{BASE}\\dados_brutos_externos\\malha_uf.geojson", encoding="utf-8") as f:
    geo = json.load(f)

rows = []
for feat in geo["features"]:
    codarea = feat["properties"]["codarea"]
    sigla = codigo_para_sigla.get(codarea)
    if sigla is None:
        continue
    rows.append({"sigla_uf": sigla, "geometry": shape(feat["geometry"])})

gdf = gpd.GeoDataFrame(rows, crs="EPSG:4674")

CMAP_SEQ = mcolors.LinearSegmentedColormap.from_list("seq_blue", ["#eaf2fb", "#2a78d6", "#0d2f52"])
TEXT = "#0b0b0b"

lin = pd.read_csv(f"{BASE}\\br_projecao_icr_2033_linear.csv")
rf = pd.read_csv(f"{BASE}\\br_projecao_icr_2033_rf.csv")
gb = pd.read_csv(f"{BASE}\\br_projecao_icr_2033_ml.csv")

lin_uf = lin.groupby("sigla_uf")["projecao_icr_2033_linear"].mean()
rf_uf = rf.groupby("sigla_uf")["projecao_icr_2033_rf"].mean()
gb_uf = gb.groupby("sigla_uf")["projecao_icr_2033_ml"].mean()

comb = pd.concat([lin_uf, rf_uf, gb_uf], axis=1)
comb["media_3_metodos_2033"] = comb.mean(axis=1)
comb = comb.reset_index()

print(comb.round(2).sort_values("media_3_metodos_2033").to_string(index=False))

g = gdf.merge(comb[["sigla_uf", "media_3_metodos_2033"]], on="sigla_uf", how="left")

fig, ax = plt.subplots(figsize=(8, 7.5))
g.plot(column="media_3_metodos_2033", cmap=CMAP_SEQ, linewidth=0.6, edgecolor="white",
       legend=True, ax=ax, missing_kwds={"color": "#d9d9d9", "label": "No data"},
       legend_kwds={"shrink": 0.6, "label": ""})
for _, row in g.iterrows():
    if pd.notna(row["media_3_metodos_2033"]):
        c = row["geometry"].representative_point()
        ax.annotate(row["sigla_uf"], (c.x, c.y), fontsize=7, ha="center", color=TEXT, alpha=0.85)
ax.set_axis_off()
fig.tight_layout()
fig.savefig(f"{FIG}\\20_mapa_projecao_icr_2033_uf.png", dpi=300, bbox_inches="tight")
print("\nSalvo: 20_mapa_projecao_icr_2033_uf.png")
