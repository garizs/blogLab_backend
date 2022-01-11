from rest_framework import serializers

from apps.users.models import UserProfile


class UsersSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', required=False)
    last_name = serializers.CharField(source='user.last_name', required=False)
    email = serializers.CharField(source='user.email', required=False)
    password = serializers.CharField(source='user.password', required=False, write_only=True)
    username = serializers.CharField(source='user.username', required=False, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'first_name', 'last_name', 'email', 'profile_picture')
        extra_kwargs = {
            'profile_picture': {'required': False}
        }

