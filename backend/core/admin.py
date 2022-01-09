"""
    Модуль для админ-панели
"""
from django.contrib import admin
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
    list_display = ('username', 'email', 'is_banned', 'is_admin', 'is_editor')
    ordering = ('username',)
    list_filter = ('is_admin', 'is_admin', 'is_banned')
    search_fields = ('username', 'email')
