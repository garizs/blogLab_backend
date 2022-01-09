from rest_framework import serializers

from backend.blog.models import PostPicture, Post


class PostPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPicture
        fields = ('images',)


class PostBasicSerializer(serializers.ModelSerializer):
    images = PostPictureSerializer(read_only=True, source='post', many=True)

    class Meta:
        model = Post
        fields = ('title', 'author', 'publish_date', 'post_type', 'text', 'images',)

