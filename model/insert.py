import sqlite3


def ins(name: str, last_name: str, course: str, fac: str) -> bool:
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO students (name, last_name, course, fac)
        VALUES (?, ?, ?, ?)
        ''', (name, last_name, course, fac))

        # Подтверждение транзакции
        conn.commit()
        # Закрытие соединения
        conn.close()
        return True

    except Exception as e:
        print(e)
        return False