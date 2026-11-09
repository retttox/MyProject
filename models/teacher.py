from dataclasses import dataclass


@dataclass
class Teacher:
    id: int
    full_name: str
    email: str
    department: str