import json

from util.GameInstance import GameInstance


class Settings:
    file_path = "assets/settings/general.json"
    settings = {}

    @staticmethod
    def load():
        # Load the settings from the JSON file
        with open(Settings.file_path, "r") as f:
            Settings.settings = json.load(f)

        for setting, value in Settings.settings.items():
            setattr(Settings, setting, value)

    @staticmethod
    def get(setting_name):
        return Settings.settings[setting_name]

    @staticmethod
    def set(setting_name, value):
        Settings.settings[setting_name] = value

    @staticmethod
    def save():
        # Save the settings to the JSON file
        with open(Settings.file_path, "w") as f:
            json.dump(Settings.settings, f, indent=4)

        GameInstance.save_instance()
