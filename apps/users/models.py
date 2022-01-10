"""Users models"""
from django.contrib.auth import get_user_model

from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    """
        Модель пользователя
    """
    user = models.OneToOneField(get_user_model(), primary_key=True, on_delete=models.CASCADE,
                                verbose_name=_("Пользователь"))
    profile_picture = models.ImageField(upload_to='users', default='users/default.svg',
                                        verbose_name=_('Аватарка пользователя'))
    is_banned = models.BooleanField(default=False, verbose_name=_('Забаненный'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Админ'))
    is_editor = models.BooleanField(default=False, verbose_name=_('Редактор'))

    def __str__(self):
        return str(self.user.username)

    class Meta:
        verbose_name = _('Профиль пользователя')
        verbose_name_plural = _('Профили пользователей')
