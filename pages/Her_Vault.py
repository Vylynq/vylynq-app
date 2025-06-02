import streamlit as st

st.title("🧠 Her Vault")

st.markdown("""
Your private space.  
Dump the thoughts.  
Save the quotes.  
Write the things no one else sees.
""")

entry = st.text_area("🔐 Speak your truth…")

if st.button("📥 Save Entry"):
    st.success("Sealed in the vault. No one’s looking — just you.")

st.caption("🔒 Encrypted. Empowered. Just how she likes it.")
