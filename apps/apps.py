from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PostsConfig(AppConfig):
    name = 'apps.posts'
    verbose_name = _("Посты")


class UsersConfig(AppConfig):
    name = 'apps.users'
    verbose_name = _("Пользователи")


class AuthConfig(AppConfig):
    name = 'apps.auth'
    label = 'users_auth'
