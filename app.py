import streamlit as st
from utils import extract_text_from_pdf
from prompts import generate_summary_and_risks
import os

st.set_page_config(page_title="Compliance Risk Analyzer", layout="wide")
st.title("🛡️ Compliance Risk Analyzer using GenAI")

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.warning("Please set your OPENAI_API_KEY as an environment variable.")
    st.stop()

uploaded_file = st.file_uploader("📄 Upload a policy document (PDF)", type="pdf")

if uploaded_file:
    with st.spinner("🔍 Extracting content from PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        st.success("✅ Text extracted successfully!")
        st.subheader("📖 Document Preview")
        st.text_area("Preview", text[:2000] + "...", height=300)

    if st.button("🔍 Analyze Compliance Risks"):
        with st.spinner("🧠 Analyzing with GPT..."):
            summary, risks = generate_summary_and_risks(text, api_key)
            st.subheader("📝 Document Summary")
            st.write(summary)
            st.subheader("⚠️ Potential Compliance Risks")
            st.write(risks)
