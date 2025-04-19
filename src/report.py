#!/usr/bin/env python3
"""
Generate HTML reports for each candidate using Jinja2.
"""
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import plotly.express as px
import os

# 1. Load the top‑20 list
df = pd.read_csv('outputs/top_candidates.csv')

# 2. Setup Jinja2 to use your existing template file (reports.html)
env = Environment(loader=FileSystemLoader('src/templates'))
template = env.get_template('reports.html')

# 3. Ensure output folder exists
os.makedirs('outputs/reports', exist_ok=True)

# 4. Loop over candidates
for i, row in df.iterrows():
    # bar chart of only this candidate’s techno_score
    cand = df.iloc[[i]]
    fig = px.bar(
        cand,
        x='pl_name',
        y='techno_score',
        title=f"Techno Score for {row['pl_name']}"
    )
    plot_div = fig.to_html(full_html=False)

    html = template.render(
        rank=i+1,
        data=row.to_dict(),
        plot_div=plot_div
    )
    outpath = f'outputs/reports/report_{i+1}.html'
    with open(outpath, 'w') as f:
        f.write(html)
    print(f"✅ Wrote {outpath}")
