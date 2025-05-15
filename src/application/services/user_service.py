from typing import Optional
from uuid import UUID
from ...domain.models.user import User
from ...domain.ports.user_repository import UserRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def create_user(self, username: str, email: str, password: str) -> User:
        user = User.create(username, email, password)
        return self._user_repository.save(user)

    def get_user(self, user_id: UUID) -> Optional[User]:
        return self._user_repository.get_by_id(user_id) 