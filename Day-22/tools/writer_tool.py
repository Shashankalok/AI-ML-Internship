from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME
import time

client = Groq(api_key=GROQ_API_KEY)


def generate_report(state):
    """
    Generates a professional report using LLM.
    Includes:
    - Input truncation (token control)
    - Retry mechanism (rate limit handling)
    """

    # Truncate inputs to avoid token overflow
    query = state.get("query", "")
    research = state.get("research", "")[:300]
    analysis = state.get("analysis", "")[:800]
    critique = state.get("critique", "")[:500]

    prompt = f"""
    Create a professional and well-structured report.

    Query:
    {query}

    Research Summary:
    {research}

    Analysis:
    {analysis}

    Critique Insights:
    {critique}

    Format the report with:
    - Title
    - Introduction
    - Key Insights
    - Challenges
    - Recommendations
    - Conclusion

    Keep it clear, concise, and professional.
    """

    # Retry mechanism for rate limits
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,  # from settings.py
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional report writer."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f" Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                time.sleep(3)  # wait before retry
            else:
                return "Error: Unable to generate report due to API limits."