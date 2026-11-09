
import sqlite3

from models.teacher import Teacher


class TeacherRepository:

    def __init__(self, database="teachers.db"):
        self.database = database

    def get_all(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM teachers")
        rows = cursor.fetchall()

        connection.close()

        return [
            Teacher(id=row[0], full_name=row[1],
                    email=row[2], department=row[3])
            for row in rows
        ]

    def add(self, full_name, email, department):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO teachers (full_name, email, department) VALUES (?, ?, ?)",
            (full_name, email, department)
        )

        connection.commit()
        connection.close()

    def update(self, teacher_id, full_name, email, department):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE teachers SET full_name=?, email=?, department=? WHERE id=?",
            (full_name, email, department, teacher_id)
        )

        connection.commit()
        connection.close()

    def delete(self, teacher_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM teachers WHERE id=?",
            (teacher_id,)
        )

        connection.commit()
        connection.close()
