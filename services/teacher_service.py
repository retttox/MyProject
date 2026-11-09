
from repositories.teacher_repository import TeacherRepository


class TeacherService:

    def __init__(self):
        self.repository = TeacherRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, teacher_id):
        teachers = self.repository.get_all()

        for teacher in teachers:
            if teacher.id == teacher_id:
                return teacher

        raise ValueError("Преподаватель не найден")

    def add_teacher(self, full_name, email, department):
        if not full_name.strip():
            raise ValueError("Введите ФИО преподавателя")

        if email and "@" not in email:
            raise ValueError("Некорректный email")

        if not department.strip():
            raise ValueError("Введите кафедру")

        self.repository.add(full_name, email, department)

    def update_teacher(self, teacher_id, full_name, email, department):
        teachers = self.repository.get_all()

        if not any(teacher.id == teacher_id for teacher in teachers):
            raise ValueError("Преподаватель не найден")

        if not full_name.strip():
            raise ValueError("Введите ФИО преподавателя")

        if email and "@" not in email:
            raise ValueError("Некорректный email")

        if not department.strip():
            raise ValueError("Введите кафедру")

        self.repository.update(
            teacher_id, full_name, email, department
        )

    def delete_teacher(self, teacher_id):
        teachers = self.repository.get_all()

        if not any(teacher.id == teacher_id for teacher in teachers):
            raise ValueError("Преподаватель не найден")

        self.repository.delete(teacher_id)
