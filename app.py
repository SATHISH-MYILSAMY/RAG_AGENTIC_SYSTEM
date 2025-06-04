import streamlit as st
import os
from dotenv import load_dotenv
from agent import ask_agent

load_dotenv()

st.set_page_config(page_title="RAG Agentic System", layout="wide")
st.title("📚 RAG Agentic LLM System")

query = st.text_area("Enter your query or question:", height=150, placeholder="e.g. Summarize recent federal regulations on energy...")

if st.button("Ask Agent"):
    if not query.strip():
        st.warning("⚠️ Please enter a valid query.")
    else:
        with st.spinner("🤖 Agent is processing your request..."):
            try:
                response = ask_agent(query)
                st.markdown("### 🧠 Agent Response:")
                st.write(response)
            except Exception as e:
                st.error(f"❌ Agent failed to respond: `{str(e)}`")


