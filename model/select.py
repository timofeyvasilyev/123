import sqlite3

def get_studentss() -> list:
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    rows = cursor.fetchall()
    conn.close()
    print(rows)
    return rows
