import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 HER Dashboard")
st.markdown("See your metrics, magic, and momentum.")

# 📊 Mock Habit Data
habit_data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Habits Completed": [2, 3, 4, 2, 5, 3, 4]
}

df_habits = pd.DataFrame(habit_data)

# 📈 Mock Mood Data
mood_data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Mood Score": [6.5, 7.0, 7.8, 6.9, 8.2, 7.5, 7.9]
}

df_mood = pd.DataFrame(mood_data)

# Show Bar Chart
st.subheader("🔥 Ritual Consistency")
bar_fig = px.bar(df_habits, x="Day", y="Habits Completed", color="Habits Completed", height=300)
st.plotly_chart(bar_fig, use_container_width=True)

# Show Line Chart
st.subheader("💫 Mood Tracker")
line_fig = px.line(df_mood, x="Day", y="Mood Score", markers=True, height=300)
st.plotly_chart(line_fig, use_container_width=True)

st.caption("✨ You're not just tracking. You're evolving.")
