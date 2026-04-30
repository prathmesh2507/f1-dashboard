import streamlit as st
import pandas as pd
import os
import plotly.express as px

# -----------------------------
# 🎨 PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="F1 Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------
# ❌ REMOVE SIDEBAR
# -----------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🎨 GLOBAL STYLE
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #111 0%, #000 100%);
    color: white;
}

.header {
    background: linear-gradient(90deg, #0B0B0B, #1A1A1A);
    padding: 25px;
    border-bottom: 2px solid #E10600;
    box-shadow: 0 0 20px rgba(225, 6, 0, 0.4);
    border-radius: 10px;
}

.title {
    color: white;
    font-size: 36px;
    font-weight: 800;
}

.subtitle {
    color: #CCCCCC;
    font-size: 15px;
}

div[role="radiogroup"] {
    background: #111;
    padding: 10px;
    border-radius: 12px;
    display: flex;
    gap: 15px;
}

div[role="radio"] {
    background: #1A1A1A;
    padding: 10px 18px;
    border-radius: 8px;
    transition: 0.3s;
}

div[role="radio"]:hover {
    background: #E10600;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🔥 HEADER
# -----------------------------
st.markdown("""
<div class="header">
    <div class="title">🏎️ F1 Analytics Dashboard</div>
    <div class="subtitle">Real-time & Historical Formula 1 Insights</div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 🚀 HERO
# -----------------------------
st.markdown("""
<div style="
background: linear-gradient(90deg, #E10600, #8B0000);
padding: 20px;
border-radius: 12px;
margin-top: 15px;">
<h2 style="color:white;">🏁 Explore Formula 1 Like Never Before</h2>
<p style="color:white;">Dive into race data, driver performance, and strategy insights.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# 🧭 NAVIGATION
# -----------------------------
menu = ["🏠 Home", "🏁 Races", "👨‍🏎️ Drivers & Teams", "📊 Current Season"]
choice = st.radio("", menu, horizontal=True)

# -----------------------------
# 📦 LOAD DATA
# -----------------------------
def load_season_data(year):
    path = "data/processed"
    all_results = []

    for file in os.listdir(path):
        if str(year) in file and "results" in file:
            df = pd.read_csv(f"{path}/{file}")
            all_results.append(df)

    if all_results:
        return pd.concat(all_results, ignore_index=True)
    return pd.DataFrame()


def load_race_data(year, gp):
    path = "data/processed"

    results_file = f"{path}/clean_{year}_{gp}_results.csv"
    laps_file = f"{path}/clean_{year}_{gp}_laps.csv"

    if not os.path.exists(results_file):
        return None, None

    results = pd.read_csv(results_file)
    laps = pd.read_csv(laps_file)

    return results, laps


# -----------------------------
# 🏠 HOME PAGE
# -----------------------------
if choice == "🏠 Home":

    st.title("🏁 Season Overview")

    # Year dropdown
    years = sorted(list(set([f.split("_")[1] for f in os.listdir("data/processed") if "results" in f])))
    selected_year = st.selectbox("Select Season", years)

    df = load_season_data(selected_year)

    if df.empty:
        st.warning("No data available.")
        st.stop()

    # -----------------------------
    # 📊 KPI CALCULATIONS
    # -----------------------------
    total_races = df["driver"].count()

    standings = df.groupby("driver")["points"].sum().sort_values(ascending=False).reset_index()

    champion = standings.iloc[0]["driver"]
    top_team = df.groupby("team")["points"].sum().idxmax()
    total_drivers = df["driver"].nunique()

    # -----------------------------
    # 🎴 CARDS
    # -----------------------------
    col1, col2, col3, col4 = st.columns(4)

    def card(title, value):
        st.markdown(f"""
        <div style="
        background:#1A1A1A;
        padding:20px;
        border-radius:12px;
        text-align:center;
        box-shadow:0 0 15px rgba(225,6,0,0.3);">
        <h4 style="color:#AAAAAA;">{title}</h4>
        <h2 style="color:white;">{value}</h2>
        </div>
        """, unsafe_allow_html=True)

    with col1:
        card("Total Entries", total_races)

    with col2:
        card("Champion", champion)

    with col3:
        card("Top Team", top_team)

    with col4:
        card("Drivers", total_drivers)

    st.markdown("---")

    # -----------------------------
    # 🏆 TABLE
    # -----------------------------
    st.subheader("🏆 Driver Standings")

    st.dataframe(standings, use_container_width=True)

    # -----------------------------
    # 📊 CHART
    # -----------------------------
    fig = px.bar(
        standings.head(10),
        x="driver",
        y="points",
        title="Top 10 Drivers",
        color="points",
        color_continuous_scale="reds"
    )

    fig.update_layout(
        plot_bgcolor="#111",
        paper_bgcolor="#111",
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# OTHER PAGES (PLACEHOLDER)
# -----------------------------
elif choice == "🏁 Races":

    st.title("🏁 Race Explorer")

    # -----------------------------
    # 📅 YEAR SELECTION
    # -----------------------------
    files = os.listdir("data/processed")

    years = sorted(list(set([f.split("_")[1] for f in files if "results" in f])))
    selected_year = st.selectbox("Select Season", years)

    # -----------------------------
    # 🏁 GP LIST
    # -----------------------------
    gps = sorted([
        "_".join(f.split("_")[2:-1]).replace("_results.csv", "")
        for f in files
        if f.startswith(f"clean_{selected_year}") and "results" in f
    ])

    selected_gp = st.selectbox("Select Grand Prix", gps)

    # -----------------------------
    # 📦 LOAD DATA
    # -----------------------------
    results, laps = load_race_data(selected_year, selected_gp)

    if results is None:
        st.warning("Race data not available.")
        st.stop()

    # -----------------------------
    # 🏆 RACE RESULTS
    # -----------------------------
    st.subheader(f"🏆 {selected_gp} Results")

    results_sorted = results.sort_values("position")

    st.dataframe(results_sorted.head(10), use_container_width=True)

    # -----------------------------
    # 📊 LAP TIME ANALYSIS
    # -----------------------------
    st.subheader("⏱️ Lap Time Analysis")

    top_drivers = results_sorted.head(5)["driver"].tolist()

    lap_subset = laps[laps["driver"].isin(top_drivers)]

    fig_lap = px.line(
        lap_subset,
        x="lap",
        y="lap_time",
        color="driver",
        title="Lap Time Trend (Top 5 Drivers)"
    )

    fig_lap.update_layout(
        plot_bgcolor="#111",
        paper_bgcolor="#111",
        font_color="white"
    )

    st.plotly_chart(fig_lap, use_container_width=True)

    # -----------------------------
    # 🛞 TYRE STRATEGY
    # -----------------------------
    st.subheader("🛞 Tyre Strategy")

    tyre_data = laps.groupby(["driver", "tyre"]).size().reset_index(name="laps")

    fig_tyre = px.bar(
        tyre_data,
        x="driver",
        y="laps",
        color="tyre",
        title="Tyre Usage"
    )

    fig_tyre.update_layout(
        plot_bgcolor="#111",
        paper_bgcolor="#111",
        font_color="white"
    )

    st.plotly_chart(fig_tyre, use_container_width=True)

elif choice == "👨‍🏎️ Drivers & Teams":
    st.title("👨‍🏎️ Drivers & Constructors")

elif choice == "📊 Current Season":
    st.title("📊 Current Season")