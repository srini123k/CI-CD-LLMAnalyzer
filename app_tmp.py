import streamlit as st
import os
from dotenv import load_dotenv
from gitlab_utils import fetch_failed_jobs, fetch_job_log
from llm_utils import analyze_log_with_llm

# --- Load Environment or Streamlit Secrets ---
load_dotenv()

openai_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
gitlab_token = st.secrets.get("GITLAB_TOKEN") or os.getenv("GITLAB_TOKEN")
project_id = st.secrets.get("PROJECT_ID") or os.getenv("PROJECT_ID")

# --- Streamlit Config ---
st.set_page_config(page_title="AI-Powered CI/CD Log Analyzer", layout="wide")
st.title("🚀 LLM-powered CI/CD Log Debugger & Optimizer")
st.caption("Auto-fetch failed GitLab jobs → analyze logs → suggest fixes via LLMs.")

# --- UI ---
st.sidebar.header("⚙️ Configuration")
limit = st.sidebar.slider("Number of failed jobs to analyze:", 1, 10, 3)

if not openai_key or not gitlab_token or not project_id:
    st.error("Missing required configuration. Please set in .env or Streamlit Secrets.")
    st.stop()

if st.button("🔍 Fetch & Analyze Failed Jobs"):
    with st.spinner("Fetching failed jobs from GitLab..."):
        failed_jobs = fetch_failed_jobs(project_id, gitlab_token, limit)

    if not failed_jobs:
        st.info("✅ No failed jobs found. Everything looks good!")
    else:
        for job in failed_jobs:
            st.markdown(f"### 🔧 Job: `{job['name']}` (ID: {job['id']})")
            st.write(f"Status: {job['status']} | Stage: {job['stage']} | Ref: {job['ref']}")
            
            log_data = fetch_job_log(project_id, job['id'], gitlab_token)
            if log_data:
                with st.spinner(f"Analyzing job {job['id']} with AI..."):
                    ai_result = analyze_log_with_llm(log_data, openai_key)
                st.markdown("#### 🤖 AI Analysis:")
                st.write(ai_result)

                with st.expander("📜 View Log"):
                    st.code(log_data[:4000])
            st.divider()

st.sidebar.info("Secrets securely loaded from Streamlit or .env file.")
st.sidebar.caption("Built with ❤️ using Streamlit, GitLab API, and OpenAI GPT models.")
