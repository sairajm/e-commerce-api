from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from ..models.user import User

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: UUID) -> Optional[User]:
        pass 