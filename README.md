#  Compliance Risk Analyzer using GenAI

This GenAI-powered tool analyzes compliance-related documents such as GDPR or HIPAA and identifies potential risks, missing clauses, and provides a summary using OpenAI's GPT-4.

---

##  Features

-  Upload PDF policy or legal documents
-  GPT-4-based summarization and risk detection
-  Highlights missing or weak regulatory clauses
-  Simple Streamlit interface

---

##  Tech Stack

- Python 3.10+
- Streamlit (for UI)
- OpenAI GPT-4 API (LLM engine)
- pdfplumber (for extracting PDF text)
- LangChain (optional for RAG)
- FAISS (optional for advanced retrieval)

---

##  Project Structure

---

##  Setup Instructions

```bash
git clone https://github.com/heyme-1212/genai-compliance-risk-analyzer.git
cd genai-compliance-risk-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
export OPENAI_API_KEY=your-api-key



