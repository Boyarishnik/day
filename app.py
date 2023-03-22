from flask import Flask, render_template, url_for, request, redirect
from config import Config
from database import FlaskDatabase, get_db

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
    db = FlaskDatabase(get_db(app))
    if request.method == "POST" and member not in db.get_members():
        db.user = (request.form["username"], request.form["password"])
        return redirect(url_for("members"))
    return render_template("register.html", menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
