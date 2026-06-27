from database.session import SessionLocal
from database.models.user import User
from database.repositories.user_repository import UserRepository
from services.password_service import PasswordService
from app.logger import logger


class AuthService:

    def __init__(self):
        self.db = SessionLocal()
        self.user_repository = UserRepository(self.db)

    def create_default_admin(self):

        if self.user_repository.user_exists():
            return

        admin = User(
            username="admin",
            password_hash=PasswordService.hash_password(
                "admin123"
            ),
            full_name="Administrator",
            role="Administrator",
            is_active=True,
        )

        self.user_repository.add(admin)

        logger.info(
            "Default administrator account created."
        )

    def authenticate(
        self,
        username,
        password
    ):

        user = self.user_repository.get_by_username(
            username
        )

        if not user:
            return None

        if not PasswordService.verify_password(
            password,
            user.password_hash
        ):
            return None

        return user