from database.models.settings import (
    Setting
)


class SettingsRepository:

    def __init__(
        self,
        db,
    ):
        self.db = db

    def get(
        self,
        key,
    ):
        return (
            self.db.query(Setting)
            .filter(
                Setting.key == key
            )
            .first()
        )

    def set(
        self,
        key,
        value,
    ):
        setting = self.get(
            key
        )

        if setting:
            setting.value = str(
                value
            )
        else:
            setting = Setting(
                key=key,
                value=str(value),
            )

            self.db.add(
                setting
            )

        self.db.commit()

        return setting