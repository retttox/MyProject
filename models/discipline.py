from dataclasses import dataclass


@dataclass
class Discipline:
    id: int
    name: str
    hours: int
    description: str