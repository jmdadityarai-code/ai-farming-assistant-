from flask import Flask, render_template, request
from weather import get_weather  # assume get_weather function proper hai

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    advice = None
    chat_response = None  # Chatbot reply

    if request.method == "POST":
        city = request.form.get("city")
        user_msg = request.form.get("message")

        if city:
            weather = get_weather(city)

            if weather:
                if weather["temp"] > 30:
                    advice = "🌱 Irrigation needed"
                else:
                    advice = "💧 No irrigation needed"

        if user_msg:
            if "water" in user_msg.lower():
                chat_response = advice
            else:
                chat_response = "🤖 I can help with farming advice!"

    return render_template(
        "index.html",
        weather=weather,
        advice=advice,
        chat_response=chat_response
    )

if __name__ == "__main__":
    app.run(debug=True, port=5051)  # 5051 ya koi bhi free port
    @app.route("/", methods=["GET", "POST"])
def home():
    return "OK TEST"