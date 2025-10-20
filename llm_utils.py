from openai import OpenAI

def analyze_log_with_llm(log_text, openai_key):
    """Analyze CI/CD log using LLM and return summarized insights"""
    client = OpenAI(api_key=openai_key)

    prompt = f"""
You are an expert DevOps assistant. Analyze the following CI/CD job log and respond with:
1. Root cause of failure (in plain English)
2. Suggested fix
3. Preventive measure to avoid recurrence

Log:
{log_text[:3500]}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
