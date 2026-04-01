from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    advice = None

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            data = get_weather(city)
            weather = data.get("temperature")
            advice = data.get("advice")

    return render_template("index.html", weather=weather, advice=advice)