import sqlite3

connection = sqlite3.connect("./db/users.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
password TEXT NOT NULL
)
""")
connection.commit()

def add_user(username, password):
    cursor.execute('INSERT INTO Users (username, password) VALUES (?, ?)', (username, password,))

def check_user(username):
    cursor.execute('SELECT id FROM Users WHERE username = ?', (username,))
    if cursor.fetchone():
        return True
    else: return False

def get_user_password(username):
    cursor.execute('SELECT password FROM Users WHERE username = ?', (username,))
    fetch = cursor.fetchone()
    if fetch:
        return fetch[0]
    else: return None

def close():
    connection.commit()
    connection.close()