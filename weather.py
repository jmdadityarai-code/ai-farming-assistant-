import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        res = requests.get(url).text

        # Example response: "London: +9°C"
        parts = res.split(":")
        if len(parts) < 2:
            return {
                "city": city,
                "temp": "N/A",
                "description": "Weather not found ❌",
                "advice": "⚠️ Try again"
            }

        temp = parts[1].strip()

        return {
            "city": city,
            "temp": temp,
            "description": "Live weather 🌤️",
            "advice": "🌿 Farming conditions normal"
        }

    except Exception as e:
        print("ERROR:", e)
        return {
            "city": city,
            "temp": "N/A",
            "description": "Error fetching weather ❌",
            "advice": "⚠️ Try again"
        }