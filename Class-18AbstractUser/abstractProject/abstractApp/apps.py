from django.apps import AppConfig


class AbstractappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'abstractApp'
