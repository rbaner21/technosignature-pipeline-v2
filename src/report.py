#!/usr/bin/env python3
"""
Generate HTML reports for each candidate using Jinja2.
"""
import os
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import plotly.express as px

# 1. Compute key paths
script_dir   = os.path.dirname(os.path.abspath(__file__))           # src/
repo_dir     = os.path.abspath(os.path.join(script_dir, os.pardir)) # repo root
data_csv     = os.path.join(repo_dir, "outputs", "top_candidates.csv")
template_dir = os.path.join(script_dir, "templates")                # src/templates
output_dir   = os.path.join(repo_dir, "outputs", "reports")

# 2. Load top‐20 candidates
df = pd.read_csv(data_csv)

# 3. Set up Jinja2 environment pointing at src/templates
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template("report.html")

# 4. Make sure the reports folder exists
os.makedirs(output_dir, exist_ok=True)

# 5. Generate one HTML report per row
for idx, row in df.iterrows():
    # Example plot; feel free to swap in any per‐candidate figure
    fig = px.scatter(df, x="best_period", y="max_power", title="Transit Power vs. Period")
    plot_div = fig.to_html(full_html=False)

    html = template.render(
        rank     = idx + 1,
        data     = row.to_dict(),
        plot_div = plot_div
    )

    out_path = os.path.join(output_dir, f"report_{idx+1}.html")
    with open(out_path, "w") as f:
        f.write(html)

print(f"✅ Reports generated in {output_dir}/")
