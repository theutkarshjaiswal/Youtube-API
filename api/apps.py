from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        # Importing updater file
        from scheduler import updater
        updater.start()
