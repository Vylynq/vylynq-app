import streamlit as st
from streamlit_extras.metric_cards import style_metric_cards

st.set_page_config(
    page_title="Vylynq Command Center",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark theme styles
st.markdown("""
    <style>
    body, .stApp {
        background-color: #0e0e0e;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
    .block-container {
        padding-top: 3rem;
    }
    h1, h2, h3 {
        color: #f5b5ff;
    }
    .stButton>button {
        background-color: #9f4eff;
        color: white;
        border-radius: 12px;
        padding: 0.5em 1.2em;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🧭 Navigate")
st.sidebar.success("Choose your ritual zone:")

st.title("✨ VYLYNQ — Your Command Center")
st.markdown("""
Welcome to your **Safe Space**, **Hype Space**, and **Power Space**.  
Track rituals. Store your truth. Run your world.

💬 *“Damn. That’s Me.”*
""")
