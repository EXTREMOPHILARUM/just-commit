import json

class SettingsManager:
    def __init__(self, config_file='config/settings.json'):
        self.config_file = config_file
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            with open(self.config_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_settings(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get_feature_status(self, feature_key):
        return self.settings.get(feature_key, False)

    def set_feature_status(self, feature_key, status):
        self.settings[feature_key] = status
        self.save_settings()

if __name__ == "__main__":
    settings_manager = SettingsManager()
    # Example usage
    print(settings_manager.get_feature_status('intelligent_branch_naming'))
    settings_manager.set_feature_status('intelligent_branch_naming', True)
    print(settings_manager.get_feature_status('intelligent_branch_naming'))
