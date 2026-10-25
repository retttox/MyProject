
import sqlite3


def create_database():
    connection = sqlite3.connect("teachers.db")
    cursor = connection.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT,
            department TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS disciplines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            hours INTEGER,
            description TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teacher_disciplines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_id INTEGER NOT NULL,
            discipline_id INTEGER NOT NULL,
            UNIQUE (teacher_id, discipline_id),
            FOREIGN KEY (teacher_id) REFERENCES teachers(id),
            FOREIGN KEY (discipline_id) REFERENCES disciplines(id)
        )
    """)

    cursor.execute("SELECT COUNT(*) FROM teachers")
    count = cursor.fetchone()[0]

    if count == 0:
        cursor.execute("""
            INSERT INTO teachers (full_name, email, department)
            VALUES
            ('Иванов Иван Иванович', 'ivanov@example.com', 'Информатики'),
            ('Петров Пётр Петрович', 'petrov@example.com', 'Математики'),
            ('Сидорова Анна Сергеевна', 'sidorova@example.com', 'Программирования')
        """)

        cursor.execute("""
            INSERT INTO disciplines (name, hours, description)
            VALUES
            ('Основы программирования', 72, 'Изучение основ программирования'),
            ('Математика', 64, 'Изучение математических методов'),
            ('Базы данных', 48, 'Работа с базами данных')
        """)

        cursor.execute("""
            INSERT INTO teacher_disciplines (teacher_id, discipline_id)
            VALUES (1, 1), (2, 2), (3, 3)
        """)


    connection.commit()
    connection.close()

    print("Database and tables created successfully!")



if __name__ == "__main__":
    create_database()
