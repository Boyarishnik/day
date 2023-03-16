from flask import Flask, render_template


app = Flask("__main__")


@app.route("/")
def main():
    return render_template("main.html")


app.run(debug=True)
