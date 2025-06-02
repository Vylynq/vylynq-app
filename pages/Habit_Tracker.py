import streamlit as st
st.set_page_config(page_title="Vylynq Ritual Tracker", layout="centered")
from streamlit_lottie import st_lottie
import requests
import json
import os
import random
from datetime import date
import streamlit as st
try:
    st.set_page_config(page_title="Vylynq [Page Name]", layout="centered")
except:
    pass  # Already set in root navigation

# ------------- CONFIG -------------

today = str(date.today())

# ------------- STYLE (Mobile Optimized) -------------
st.markdown("""
<style>
input[type="text"], .stButton>button {
    font-size: 18px;
    padding: 12px 20px;
}
iframe {
    max-width: 100%;
}
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 2rem 1rem;
    }
    h1, h2, h3 {
        font-size: 1.3rem;
    }
    .stButton>button {
        width: 100%;
    }
}
</style>
""", unsafe_allow_html=True)

# ------------- FUNCTIONS -------------
reward_log_file = "reward_log.json"

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def has_played_sound_today():
    if os.path.exists(reward_log_file):
        with open(reward_log_file, "r") as f:
            data = json.load(f)
            return data.get("date") == today
    return False

def mark_sound_played():
    with open(reward_log_file, "w") as f:
        json.dump({"date": today}, f)

def load_data():
    if os.path.exists("rituals.json"):
        with open("rituals.json", "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open("rituals.json", "w") as f:
        json.dump(data, f, indent=2)

# ------------- INIT -------------
rituals = load_data()
confetti = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_u4yrau.json")

# ------------- QUOTES -------------
quotes = [
    "💼 Discipline? Nah. You just got tired of your own BS.",
    "🔥 You’re not lazy. You’re just too good at excuses.",
    "🎯 Another checkbox ticked. You dangerous beast.",
    "🚀 Routine? More like world domination on repeat.",
    "🧠 High performers don’t need motivation. They build rituals.",
    "😎 Most people quit by now. You're clearly not most people.",
    "📉 Your excuses are out of stock. Try again tomorrow.",
    "⚡ Another checkbox, another mic drop.",
    "🥷 You move in silence, like a productive ninja.",
]
st.markdown(f"<h4 style='color:#aaaaaa'>{random.choice(quotes)}</h4>", unsafe_allow_html=True)

# ------------- HEADER -------------
st.markdown("## 🎯 Ritual Tracker")
st.markdown("🚀 **Name your ritual**")
new_ritual = st.text_input("", placeholder="e.g. Workout")

if st.button("🔒 Lock It In"):
    if new_ritual.strip() != "":
        if new_ritual not in rituals:
            rituals[new_ritual] = {
                "streak": 0,
                "last_completed": "",
                "total_completed": 0
            }
            save_data(rituals)
            st.success(f"Ritual ‘{new_ritual}’ locked in. Let’s go.")
        else:
            st.info("Ritual already exists.")
    else:
        st.warning("Please enter a ritual name.")

# ------------- RITUAL CHECKLIST -------------
st.markdown("---")
st.subheader("✅ Today's Rituals")

all_checked = True
for ritual, info in rituals.items():
    if info["last_completed"] != today:
        checked = st.checkbox(f"{ritual}", key=ritual)
        if checked:
            rituals[ritual]["streak"] += 1
            rituals[ritual]["last_completed"] = today
            rituals[ritual]["total_completed"] += 1
            save_data(rituals)
            st.success(f"🔥 {ritual} done! Streak: {rituals[ritual]['streak']} days")
            st_lottie(confetti, height=200, key=f"confetti_{ritual}")
        else:
            all_checked = False
    else:
        st.markdown(f"✅ **{ritual}** – Already completed today")

# ------------- SOUND ON ALL COMPLETE -------------
if all_checked and len(rituals) > 0 and not has_played_sound_today():
    st.markdown("""
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/cartoon/clang_and_wobble.ogg" type="audio/ogg">
        </audio>
    """, unsafe_allow_html=True)
    st.markdown("### 🎉 Boss Level Achieved. All rituals done.")
    mark_sound_played()

# ------------- DASHBOARD OVERVIEW -------------
st.markdown("---")
st.subheader("📊 Ritual Dashboard")

total_rituals = len(rituals)
total_xp = sum(r["streak"] for r in rituals.values())
total_completed = sum(r["total_completed"] for r in rituals.values())
level = total_xp // 10 + 1

col1, col2, col3 = st.columns(3)
col1.metric("Rituals", total_rituals)
col2.metric("🔥 XP", total_xp)
col3.metric("✅ Completions", total_completed)

st.markdown("### 🎮 XP Progress")
st.progress(min((total_xp % 10) / 10, 1.0), text=f"Level {level}")

st.markdown("### 📅 Streak History")
for ritual, data in rituals.items():
    st.markdown(f"**{ritual}** – 🔁 {data['streak']} days | ✅ {data['total_completed']} completed")
