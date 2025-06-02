import streamlit as st
st.set_page_config(page_title="Focus Zone", layout="centered")
import time
import json
import os
from datetime import datetime
import streamlit as st
try:
    st.set_page_config(page_title="Vylynq [Page Name]", layout="centered")
except:
    pass  # Already set in root navigation

# ---------- CONFIG ----------


# ---------- FILE ----------
session_file = "focus_log.json"
if not os.path.exists(session_file):
    with open(session_file, "w") as f:
        json.dump({"sessions": 0}, f)

# ---------- STATE INIT ----------
if "is_running" not in st.session_state:
    st.session_state.is_running = False
if "paused" not in st.session_state:
    st.session_state.paused = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed" not in st.session_state:
    st.session_state.elapsed = 0
if "task" not in st.session_state:
    st.session_state.task = ""

# ---------- STYLE ----------
st.markdown("""
<style>
    .stButton>button {
        font-size: 18px;
        padding: 10px 24px;
        width: 100%;
    }
    input[type="text"] {
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("🔒 Focus Zone")
st.markdown("Zero distractions. One task. Pure execution.")

# ---------- USER INPUT ----------
if not st.session_state.is_running:
    st.session_state.task = st.text_input("🎯 What are you focusing on?", placeholder="e.g. Write pitch deck")
    focus_minutes = st.slider("⏱️ Focus Duration", 15, 60, 25)
    enable_sound = st.checkbox("🔔 Sound on complete", value=True)

# ---------- START SESSION ----------
if not st.session_state.is_running and st.button("🚀 Start Session"):
    if st.session_state.task.strip() != "":
        st.session_state.is_running = True
        st.session_state.start_time = time.time()
        st.session_state.duration = focus_minutes * 60
        st.session_state.elapsed = 0
        st.session_state.paused = False
    else:
        st.warning("Please enter a task to focus on.")

# ---------- TIMER ----------
if st.session_state.is_running:
    st.markdown(f"### 🎯 Focusing on: **{st.session_state.task}**")
    if not st.session_state.paused:
        current_time = time.time()
        st.session_state.elapsed = current_time - st.session_state.start_time
        remaining = st.session_state.duration - st.session_state.elapsed
    else:
        remaining = st.session_state.duration - st.session_state.elapsed

    mins, secs = divmod(int(remaining), 60)
    st.metric("🧠 Time Left", f"{mins:02}:{secs:02}")

    # Buttons
    col1, col2 = st.columns(2)
    if col1.button("⏸ Pause" if not st.session_state.paused else "▶ Resume"):
        if st.session_state.paused:
            st.session_state.start_time = time.time() - st.session_state.elapsed
            st.session_state.paused = False
        else:
            st.session_state.paused = True

    if col2.button("⏹ Stop"):
        st.session_state.is_running = False
        st.session_state.paused = False
        st.session_state.task = ""
        st.warning("⛔ Session cancelled.")

    # Countdown loop
    if remaining <= 0:
        st.session_state.is_running = False
        st.success("✅ Session complete!")
        with open(session_file, "r") as f:
            data = json.load(f)
        data["sessions"] += 1
        with open(session_file, "w") as f:
            json.dump(data, f)

        if enable_sound:
            st.markdown("""
                <audio autoplay>
                    <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" type="audio/ogg">
                </audio>
            """, unsafe_allow_html=True)
        st.balloons()

    # Refresh every second only if running and not paused
    if st.session_state.is_running and not st.session_state.paused:
        time.sleep(1)
        st.rerun()

# ---------- SESSION COUNTER ----------
with open(session_file, "r") as f:
    data = json.load(f)

st.markdown("---")
st.metric("🔥 Focus Sessions Completed", data["sessions"])
st.info("Use this after your daily rituals in Habit Tracker to go beast mode.")
