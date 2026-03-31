import requests

def get_weather(city):
    try:
        # Step 1: Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_res = requests.get(geo_url).json()

        if "results" not in geo_res:
            return {
                "city": city,
                "temp": "N/A",
                "description": "City not found ❌"
            }

        lat = geo_res["results"][0]["latitude"]
        lon = geo_res["results"][0]["longitude"]

        # Step 2: Get weather
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()

        print(weather_res)  # DEBUG

        # SAFE ACCESS
        current = weather_res.get("current_weather")

        if not current:
            return {
                "city": city,
                "temp": "N/A",
                "description": "Weather not available ⚠️"
            }

        return {
            "city": city,
            "temp": current.get("temperature"),
            "description": "Live weather 🌤️"
        }

    except Exception as e:
        print(e)
        return {
            "city": city,
            "temp": "Error",
            "description": "Something went wrong ❌"
        }
    