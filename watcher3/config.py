import json
import os
from datetime import datetime

class Config:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
        except FileNotFoundError:
            print(f"Файлът с конфигурацията {self.config_file} не беше намерен.")
            return {}

        for directory in config_data.get('directories', []):
            directory['start_time'] = datetime.strptime(directory['start_time'], '%H:%M').time()
            directory['end_time'] = datetime.strptime(directory['end_time'], '%H:%M').time()
            directory['last_checked'] = directory.get('last_checked', None)

        return config_data

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=4)

# Пример за конфигурационен файл config.json:
# {
#     "directories": [
#         # ...
#     ],
#     "max_workers": 3,
#     "sleep_time": 60,
#     # ... други настройки
# }