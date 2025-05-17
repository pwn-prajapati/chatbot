import streamlit as st
from summarizer import generate_summary

st.set_page_config(page_title="Text Summarizer")

st.title("📝 Simple Text Summarizer")
st.markdown("Paste your long text below and click the button to summarize it.")

# Text input area
text_input = st.text_area("Your Text:", height=250)

# Summarize button
if st.button("Summarize"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text first.")
    else:
        summary = generate_summary(text_input)
        st.subheader("📌 Summary:")
        st.write(summary)
