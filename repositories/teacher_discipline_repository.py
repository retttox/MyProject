
import sqlite3

from models.teacher_discipline import TeacherDiscipline


class TeacherDisciplineRepository:

    def __init__(self, database="teachers.db"):
        self.database = database

    def get_all(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM teacher_disciplines")
        rows = cursor.fetchall()

        connection.close()

        return [
            TeacherDiscipline(
                id=row[0],
                teacher_id=row[1],
                discipline_id=row[2]
            )
            for row in rows
        ]

    def get_by_teacher_id(self, teacher_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM teacher_disciplines WHERE teacher_id = ?",
            (teacher_id,)
        )

        rows = cursor.fetchall()
        connection.close()

        return [
            TeacherDiscipline(
                id=row[0],
                teacher_id=row[1],
                discipline_id=row[2]
            )
            for row in rows
        ]

    def add(self, teacher_id, discipline_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute(
            """INSERT INTO teacher_disciplines
               (teacher_id, discipline_id)
               VALUES (?, ?)""",
            (teacher_id, discipline_id)
        )

        connection.commit()
        connection.close()

    def update(self, link_id, teacher_id, discipline_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute(
            """UPDATE teacher_disciplines
               SET teacher_id=?, discipline_id=?
               WHERE id=?""",
            (teacher_id, discipline_id, link_id)
        )

        connection.commit()
        connection.close()

    def delete(self, link_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM teacher_disciplines WHERE id=?",
            (link_id,)
        )

        connection.commit()
        connection.close()
