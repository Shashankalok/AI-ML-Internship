from groq import Groq
from config.settings import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


def summarize_text(text):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[
            {"role": "system", "content": "You are a helpful AI that summarizes text clearly and concisely."},
            {"role": "user", "content": f"Summarize this:\n{text}"}
        ]
    )

    return response.choices[0].message.content