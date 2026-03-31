import requests

def get_weather(city):
    try:
        # 🌍 Step 1: Get coordinates from city name
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_res = requests.get(geo_url, timeout=5).json()

        if "results" not in geo_res:
            return {
                "city": city,
                "temp": "N/A",
                "description": "City not found ❌"
            }

        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        # 🌤️ Step 2: Get weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url, timeout=5).json()

        print("DEBUG:", weather_res)  # optional (logs me dikhega)

        current = weather_res.get("current_weather")

        if not current:
            return {
                "city": city,
                "temp": "N/A",
                "description": "Weather not available ⚠️"
            }

        temp = current.get("temperature")

        # 🌱 Simple irrigation logic
        if temp is not None:
            if temp > 30:
                advice = "💧 Irrigation recommended (Hot weather)"
            elif temp < 10:
                advice = "❄️ No irrigation needed (Cold weather)"
            else:
                advice = "🌿 Moderate conditions, irrigation optional"
        else:
            advice = "⚠️ No advice available"

        return {
            "city": city,
            "temp": temp,
            "description": "Live weather 🌤️",
            "advice": advice
        }

    except Exception as e:
        print("ERROR:", e)
        return {
            "city": city,
            "temp": "Error",
            "description": "Something went wrong ❌",
            "advice": "⚠️ Try again later"
        }