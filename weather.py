import requests

def get_weather(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_res = requests.get(url).json()

    if "results" not in geo_res:
        return {"city": city, "temp": "Not found", "description": "City not found ❌"}

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_res = requests.get(weather_url).json()

    # ✅ correct key
    temp = weather_res["current_weather"]["temperature"]

    return {
        "city": city,
        "temp": temp,
        "description": "Live weather 🌤️"
    }
    