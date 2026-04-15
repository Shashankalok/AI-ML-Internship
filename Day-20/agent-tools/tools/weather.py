from langchain.tools import tool
import requests

@tool
def get_weather(city: str) -> str:
    """
    Get current weather for a given city (no API key required).
    """
    try:
        url = f"https://wttr.in/{city}?format=j1"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=5)

        # Debug check
        if response.status_code != 200:
            return f"Error: Unable to fetch data (Status {response.status_code})"

        data = response.json()

        current = data["current_condition"][0]
        temp = current["temp_C"]
        weather = current["weatherDesc"][0]["value"]

        return f"Weather in {city}: {temp}°C, {weather}"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"