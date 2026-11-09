from repositories.user_repository import UserRepository
from repositories.teacher_repository import TeacherRepository


class AuthService:

    def __init__(self):
        self.repository = UserRepository()
        self.teacher_repository = TeacherRepository()

    def get_teachers(self):
        teachers = self.teacher_repository.get_all()

        return [
            (teacher.id, teacher.full_name)
            for teacher in teachers
        ]

    def register(self, username, password, teacher_id=None):
        if not username.strip():
            raise ValueError("Введите логин")

        if len(password) < 4:
            raise ValueError("Пароль должен содержать минимум 4 символа")

        if self.repository.get_by_username(username):
            raise ValueError("Такой пользователь уже существует")

        if self.repository.get_count() == 0:
            role = "admin"
            teacher_id = None

        else:
            role = "user"

            if teacher_id is None:
                raise ValueError("Выберите преподавателя")

            teachers = self.teacher_repository.get_all()

            if not any(teacher.id == teacher_id for teacher in teachers):
                raise ValueError("Такого преподавателя нет")

            if self.repository.get_by_teacher_id(teacher_id):
                raise ValueError(
                    "Этот преподаватель уже привязан к аккаунту"
                )

        self.repository.add(
            username, password, role, teacher_id
        )

    def link_teacher(self, username, teacher_id):
        user = self.repository.get_by_username(username)

        if user is None:
            raise ValueError("Пользователь не найден")

        if user.role == "admin":
            raise ValueError(
                "Нельзя привязать преподавателя к администратору"
            )

        teachers = self.teacher_repository.get_all()

        if not any(teacher.id == teacher_id for teacher in teachers):
            raise ValueError("Такого преподавателя нет")

        linked_user = self.repository.get_by_teacher_id(teacher_id)

        if linked_user is not None and linked_user.username != username:
            raise ValueError(
                "Этот преподаватель уже привязан к другому аккаунту"
            )

        self.repository.link_teacher(username, teacher_id)

    def login(self, username, password):
        user = self.repository.get_by_username(username)

        if user is None or user.password != password:
            raise ValueError("Неверный логин или пароль")

        return {
            "id": user.id,
            "username": user.username,
            "role": user.role,
            "teacher_id": user.teacher_id
        }