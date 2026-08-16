"""
Mapas coropleticos por UF, inspirados nas Figuras 3-9 de Fagundes, Marques &
Malheiros (2025) -- eles mapeiam affordability/cobertura geograficamente; nos
tinhamos so graficos de barra por regiao. Este script fecha essa lacuna visual.

Entrada: dados_brutos_externos/malha_uf.geojson (contornos IBGE, baixado via API),
         br_painel_icr_sm.csv, br_projecao_cobertura_2033.csv,
         br_projecao_cobertura_2033_esgoto.csv
Saida: figuras/10_mapa_icr_sm_uf.png, 11_mapa_2033_agua_uf.png,
       12_mapa_2033_esgoto_uf.png, 13_mapa_gap_agua_esgoto_uf.png
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

# ============ carrega malha geografica ============
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
print(f"Malha carregada: {len(gdf)} UFs")

# paleta sequencial validada (skill dataviz) -- azul, claro->escuro
CMAP_SEQ = mcolors.LinearSegmentedColormap.from_list("seq_blue", ["#eaf2fb", "#2a78d6", "#0d2f52"])
CMAP_DIV = mcolors.LinearSegmentedColormap.from_list("div", ["#1baf7a", "#f5f5f0", "#d03b3b"])
TEXT = "#0b0b0b"

def plota_mapa(gdf_merged, coluna, fname, cmap=CMAP_SEQ, vmin=None, vmax=None):
    # sem titulo embutido na imagem -- o titulo/legenda da figura fica no
    # \caption do LaTeX, nao na propria imagem, para consistencia de idioma
    # e para nao duplicar informacao entre imagem e legenda academica
    fig, ax = plt.subplots(figsize=(8, 7.5))
    gdf_merged.plot(column=coluna, cmap=cmap, linewidth=0.6, edgecolor="white",
                     legend=True, ax=ax, vmin=vmin, vmax=vmax,
                     missing_kwds={"color": "#d9d9d9", "label": "No data"},
                     legend_kwds={"shrink": 0.6, "label": ""})
    for _, row in gdf_merged.iterrows():
        if pd.notna(row[coluna]):
            c = row["geometry"].representative_point()
            ax.annotate(row["sigla_uf"], (c.x, c.y), fontsize=7, ha="center", color=TEXT, alpha=0.85)
    ax.set_axis_off()
    fig.tight_layout()
    fig.savefig(f"{FIG}\\{fname}", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print("Salvo:", fname)

# ============ Mapa 1: ICR-SM medio por UF ============
icr = pd.read_csv(f"{BASE}\\br_painel_icr_sm.csv")
icr_uf = icr.groupby("sigla_uf")["ICR_SM"].mean().reset_index()
g1 = gdf.merge(icr_uf, on="sigla_uf", how="left")
plota_mapa(g1, "ICR_SM", "10_mapa_icr_sm_uf.png")

# ============ Mapa 2: % will_not_meet agua 2033 por UF ============
proj_agua = pd.read_csv(f"{BASE}\\br_projecao_cobertura_2033.csv")
wnm_agua_uf = proj_agua.groupby("sigla_uf")["classificacao_2033"].apply(
    lambda s: (s == "will_not_meet").mean() * 100
).reset_index(name="pct_will_not_meet")
g2 = gdf.merge(wnm_agua_uf, on="sigla_uf", how="left")
plota_mapa(g2, "pct_will_not_meet", "11_mapa_2033_agua_uf.png", vmin=0, vmax=100)

# ============ Mapa 3: % will_not_meet esgoto 2033 por UF ============
proj_esg = pd.read_csv(f"{BASE}\\br_projecao_cobertura_2033_esgoto.csv")
wnm_esg_uf = proj_esg.groupby("sigla_uf")["classificacao_2033_esgoto"].apply(
    lambda s: (s == "will_not_meet").mean() * 100
).reset_index(name="pct_will_not_meet_esgoto")
g3 = gdf.merge(wnm_esg_uf, on="sigla_uf", how="left")
plota_mapa(g3, "pct_will_not_meet_esgoto", "12_mapa_2033_esgoto_uf.png", vmin=0, vmax=100)

# ============ Mapa 4: gap esgoto-agua (evidencia de desacoplamento) ============
gap = wnm_agua_uf.merge(wnm_esg_uf, on="sigla_uf", how="outer")
gap["gap_esgoto_menos_agua"] = gap["pct_will_not_meet_esgoto"] - gap["pct_will_not_meet"]
g4 = gdf.merge(gap, on="sigla_uf", how="left")
plota_mapa(g4, "gap_esgoto_menos_agua", "13_mapa_gap_agua_esgoto_uf.png",
           cmap=CMAP_DIV, vmin=-40, vmax=40)

print("\nTodos os mapas gerados em", FIG)
