@app.route("/", methods=["GET", "POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form.get("city")
        print("CITY:", city)

        # 🔥 TEST DATA (force)
        weather = {
            "city": city,
            "temp": "25°C",
            "description": "Test Weather",
            "advice": "Test Advice"
        }

    return render_template("index.html", weather=weather)