from flask import Flask, render_template, url_for, request, redirect
from config import Config
from database import FlaskDatabase, get_db

app = Flask("__main__")
app.config.from_object(Config)

menu = {"Главная": "/",
        "Участвовать": "/register",
        "Участники": "/members",
        "Подробнее": "https://www.earthhour.org/"}


@app.route("/")
def main():
    return render_template("main.html", menu=menu)


@app.route("/register", methods=["POST", "GET"])
def register():
    db = FlaskDatabase(get_db(app))
    if request.method == "POST" and request.form["member_name"] not in db.get_members():
        db += request.form["member_name"]
        print(request.form["member_name"])
        return redirect("/members")
    return render_template("register.html", menu=menu)


@app.route("/members")
def members():
    db = FlaskDatabase(get_db(app))
    return render_template("members.html", menu=menu, db=db)


if __name__ == "__main__":
    app.run(debug=True)
