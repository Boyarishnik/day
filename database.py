import sqlite3
from flask import g


def get_db(app):
    if not hasattr(g, "link_db"):
        g.link_db = connect_db(app)
    return g.link_db


def connect_db(app):
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


def create_db(app):
    """Вспомогательная функция для создания бд"""
    db = connect_db(app)
    with app.open_resource("sql_db.sql", mode="r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


class FlaskDatabase:

    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def __iadd__(self, member):
        try:
            self.__cur.execute(f"INSERT INTO members VALUES (NULL, ?)", (member,))
            self.__db.commit()
        except sqlite3.Error as e:
            print(f"error {e}")
            return False
        return True

    def __delitem__(self, key):
        try:
            self.__cur.execute(f"DELETE from mainmenu where id = {key}")
            self.__db.commit()
        except sqlite3.Error as e:
            print(f"error {e}")
            return False
        return True

if __name__ == "__main__":
    from app import app
    create_db(app)