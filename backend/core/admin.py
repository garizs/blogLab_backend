"""
    Модуль для админ-панели
"""
from django.contrib import admin
from django.contrib.admin import display
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from backend.blog.models import Post, UserProfile, PostPicture


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
        return obj.user.username

    @display(description=_('Электронная почта'))
    def get_email(self, obj):
        return obj.user.email
