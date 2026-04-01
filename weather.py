import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        res = requests.get(url, timeout=5).text

        if ":" not in res:
            return {
                "city": city,
                "temp": "N/A",
                "description": "Weather not available",
                "advice": "Try again later"
            }

        temp = res.split(":")[1].strip()

        return {
            "city": city,
            "temp": temp,
            "description": "Live weather",
            "advice": "Farming conditions normal"
        }

    except Exception as e:
        print("ERROR:", e)
        return {
            "city": city,
            "temp": "N/A",
            "description": "Error fetching weather",
            "advice": "Try again"
        }