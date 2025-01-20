import sqlite3
from datetime import datetime
from fileinput import close

from pyexpat.errors import messages


def database_connection():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    return connection, cursor

def create_table():
    connection, cursor = database_connection()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        data_added TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        message TEXT
    )""")
    connection.commit()
    connection.close()

def add_user(user_id, username):
    connection, cursor = database_connection()
    cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (id, username, data_added) VALUES (?, ?, datetime('now'))",
                         (user_id, username, datetime.now()))
        connection.commit()
    connection.close()

def log_message(user_id, message):
    connection, cursor = database_connection()
    cursor.execute("INSERT INTO messages (id, message) VALUES (?, ?)",
                         (user_id, message))
    connection.commit()
    connection.close()









































