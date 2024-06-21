import sqlite3


def create_db():
    # Подключение к базе данных (если файла базы данных не существует, он будет создан)
    conn = sqlite3.connect('db.db')

    # Создание объекта cursor для выполнения SQL-запросов
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name text NOT NULL,
        last_name TEXT NOT NULL,
        course TEXT NOT NULL,
        fac TEXT NOT NULL
    );
''')
    conn.commit()


    cursor.execute('''
    SELECT * FROM students''')

    print(cursor.fetchall())

    # Подтверждение транзакции
    conn.commit()

    # Закрытие соединения
    conn.close()

create_db()
