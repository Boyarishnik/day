from flask import Flask, render_template, url_for, request, redirect
from config import Config
from database import FlaskDatabase, get_db

# Инициализация веб-приложения
app = Flask("__main__")
app.config.from_object(Config)

# Определение меню навигации
menu = {
    "Главная": "/",
    "Участвовать": "/register",
    "Участники": "/members",
    "Подробнее": "https://www.earthhour.org/"
}

# Обработчик маршрута для главной страницы
@app.route("/")
def main():
    return render_template("main.html", menu=menu)

# Обработчик маршрута для страницы регистрации
@app.route("/register", methods=["POST", "GET"])
def register():
    # Инициализация базы данных
    db = FlaskDatabase(get_db(app))
    
    # Обработка POST-запроса для регистрации нового участника
    if request.method == "POST" and request.form["member_name"] not in db.get_members():
        # Добавление нового участника в базу данных
        db += request.form["member_name"]
        print(request.form["member_name"])  # Вывод имени участника в консоль
        return redirect("/members")  # Перенаправление на страницу участников
    
    # Отображение страницы регистрации
    return render_template("register.html", menu=menu)

# Обработчик маршрута для страницы участников
@app.route("/members")
def members():
    # Инициализация базы данных
    db = FlaskDatabase(get_db(app))
    
    # Отображение страницы участников с данными из базы
    return render_template("members.html", menu=menu, db=db)

# Запуск приложения, если этот файл выполняется как основной
if __name__ == "__main__":
    app.run(debug=True)