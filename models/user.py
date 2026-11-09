from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    password: str
    role: str
    teacher_id: int = None