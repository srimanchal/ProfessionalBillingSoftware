from database.session import SessionLocal
from database.models.user import User
from services.password_service import PasswordService


class FirstRunService:

    def __init__(self):
        self.db = SessionLocal()

    def is_first_run(self):
        return (
            self.db.query(User)
            .count()
            == 0
        )

    def create_admin(
        self,
        username,
        password,
    ):
        user = User(
            username=username,
            password_hash=PasswordService.hash_password(
                password
            ),
            full_name="Administrator",
            role="Administrator",
            is_active=True,
        )

        self.db.add(user)
        self.db.commit()

        return user