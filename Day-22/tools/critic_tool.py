from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def evaluate_text(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an expert reviewer. Evaluate the quality of the analysis and suggest improvements."
            },
            {
                "role": "user",
                "content": f"Evaluate this analysis and suggest improvements:\n{text}"
            }
        ]
    )

    return response.choices[0].message.content