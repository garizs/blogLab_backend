from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE,
                                verbose_name=_("Пользователь"))
    username = models.CharField(max_length=32, blank=False, verbose_name=_('Никнейм'))
    user_first_last_name = models.CharField(max_length=256, blank=True, verbose_name=_('ФИО пользователя'))
    email = models.EmailField(verbose_name=_('Email пользователя'))
    profile_picture = models.ImageField(upload_to='users', default='users/default.png',
                                        verbose_name=_('Аватарка пользователя'))
    is_banned = models.BooleanField(default=False, verbose_name=_('Забаненный'))
    is_admin = models.BooleanField(default=False, verbose_name=_('Админ'))
    is_editor = models.BooleanField(default=False, verbose_name=_('Редактор'))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('Профиль пользователя')
        verbose_name_plural = _('Профили пользователей')


class Post(models.Model):
    POST_TYPES = (
        ('MAIN', 'Главная'),
        ('COOK', 'Кулинария'),
        ('FASHION', 'Мода'),
        ('HOT', 'Горячее'),
        ('BLOGGERS', 'Блоггеры'),
    )
    title = models.CharField(max_length=256, verbose_name=_('Заголовок статьи'))
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=_('Автор статьи'))
    publish_date = models.DateTimeField(default=timezone.now, verbose_name=_('Дата публикации'))
    text = models.TextField(null=False, blank=False, default='Hello, World!', verbose_name=_('Текст статьи'))
    post_type = models.CharField(choices=POST_TYPES, max_length=15, verbose_name=_('Категория статьи'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')


class PostPicture(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post', verbose_name=_('Пост'))
    images = models.ImageField(upload_to='posts', default='', verbose_name=_('Изображение'))

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = _('Картинка статьи')
        verbose_name_plural = _('Картинки статьи')


class FavouritePosts(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Пост'))
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Избранный пост')
        verbose_name_plural = _('Избранные посты')
