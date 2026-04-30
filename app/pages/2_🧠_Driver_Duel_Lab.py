import streamlit as st
import pandas as pd
import os
import sys
import plotly.express as px

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from theme import apply_theme

apply_theme()

st.title("🧠 Driver Duel Lab")

# Load latest lap data
DATA_PATH = "data/processed"
files = [f for f in os.listdir(DATA_PATH) if "laps" in f]

latest_file = sorted(files)[-1]
df = pd.read_csv(os.path.join(DATA_PATH, latest_file))

# Driver selection
drivers = df['driver'].unique()

col1, col2 = st.columns(2)

with col1:
    driver1 = st.selectbox("Select Driver 1", drivers)

with col2:
    driver2 = st.selectbox("Select Driver 2", drivers)

# Filter data
d1 = df[df['driver'] == driver1]
d2 = df[df['driver'] == driver2]

# -----------------------------
# 📊 COMPARISON METRICS
# -----------------------------
col1, col2 = st.columns(2)

def avg_time(df):
    return round(df['lap_time'].mean(), 2)

with col1:
    st.metric(driver1, f"{avg_time(d1)} sec")

with col2:
    st.metric(driver2, f"{avg_time(d2)} sec")

# -----------------------------
# 📈 LAP TIME GRAPH
# -----------------------------
st.markdown("### 📈 Lap Time Comparison")

fig = px.line(
    df[df['driver'].isin([driver1, driver2])],
    x="lap",
    y="lap_time",
    color="driver",
    title="Lap Time Comparison"
)

fig.update_layout(
    plot_bgcolor="#0B0B0B",
    paper_bgcolor="#0B0B0B",
    font=dict(color="white")
)

st.plotly_chart(fig, use_container_width=True)