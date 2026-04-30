import streamlit as st
import pandas as pd
import os
import sys
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from theme import apply_theme

apply_theme()

st.title("🛞 Race Strategy Explorer")

# Load laps
DATA_PATH = "data/processed"
files = [f for f in os.listdir(DATA_PATH) if "laps" in f]

latest_file = sorted(files)[-1]
df = pd.read_csv(os.path.join(DATA_PATH, latest_file))

# Tyre strategy
st.markdown("### 🛞 Tyre Usage")

fig = px.scatter(
    df,
    x="lap",
    y="driver",
    color="tyre",
    title="Tyre Strategy"
)

fig.update_layout(
    plot_bgcolor="#0B0B0B",
    paper_bgcolor="#0B0B0B",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)