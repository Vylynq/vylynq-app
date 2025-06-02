import streamlit as st
import random

quotes = [
    "“She remembered who she was. And the game changed.”",
    "“You’re not healing quietly anymore.”",
    "“Ritual locked. Momentum activated.”"
]

st.title("💪 Ritual Tracker")
habit = st.text_input("🔖 Name your ritual")

if st.button("💥 Lock It In"):
    st.success(f"Ritual ‘{habit}’ locked in. Keep the streak alive 🔥")
    st.markdown(f"💬 *{random.choice(quotes)}*")
