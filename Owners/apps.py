from django.apps import AppConfig


class OwnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Owners'

    def ready(self):
        import Owners.signals