import streamlit as st
import pandas as pd
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from theme import apply_theme

apply_theme()

st.markdown("""
<h1 style='text-align:center;'>🏎️ F1 RACE CONTROL ROOM</h1>
<p style='text-align:center; color:gray;'>Live Race Intelligence System</p>
""", unsafe_allow_html=True)

# Load latest data
DATA_PATH = "data/processed"
files = [f for f in os.listdir(DATA_PATH) if "results" in f]

latest_file = sorted(files)[-1]
df = pd.read_csv(os.path.join(DATA_PATH, latest_file))

# -----------------------------
# 🏁 HERO SECTION
# -----------------------------
winner = df.iloc[0]

st.markdown(f"""
<div style="
    background: linear-gradient(90deg, #E10600, #8B0000);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-bottom: 30px;
">
    <h2 style="color:white;">🏆 {winner['driver']}</h2>
    <p style="color:white;">Winner • {winner['team']}</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 📊 GRID STATS
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

def stat_box(title, value):
    st.markdown(f"""
    <div style="
        background:#111;
        padding:20px;
        border-radius:12px;
        border:1px solid #222;
        text-align:center;
    ">
        <div style="color:gray;">{title}</div>
        <div style="font-size:24px; font-weight:bold;">{value}</div>
    </div>
    """, unsafe_allow_html=True)

with col1:
    stat_box("Winner", winner['driver'])

with col2:
    stat_box("Team", winner['team'])

with col3:
    stat_box("Points", winner['points'])

with col4:
    stat_box("Grid Position", winner['grid_position'])

# -----------------------------
# 📋 TABLE
# -----------------------------
st.markdown("### 📊 Full Race Results")
st.dataframe(df, use_container_width=True)