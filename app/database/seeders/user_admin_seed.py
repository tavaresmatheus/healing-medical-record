import datetime

from sqlmodel import Session

from app.config.config import Settings
from app.models.user import User
from app.repositories.user.user_repository import UserRepository
from app.repositories.user.user_repository_interface import IUserRepository
from app.database.database import engine

class UserAdminSeed:
    def __init__(self, user_repository: IUserRepository, settings: Settings):
        self.user_repository = user_repository
        self.settings = settings

    def seed(self) -> None:
        user = User(
            name=self.settings.admin_name,
            email=self.settings.admin_email,
            birth_date=datetime.date(2001, 1, 1),
            cpf='00000000000',
            rg='000000000',
            email_verified=True,
            password=self.settings.admin_password,
            created_at=datetime.datetime.now(datetime.timezone.utc)
        )
        self.user_repository.create(user)


if __name__ == '__main__':
    settings = Settings()

    with Session(engine) as session:
        user_repository = UserRepository(session)
        user_admin_seed = UserAdminSeed(user_repository, settings)
        user_admin_seed.seed()
