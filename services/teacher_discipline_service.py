
from repositories.teacher_discipline_repository import TeacherDisciplineRepository
from services.discipline_service import DisciplineService
from services.teacher_service import TeacherService


class TeacherDisciplineService:

    def __init__(self):
        self.repository = TeacherDisciplineRepository()
        self.discipline_service = DisciplineService()
        self.teacher_service = TeacherService()

    def get_by_teacher_id(self, teacher_id):
        links = self.repository.get_by_teacher_id(teacher_id)

        disciplines = []

        for link in links:
            discipline = self.discipline_service.get_by_id(
                link.discipline_id
            )
            disciplines.append(discipline)

        return disciplines

    def assign_discipline(self, teacher_id, discipline_id):
        self.teacher_service.get_by_id(teacher_id)
        self.discipline_service.get_by_id(discipline_id)

        links = self.repository.get_by_teacher_id(teacher_id)

        for link in links:
            if link.discipline_id == discipline_id:
                raise ValueError("Эта дисциплина уже назначена преподавателю")

        self.repository.add(teacher_id, discipline_id)
