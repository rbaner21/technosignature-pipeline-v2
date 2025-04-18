#!/usr/bin/env python3
"""
Generate HTML reports for each candidate using Jinja2.
"""
import pandas as pd
from jinja2 import Environment, FileSystemLoader
import plotly.express as px
import os

# 1. Load candidates
df = pd.read_csv('../outputs/top_candidates.csv')

# 2. Setup Jinja2
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('report.html')

# 3. Ensure output folder exists
os.makedirs('../outputs/reports', exist_ok=True)

# 4. Generate one report per candidate
for i, row in df.iterrows():
    fig = px.scatter(df, x='best_period', y='max_power', title='Transit Power vs. Period')
    plot_div = fig.to_html(full_html=False)
    html = template.render(rank=i+1, data=row.to_dict(), plot_div=plot_div)
    with open(f'../outputs/reports/report_{i+1}.html', 'w') as f:
        f.write(html)
