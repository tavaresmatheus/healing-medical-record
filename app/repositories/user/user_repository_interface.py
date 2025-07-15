from app.models.user import User
from app.repositories.base.base_repository_interface import IBaseRepository

class IUserRepository(IBaseRepository[User]):
    pass
