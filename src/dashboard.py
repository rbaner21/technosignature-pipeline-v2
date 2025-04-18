#!/usr/bin/env python3
"""
Simple Dash dashboard for top candidates.
"""
import dash
from dash import dash_table, html
import pandas as pd

# 1. Load data
df = pd.read_csv('../outputs/top_candidates.csv')

# 2. Initialize app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Top Technosignature Candidates"),
    dash_table.DataTable(
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=20
    )
])

# 3. Run server
if __name__ == "__main__":
    app.run_server(port=8050)

