import streamlit as st

st.set_page_config(page_title="Vylynq Mobile", layout="centered")

# ----- Style -----
st.markdown("""
<style>
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #111;
    border-top: 1px solid #444;
    display: flex;
    justify-content: space-around;
    padding: 0.8rem 0;
    z-index: 1000;
}
.bottom-nav a {
    color: #aaa;
    text-decoration: none;
    font-size: 0.85rem;
    text-align: center;
}
.bottom-nav a:hover {
    color: white;
}
.bottom-nav .emoji {
    font-size: 1.5rem;
    display: block;
}
.block-container {
    padding-bottom: 80px;
}
</style>
""", unsafe_allow_html=True)

# ----- Routing -----
page = st.query_params.get("page", "dashboard")

# ----- Content Based on Page -----
if page == "dashboard":
    st.title("🏠 Vylynq Dashboard")
    st.info("This would normally show your XP, streaks, stats, etc.")
elif page == "habit":
    st.title("🎯 Habit Tracker")
    st.info("Redirect to your actual habit_tracker.py or replicate content.")
elif page == "focus":
    st.title("🧠 Focus Zone")
    st.info("Redirect or display content from focus_zone.py here.")

# ----- Bottom Nav -----
st.markdown("""
<div class='bottom-nav'>
    <a href='?page=dashboard'><span class='emoji'>🏠</span>Home</a>
    <a href='?page=habit'><span class='emoji'>🎯</span>Habits</a>
    <a href='?page=focus'><span class='emoji'>🧠</span>Focus</a>
</div>
""", unsafe_allow_html=True)
