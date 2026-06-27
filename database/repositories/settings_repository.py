from database.repositories.base_repository import BaseRepository
from database.models.settings import Settings


class SettingsRepository(BaseRepository):

    def get_setting(self, key):
        return (
            self.session.query(Settings)
            .filter(Settings.key == key)
            .first()
        )