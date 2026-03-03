import pandas as pd
import geopandas as gpd
from bokeh.plotting import figure, curdoc
from bokeh.models import (GeoJSONDataSource, LinearColorMapper, ColorBar,
                          Slider, Select, HoverTool)
from bokeh.layouts import column, row
from bokeh.palettes import YlOrRd9
import json

# ── Load CSV ──────────────────────────────────────────────────────
df = pd.read_csv("data/covid-vaccination.csv")
df["date"] = pd.to_datetime(df["date"])
df["iso_code"] = df["iso_code"].str.strip().str.upper()

# Convert date to string to avoid JSON serialization error
df["date_str"] = df["date"].dt.strftime("%Y-%m-%d")

# ── Load GeoJSON ──────────────────────────────────────────────────
world = gpd.read_file("data/countries.geojson")
world = world.rename(columns={"ISO3166-1-Alpha-3": "iso_code", "name": "country_name"})
world["iso_code"] = world["iso_code"].str.strip().str.upper()
world = world[world["iso_code"] != "-99"].copy()

# ── Dates as strings ──────────────────────────────────────────────
date_strings = sorted(df["date_str"].unique())
print(f"Total dates: {len(date_strings)}")
print(f"First date: {date_strings[0]}")
print(f"Last date:  {date_strings[-1]}")

# ── Find best starting date (most countries have data) ───────────
date_counts = df.groupby("date_str")["iso_code"].count()
best_date = date_counts.idxmax()
print(f"Best date (most countries): {best_date} with {date_counts.max()} entries")

def get_geojson(selected_date_str, selected_country="All"):
    filtered = df[df["date_str"] == selected_date_str].copy()
    if selected_country != "All":
        filtered = filtered[filtered["country"] == selected_country]
    # Drop date columns before merge to avoid serialization issues
    filtered = filtered.drop(columns=["date"], errors="ignore")
    merged = world.merge(filtered, on="iso_code", how="left")
    merged["ratio"] = merged["ratio"].fillna(0)
    merged["country"] = merged["country"].fillna(merged["country_name"])
    merged["ratio_str"] = merged["ratio"].apply(lambda x: f"{x:.1f}%")
    merged["people_vaccinated"] = merged["people_vaccinated"].fillna(0).astype(int)
    merged["total_vaccinations"] = merged["total_vaccinations"].fillna(0).astype(int)
    merged["New_deaths"] = merged["New_deaths"].fillna(0).astype(int)
    # Drop any remaining non-serializable columns
    for col in merged.columns:
        if merged[col].dtype == "datetime64[ns]":
            merged = merged.drop(columns=[col])
    return json.loads(merged.to_json())

# ── Start from best date ──────────────────────────────────────────
start_index = date_strings.index(best_date)
geo_source = GeoJSONDataSource(geojson=json.dumps(get_geojson(best_date)))

palette = list(reversed(YlOrRd9))
mapper = LinearColorMapper(palette=palette, low=0, high=100, nan_color="#d3d3d3")

p = figure(
    title="COVID-19 Vaccination Rate by Country",
    height=520, width=950,
    toolbar_location="right",
    tools="pan,wheel_zoom,reset,save"
)

p.patches(
    "xs", "ys",
    source=geo_source,
    fill_color={"field": "ratio", "transform": mapper},
    line_color="white",
    line_width=0.4,
    fill_alpha=0.85
)

color_bar = ColorBar(
    color_mapper=mapper,
    label_standoff=10,
    title="% Vaccinated",
    location=(0, 0)
)
p.add_layout(color_bar, "right")

hover = HoverTool(tooltips=[
    ("Country",            "@country"),
    ("Vaccination Rate",   "@ratio_str"),
    ("People Vaccinated",  "@people_vaccinated{0,0}"),
    ("Total Vaccinations", "@total_vaccinations{0,0}"),
    ("New Deaths",         "@New_deaths{0,0}"),
])
p.add_tools(hover)

slider = Slider(
    start=0, end=len(date_strings) - 1,
    value=start_index, step=1,
    title=f"Date: {best_date}",
    width=750
)

countries = ["All"] + sorted(df["country"].dropna().unique().tolist())
country_select = Select(
    title="Filter by Country:",
    value="All",
    options=countries,
    width=220
)

def update(attr, old, new):
    selected_date    = date_strings[slider.value]
    selected_country = country_select.value
    slider.title     = f"Date: {selected_date}"
    geo_source.geojson = json.dumps(get_geojson(selected_date, selected_country))

slider.on_change("value", update)
country_select.on_change("value", update)

layout = column(
    row(country_select),
    slider,
    p
)

curdoc().add_root(layout)
curdoc().title = "COVID-19 Vaccination Dashboard"
