from groq import Groq
import os
import json

client = Groq(api_key=os.getenv('GROQ_API_KEY'))

PROMPT_TEMPLATE = """
You are a senior network engineer. Given the following detected anomalies (as JSON), produce:
1) Short root-cause explanation (2-3 sentences)
2) A prioritized list of recommended CLI commands and checks
3) A brief note about likely impact

Anomalies JSON:
{anomalies}
"""


def summarize_anomalies(anomalies):
    if not anomalies:
        return "No anomalies to summarize."

    content = PROMPT_TEMPLATE.format(anomalies=json.dumps(anomalies, indent=2))

    resp = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{'role': 'user', 'content': content}],
        temperature=0.2,
    )

    return resp.choices[0].message.content