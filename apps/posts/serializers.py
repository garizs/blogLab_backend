"""
    Сериализаторы API постов
"""
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework import serializers

from apps.posts.models import PostPicture, Post


class PostPictureSerializer(serializers.ModelSerializer):
    """
        Серилизатор изображений постов
    """

    class Meta:
        model = PostPicture
        fields = ('images',)


class PostBasicSerializer(serializers.ModelSerializer):
    """
        Сериализатор постов
    """
    images = PostPictureSerializer(read_only=True, source='post', many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'publish_date', 'text', 'images',)
        read_only_fields = ('title', 'author', 'publish_date', 'text')


@extend_schema_serializer(examples=[
    OpenApiExample(
        'Добавить в избранное',
        value={
            'id': 1,
            'action_code': 'add',
        },
        summary='Добавить в избранное',
        request_only=True,
        response_only=False
    ),
    OpenApiExample(
        'Убрать из избранного',
        value={
            'id': 1,
            'action_code': 'delete',
        },
        summary='Убрать из избранного',
        request_only=True,
        response_only=False
    ),
])
class PostFavouriteSerializer(PostBasicSerializer):
    id = serializers.IntegerField(required=True)
    action_code = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'publish_date', 'text', 'images', 'action_code')
        read_only_fields = ('title', 'author', 'publish_date', 'text')
