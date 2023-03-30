from django.apps import AppConfig
from django.contrib.admin import apps


class BackEndConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "back_end"
