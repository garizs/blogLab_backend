from django.contrib import admin
from django.utils.safestring import mark_safe
from backend.blog.models import Post, UserProfile, PostPicture


class PicturesInline(admin.StackedInline):
    model = PostPicture
    fields = ('images', 'image_tag',)
    readonly_fields = ('image_tag',)
    extra = 1

    def image_tag(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.images.url,
            width=400,
            height=400,
        )
        )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    inlines = [PicturesInline]

    def save_model(self, request, obj, form, change):
        obj.save()
        pictures = request.FILES.getlist('pictures')
        for picture in pictures:
            PostPicture.objects.create(post=obj, image=picture)
        return super().save_model(request, obj, form, change)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_banned', 'is_admin', 'is_editor')
    ordering = ('username',)
    list_filter = ('is_admin', 'is_admin', 'is_banned')
    search_fields = ('username', 'email')
