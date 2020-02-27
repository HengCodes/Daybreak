import os

from django.apps import AppConfig

default_app_config = 'project.ProjectConfig'


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


class ProjectConfig(AppConfig):
    name = 'project'
    verbose_name = "项目管理"
