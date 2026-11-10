import logging

import streamlit as st
from summarizer import summarize_text

logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered"
)

st.title("AI Text Summarizer")

st.write("Paste your text below and generate an AI-powered summary.")
user_text=st.text_area("Enter your Text", height=250, placeholder="Paste your article or paragraph here...")

length = st.selectbox(
    "Choose Summary Length",
    options=["Short", "Medium", "Long"])

if st.button("Generate Summary"):
     if not user_text.strip():
          st.warning("Please enter some text to summarize.")
     else:
          with st.spinner("Generating summary..."):
               try:
                    logger.info("Generating summary for the provided text.")
                    summary = summarize_text(length, user_text)
                    st.subheader("Summary:")
                    st.write(summary)
               except Exception as e:
                    logger.exception("Failed to generate text summary")
                    st.error(f"An error occurred while generating the summary: {e}")
          