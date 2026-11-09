import sqlite3

from models.user import User


class UserRepository:

    def __init__(self, database="teachers.db"):
        self.database = database

    def get_count(self):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]

        connection.close()

        return count

    def get_by_username(self, username):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, password, role, teacher_id
            FROM users
            WHERE username = ?
        """, (username,))

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        return User(
            id=row[0],
            username=row[1],
            password=row[2],
            role=row[3],
            teacher_id=row[4]
        )

    def get_by_teacher_id(self, teacher_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, username, password, role, teacher_id
            FROM users
            WHERE teacher_id = ?
        """, (teacher_id,))

        row = cursor.fetchone()
        connection.close()

        if row is None:
            return None

        return User(
            id=row[0],
            username=row[1],
            password=row[2],
            role=row[3],
            teacher_id=row[4]
        )

    def add(self, username, password, role, teacher_id=None):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO users (username, password, role, teacher_id)
                VALUES (?, ?, ?, ?)
            """, (username, password, role, teacher_id))

            connection.commit()

        finally:
            connection.close()

    def link_teacher(self, username, teacher_id):
        connection = sqlite3.connect(self.database)
        cursor = connection.cursor()

        try:
            cursor.execute("""
                UPDATE users
                SET teacher_id = ?
                WHERE username = ?
            """, (teacher_id, username))

            connection.commit()

        finally:
            connection.close()