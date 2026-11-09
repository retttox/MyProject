
from repositories.discipline_repository import DisciplineRepository


class DisciplineService:

    def __init__(self):
        self.repository = DisciplineRepository()

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, discipline_id):
        disciplines = self.repository.get_all()

        for discipline in disciplines:
            if discipline.id == discipline_id:
                return discipline

        raise ValueError("Дисциплина не найдена")

    def add_discipline(self, name, hours, description):
        if not name.strip():
            raise ValueError("Введите название дисциплины")

        if hours <= 0:
            raise ValueError("Количество часов должно быть больше нуля")

        self.repository.add(name, hours, description)

    def update_discipline(self, discipline_id, name, hours, description):
        disciplines = self.repository.get_all()

        if not any(discipline.id == discipline_id for discipline in disciplines):
            raise ValueError("Дисциплина не найдена")

        if not name.strip():
            raise ValueError("Введите название дисциплины")

        if hours <= 0:
            raise ValueError("Количество часов должно быть больше нуля")

        self.repository.update(
            discipline_id, name, hours, description
        )

    def delete_discipline(self, discipline_id):
        disciplines = self.repository.get_all()

        if not any(discipline.id == discipline_id for discipline in disciplines):
            raise ValueError("Дисциплина не найдена")

        self.repository.delete(discipline_id)
