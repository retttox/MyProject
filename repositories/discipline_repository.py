
import sqlite3

from models.discipline import Discipline


class DisciplineRepository:

    def __init__(self, database="teachers.db"):
        self.database = database

    def get_all(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM disciplines")
        rows = cursor.fetchall()

        connection.close()

        return [
            Discipline(
                id=row[0],
                name=row[1],
                hours=row[2],
                description=row[3]
            )
            for row in rows
        ]

    def add(self, name, hours, description):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO disciplines (name, hours, description) VALUES (?, ?, ?)",
            (name, hours, description)
        )

        connection.commit()
        connection.close()

    def update(self, discipline_id, name, hours, description):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE disciplines SET name=?, hours=?, description=? WHERE id=?",
            (name, hours, description, discipline_id)
        )

        connection.commit()
        connection.close()

    def delete(self, discipline_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM disciplines WHERE id=?",
            (discipline_id,)
        )

        connection.commit()
        connection.close()
