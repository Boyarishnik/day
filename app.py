from flask import Flask, render_template, url_for, request, redirect
from config import Config
from database import FlaskDatabase

app = Flask("__main__")
app.config.from_object(Config)

menu = {"Главная": "/",
        "Участвовать": "/register",
        "Участники": "/members",
        "asd": "/asdasdasda"}


@app.route("/")
def main():
    return render_template("main.html", menu=menu)

@app.route("/register", methods=["POST", "GET"])
def register():
    db = FlaskDatabase(get_db())
    if request.method == "POST" and request.form["username"] not in map(lambda a: a["name"], users):
        db.user = (request.form["username"], request.form["password"])
        return redirect(url_for("members"))
    return render_template("signup.html", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
