from flask import Flask, render_template

app = Flask(__name__)

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine",  "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Fritz", "score": 80},
    {"name": "Sirius", "score": 75},
]


@app.route("/")
def home():
    return render_template("base.html", titulo="Ninja py")

@app.route("/resultado")
def resultado():
    context = {
        "titulo": "Resultados",
        "estudantes": students,
        "teste": test_name,
        "max_score": max_score
    }
    return render_template("results.html", **context)

if __name__ == "__main__":
    app.run(debug=True)