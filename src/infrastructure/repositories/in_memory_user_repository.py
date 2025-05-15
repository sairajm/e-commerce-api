from typing import Optional
from uuid import UUID, uuid4
from ...domain.models.user import User
from ...domain.ports.user_repository import UserRepository

class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._users: dict[UUID, User] = {}

    def save(self, user: User) -> User:
        if user.id is None:
            user.id = uuid4()
        self._users[user.id] = user
        return user

    def get_by_id(self, user_id: UUID) -> Optional[User]:
        return self._users.get(user_id) 