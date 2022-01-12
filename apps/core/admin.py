"""
    Модуль для админ-панели
"""
from django.contrib import admin
from django.contrib.admin import display
from django.forms import forms
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe

from apps.curators.models import Curator
from apps.posts.models import Post, PostPicture
from apps.users.models import UserProfile


class PicturesInline(admin.StackedInline):
    """
        Класс отображения и изменения изображений постов
    """
    model = PostPicture
    fields = ('images', 'image_tag',)
    readonly_fields = ('image_tag',)
    extra = 1

    @classmethod
    def image_tag(cls, obj):
        """
            Метод отображения изображений в админ-панели
        """
        url = obj.images.url
        width = 400
        height = 400
        return mark_safe(f'<img src="{url}" width="{width}" height={height} />')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
        Класс изменения постов
    """
    list_display = ('title', 'author', 'publish_date')
    inlines = [PicturesInline]


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
        Класс отображения и изменения пользователей
    """

    @classmethod
    def image_tag(cls, obj):
        """
            Метод отображения изображений в админ-панели
        """
        url = obj.profile_picture.url
        width = 400
        height = 400
        return mark_safe(f'<img src="{url}" width="{width}" height={height} />')

    image_tag.short_description = _('Изображение')
    list_display = ('get_username', 'get_email', 'is_banned', 'is_admin', 'is_editor')
    list_filter = ('is_admin', 'is_admin', 'is_banned')
    readonly_fields = ('image_tag',)
    search_fields = ('get_username', 'get_email')

    @display(ordering='user__username', description=_('Имя пользователя'))
    def get_username(self, obj):
        """Получение никнейма для отображения"""
        return obj.user.username

    @display(description=_('Электронная почта'))
    def get_email(self, obj):
        """Получение почты для отображения"""
        return obj.user.email


@admin.register(Curator)
class CuratorAdmin(admin.ModelAdmin):
    """
        Класс отображения и изменения пользователей
    """

    @classmethod
    def image_tag(cls, obj):
        """
            Метод отображения изображений в админ-панели
        """
        url = obj.image.url
        width = 400
        height = 400
        return mark_safe(f'<img src="{url}" width="{width}" height={height} />')

    image_tag.short_description = _('Изображение')
    list_display = ('get_name', 'get_main')
    readonly_fields = ('image_tag',)
    search_fields = ('get_name', 'get_main')

    @display(ordering='user__username', description=_('Имя пользователя'))
    def get_name(self, obj):
        """Получение никнейма для отображения"""
        return obj.name

    @display(description=_('На главной'))
    def get_main(self, obj):
        """Получение почты для отображения"""
        return obj.is_main
