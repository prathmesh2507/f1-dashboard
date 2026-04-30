import streamlit as st
import pandas as pd
import os
import sys
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from theme import apply_theme

apply_theme()

st.title("📈 Team War Room")

# Load results
DATA_PATH = "data/processed"
files = [f for f in os.listdir(DATA_PATH) if "results" in f]

latest_file = sorted(files)[-1]
df = pd.read_csv(os.path.join(DATA_PATH, latest_file))

# Team points
team_points = df.groupby("team")["points"].sum().reset_index()

# Chart
fig = px.bar(
    team_points,
    x="team",
    y="points",
    color="team",
    title="Team Performance"
)

fig.update_layout(
    plot_bgcolor="#0B0B0B",
    paper_bgcolor="#0B0B0B",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)