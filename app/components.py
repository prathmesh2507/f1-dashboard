import streamlit as st

def metric_card(title, value):
    st.markdown(f"""
        <div class="card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)


def section(title):
    st.markdown(f"## {title}")


def glow_text(text):
    st.markdown(f"""
        <h2 style='color:#E10600; text-shadow: 0 0 10px #E10600;'>{text}</h2>
    """, unsafe_allow_html=True)