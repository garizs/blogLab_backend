"""
    Сериализаторы API постов
"""

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


class PostFavouriteSerializer(PostBasicSerializer):
    id = serializers.IntegerField(required=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'publish_date', 'text', 'images',)
        read_only_fields = ('title', 'author', 'publish_date', 'text')


