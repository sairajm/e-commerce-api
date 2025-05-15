from dataclasses import dataclass
from typing import Optional
from uuid import UUID

@dataclass
class User:
    id: Optional[UUID]
    username: str
    email: str
    password: str

    @classmethod
    def create(cls, username: str, email: str, password: str) -> 'User':
        return cls(
            id=None,
            username=username,
            email=email,
            password=password
        ) 