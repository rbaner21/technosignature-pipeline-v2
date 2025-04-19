#!/usr/bin/env python3
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import plotly.express as px
import os, pathlib

# locate project root & output folders
HERE     = pathlib.Path(__file__).parent
ROOT     = HERE.parent
OUT_DIR  = ROOT / "outputs"
REPORTS  = OUT_DIR / "reports"
TEMPLATE = HERE / "templates"

# 1) load top_candidates.csv from <repo>/outputs/
df = pd.read_csv(OUT_DIR / "top_candidates.csv")

# 2) configure Jinja2
env      = Environment(loader=FileSystemLoader(str(TEMPLATE)))
template = env.get_template("report.html")

# 3) ensure reports dir exists
os.makedirs(REPORTS, exist_ok=True)

# 4) render one HTML per candidate
for i, row in df.iterrows():
    fig      = px.scatter(df, x="best_period", y="max_power",
                          title="Transit Power vs. Period")
    plot_div = fig.to_html(full_html=False)
    html     = template.render(rank=i+1, data=row.to_dict(),
                               plot_div=plot_div)
    with open(REPORTS / f"report_{i+1}.html", "w") as f:
        f.write(html)
