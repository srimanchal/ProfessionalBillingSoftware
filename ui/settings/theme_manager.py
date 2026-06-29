from services.settings_service import (
    SettingsService
)

from ui.themes.dark_theme import (
    DARK_THEME
)

from ui.themes.light_theme import (
    LIGHT_THEME
)


class ThemeManager:

    @staticmethod
    def apply(app):
        settings = SettingsService()

        theme = settings.get(
            "theme",
            "dark"
        )

        if theme == "dark":
            app.setStyleSheet(
                DARK_THEME
            )
        else:
            app.setStyleSheet(
                LIGHT_THEME
            )