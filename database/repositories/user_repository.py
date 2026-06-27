from database.repositories.base_repository import BaseRepository
from database.models.user import User


class UserRepository(BaseRepository):

    def get_by_username(self, username):
        return (
            self.session.query(User)
            .filter(User.username == username)
            .first()
        )