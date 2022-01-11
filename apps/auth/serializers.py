"""Модуль сериализации юзеров"""
from rest_framework import serializers
from rest_framework.fields import CharField, FileField


class UsersAuthSerializer(serializers.Serializer):
    """Сериализатор пользователей"""
    username = CharField(label='Юзернейм', required=True)
    password = CharField(label='Пароль', required=True)
    email = CharField(label='Почта', required=True)
    first_name = CharField(label='Имя', required=False)
    last_name = CharField(label='Фамилия', required=False)
    profile_picture = FileField(label='Аватар', required=False)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
