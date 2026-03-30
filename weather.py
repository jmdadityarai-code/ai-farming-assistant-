import requests

def get_weather(city):
    # Step 1: Get latitude & longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        return None

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Step 2: Get weather
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_res = requests.get(weather_url).json()

    temp = weather_res["current_weather"]["temperature"]

    return {
        "city": city,
        "temp": temp,
        "description": "Live weather data"
    }