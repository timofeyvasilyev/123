import sqlite3

def del_student(id) -> bool:
    try:
        conn = sqlite3.connect('db.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM students WHERE id=?', (id,))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False