from flask import Flask, render_template, request

app = Flask(__name__)

cadetinfo = {
    "Abhinav Pathak": ["TUE2", "WED1", "FRI1", "SAT2"],
    "Sri Karan M": ["MON1", "TUE2", "FRI1", "SAT2"],
    "Kura Sreevardhan Reddy": ["TUE1", "WED2", "THU1", "SAT2"],
    "Samahith M Rao": ["WED1", "THU2", "FRI1", "SAT2"],
    "Dhriti H Shetty": ["MON2", "TUE2", "WED1", "THU2"],
    "Aarushi R Jingade": ["MON2", "TUE1", "THU1", "SAT1"],
    "Ankita Agarwal": ["TUE1", "WED2", "THU1", "FRI2"],
    "Aryaman Sharma": ["TUE2", "WED1", "THU2", "FRI1"]
}


@app.route("/", methods=["GET", "POST"])
def home():

    freecadets = []

    if request.method == "POST":

        day = request.form["day"]
        half = request.form["half"]

        required = day.upper() + half

        for cadet, availability in cadetinfo.items():
            if required in availability:
                freecadets.append(cadet)

    return render_template("index.html", freecadets=freecadets)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)