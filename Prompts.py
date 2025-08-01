import openai

def generate_summary_and_risks(text, api_key):
    openai.api_key = api_key

    system_prompt = (
        "You are a compliance and legal policy expert. Analyze the document for missing clauses "
        "and summarize the content based on GDPR requirements like user consent, access control, "
        "data minimization, and breach notification."
    )

    user_prompt = f"""
Please analyze the following compliance policy:

{text[:3000]}

Tasks:
1. Provide a clear summary of the key points.
2. Highlight any missing, weak, or unclear compliance clauses.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3
    )

    result = response.choices[0].message.content

    # Attempt to split summary and risks
    if "2." in result:
        parts = result.split("2.")
        summary = parts[0].strip()
        risks = "2." + parts[1].strip()
    else:
        summary = result
        risks = "No distinct risk section found."

    return summary, risks
