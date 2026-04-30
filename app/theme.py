import streamlit as st

def apply_theme():
    st.markdown("""
    <style>

    /* 🔥 GLOBAL */
    .stApp {
        background: linear-gradient(135deg, #0B0B0B, #111111);
        color: #FFFFFF;
        font-family: 'Segoe UI', sans-serif;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: #0F0F0F;
        border-right: 1px solid #222;
    }

    /* TITLES */
    h1 {
        color: #E10600;
        font-size: 42px;
        font-weight: 700;
    }

    h2, h3 {
        color: #FF2A2A;
    }

    /* 🔥 GLASS CARDS */
    .card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 8px 32px rgba(0,0,0,0.6);
        transition: 0.3s;
    }

    .card:hover {
        transform: scale(1.02);
        border: 1px solid #E10600;
    }

    /* METRICS */
    .metric-title {
        font-size: 14px;
        color: #aaa;
    }

    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #FFFFFF;
    }

    /* BUTTON */
    .stButton>button {
        background: linear-gradient(45deg, #E10600, #ff3c3c);
        border: none;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
    }

    .stButton>button:hover {
        transform: scale(1.05);
    }

/* REMOVE DEFAULT PADDING */
.block-container {
    padding-top: 1rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

</style>
""", unsafe_allow_html=True)