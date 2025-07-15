from sqlmodel import Session

from app.models.user import User
from app.repositories.base.base_repository import BaseRepository
from app.repositories.user.user_repository_interface import IUserRepository

class UserRepository(BaseRepository[User], IUserRepository):
    def __init__(self, session: Session):
        super().__init__(User, session)
