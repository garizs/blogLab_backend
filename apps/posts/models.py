"""Post models"""
from django.utils import timezone

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import UserProfile


class Post(models.Model):
    """
        Модель постов
    """
    POST_TYPES = (
        ('MAIN', 'Главная'),
        ('COOK', 'Кулинария'),
        ('FASHION', 'Мода'),
        ('HOT', 'Горячее'),
        ('BLOGGERS', 'Блоггеры'),
    )
    title = models.CharField(max_length=256,
                             verbose_name=_('Заголовок статьи'))
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                               verbose_name=_('Автор статьи'))
    publish_date = models.DateTimeField(default=timezone.now,
                                        verbose_name=_('Дата публикации'))
    text = models.TextField(null=False, blank=False, default='Hello, World!',
                            verbose_name=_('Текст статьи'))
    post_type = models.CharField(choices=POST_TYPES, max_length=15,
                                 verbose_name=_('Категория статьи'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')


class PostPicture(models.Model):
    """
        Модель изображений постов
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post',
                             verbose_name=_('Пост'))
    images = models.ImageField(upload_to='posts', default='',
                               verbose_name=_('Изображение'))

    def __str__(self):
        return self.post.title

    class Meta:
        verbose_name = _('Картинка статьи')
        verbose_name_plural = _('Картинки статьи')


class FavouritePosts(models.Model):
    """
        Модель избранных постов
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_('Пост'))
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Избранный пост')
        verbose_name_plural = _('Избранные посты')
