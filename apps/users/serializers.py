

from rest_framework import serializers

from apps.users.models import UserProfile


class UsersSerializers(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ('username', 'profile_picture')
