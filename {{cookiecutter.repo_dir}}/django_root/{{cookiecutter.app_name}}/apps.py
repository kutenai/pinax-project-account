from django.apps import AppConfig as BaseAppConfig
from django.utils.importlib import import_module


class AppConfig(BaseAppConfig):

    name = "{{cookiecutter.app_name}}"

    def ready(self):
        import_module("webapp.receivers")
