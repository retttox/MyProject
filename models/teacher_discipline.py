from dataclasses import dataclass


@dataclass
class TeacherDiscipline:
    id: int
    teacher_id: int
    discipline_id: int