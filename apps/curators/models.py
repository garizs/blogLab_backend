from django.db import models
from django.forms import forms
from django.utils.translation import gettext_lazy as _


class Curator(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Имя и фамилия куратора'))
    description = models.TextField(verbose_name=_('Описание'))
    image = models.ImageField(upload_to='curators', verbose_name=_('Фотография'))
    is_main = models.BooleanField(default=False, verbose_name=_('На главной странице'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Куратор')
        verbose_name_plural = _('Кураторы')

    def clean(self):
        if len(Curator.objects.filter(is_main=True)) < 3:
            pass
        raise forms.ValidationError('Больше 3х кураторов!')

