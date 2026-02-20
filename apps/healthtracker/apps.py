from django.apps import AppConfig


class CaloriesConfig(AppConfig):
    name = 'apps.healthtracker'

    def ready(self, **kwargs):
        import apps.healthtracker.signals
