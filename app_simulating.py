import streamlit as st
import time

st.set_page_config(page_title="LLM-powered CI/CD Log Debugger & Optimizer", layout="wide")

# ---- Simulated data ----
def fetch_failed_jobs(project_id, token, limit=3):
    """Simulated failed jobs for demo purposes"""
    return [
        {"id": 1, "name": "build-app", "status": "failed"},
        {"id": 2, "name": "run-tests", "status": "failed"},
        {"id": 3, "name": "deploy-staging", "status": "failed"},
    ]

def fetch_job_log(project_id, job_id, token):
    """Return sample logs for demonstration"""
    logs = {
        1: """Running with gitlab-runner 16.6.0 (1234abcd)
Using Docker image node:18.14.0
$ npm install
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR! peer react@"^17.0.0" from react-dom@17.0.2
ERROR: Job failed: exit code 1""",

        2: """=========================== test session starts ============================
test_user_login.py::test_login_invalid_user FAILED
AssertionError: Expected 401 Unauthorized but got 200 OK
ERROR: Job failed: exit code 1""",

        3: """$ aws s3 sync dist/ s3://myapp-staging
fatal error: An error occurred (AccessDenied)
ERROR: Job failed: exit code 1"""
    }
    return logs[job_id]


# ---- Simulated AI Analysis ----
def mock_llm_analysis(job_name, log_text):
    """Generate fake AI-like analysis results"""
    if "npm" in log_text:
        return {
            "summary": "Dependency conflict in Node.js build.",
            "root_cause": "React version mismatch between dependencies.",
            "recommendation": "Align React versions or use `--legacy-peer-deps` during npm install."
        }
    elif "AssertionError" in log_text:
        return {
            "summary": "Test failed in user login validation.",
            "root_cause": "Backend returned 200 instead of 401 for invalid credentials.",
            "recommendation": "Fix API response codes or update test expectations."
        }
    elif "AccessDenied" in log_text:
        return {
            "summary": "Deployment to S3 bucket failed.",
            "root_cause": "Insufficient IAM permissions for S3 PutObject operation.",
            "recommendation": "Update IAM role or S3 bucket policy with correct write access."
        }
    else:
        return {
            "summary": "Generic failure detected.",
            "root_cause": "Unclassified error.",
            "recommendation": "Review logs and retry."
        }


# ---- Streamlit UI ----
st.sidebar.title("⚙️ Configuration")
num_jobs = st.sidebar.slider("Number of failed jobs to analyze:", 1, 5, 3)
st.sidebar.info("🔒 Secrets securely loaded from Streamlit or .env file.\n\nBuilt with ❤️ using Streamlit, GitLab API, and OpenAI GPT models.")

st.title("🚀 LLM-powered CI/CD Log Debugger & Optimizer")
st.write("Auto-fetch failed GitLab jobs → analyze logs → suggest fixes via LLMs.")

if st.button("🔍 Fetch & Analyze Failed Jobs"):
    with st.spinner("Fetching failed jobs from GitLab..."):
        time.sleep(1)
        failed_jobs = fetch_failed_jobs(None, None, num_jobs)
    
    if not failed_jobs:
        st.success("✅ No failed jobs found. Everything looks good!")
    else:
        st.subheader("🧩 Analysis Results")
        for job in failed_jobs:
            log_text = fetch_job_log(None, job["id"], None)
            analysis = mock_llm_analysis(job["name"], log_text)

            with st.expander(f"💥 {job['name']} — {job['status'].upper()}"):
                st.code(log_text, language="bash")
                st.markdown(f"**🧠 Summary:** {analysis['summary']}")
                st.markdown(f"**🔍 Root Cause:** {analysis['root_cause']}")
                st.markdown(f"**💡 Recommendation:** {analysis['recommendation']}")
                st.divider()

st.markdown("---")
st.caption("Built for demo purposes — simulating GitLab + LLM integration for CI/CD optimization.")
