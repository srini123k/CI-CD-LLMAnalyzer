# CI-CD-LLMAnalyzer 🚀  
*AI-powered root cause analysis for CI/CD pipeline failures*

[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenAI](https://img.shields.io/badge/Powered%20by-OpenAI-ff69b4.svg)](https://openai.com)
[![GitLab](https://img.shields.io/badge/Integration-GitLab-orange.svg)](https://gitlab.com)
[![Slack](https://img.shields.io/badge/Notifications-Slack-4A154B?logo=slack)](https://slack.com)

---

## 🧭 Overview

**CI-CD-LLMAnalyzer** is an intelligent assistant designed to automatically analyze CI/CD job failures using Large Language Models (LLMs).  
It connects to your GitLab pipelines, fetches logs, and provides a human-readable summary of what went wrong — along with actionable fix recommendations.

> 💡 Think of it as an “AI teammate” that reads your logs, finds the root cause, and explains it instantly.

---

## ⚙️ Architecture

![Architecture Diagram](assets/architecture.png)

The system has four key components:

1️⃣ **GitLab CI/CD** → Generates build/test/deploy logs  
2️⃣ **Python Backend (FastAPI / Streamlit)** → Fetches logs via GitLab API  
3️⃣ **LLM Engine (e.g., GPT-4 / Claude / Local)** → Analyzes logs and produces concise summaries + fix suggestions  
4️⃣ **Notification Layer (Slack / Email / CLI)** → Sends results directly to engineers

---

## 🎯 Key Features

✅ Automatic log fetching from GitLab pipelines  
✅ LLM-based summarization of job failures  
✅ Fix recommendations with context awareness  
✅ Slack and email notifications for faster triage  
✅ Configurable thresholds and retry policies  
✅ Extensible backend (supports OpenAI, Anthropic, Azure, etc.)

---

## 🔍 Why This Project?

In large DevOps environments, engineers spend **hours** reading CI/CD logs.  
This project eliminates manual parsing by letting **AI perform root-cause analysis** — reducing **Mean Time To Resolution (MTTR)** and increasing productivity.

---

## ⚡ Example Workflow

1. A GitLab job fails  
2. CI-CD-LLMAnalyzer automatically pulls the log  
3. LLM analyzes and summarizes errors (e.g., “ImagePullBackOff: Invalid ECR credentials”)  
4. Sends summary + fix suggestion to Slack  
5. Developer acts immediately with context

---

## 🧩 Getting Started

### Prerequisites
- Python 3.9+
- GitLab Personal Access Token
- LLM API Key (e.g., OpenAI)
- (Optional) Slack webhook URL for notifications

### Installation
```bash
git clone https://github.com/srini123k/CI-CD-LLMAnalyzer.git
cd CI-CD-LLMAnalyzer
pip install -r requirements.txt

### Diagram


<img width="1024" height="1536" alt="Automated CI_CD Root Cause Analysis Diagram" src="https://github.com/user-attachments/assets/40ea6475-9084-4cba-a103-48a3b715f329" />


