"""Модуль пользователей"""
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.users.models import UserProfile
from apps.auth.serializers import UsersSerializer


class UsersView(viewsets.GenericViewSet):
    """Класс для работы с пользователями"""
    serializer_class = UsersSerializer

    @classmethod
    @action(detail=False, methods=['post'])
    def register(cls, request):
        """Регистрация пользователей"""
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            is_found = UserProfile.objects.filter(Q(user__username=username) | Q(user__email=email))
            if not is_found:
                password = request.POST['password']
                first_name = request.POST['first_name']
                last_name = request.POST['last_name']
                user = User.objects.create_user(username=username, email=email,
                                                password=password, first_name=first_name,
                                                last_name=last_name)
                profile_picture = request.POST.get('profile_picture')
                if profile_picture:
                    UserProfile.objects.create(user=user, profile_picture=profile_picture)
                else:
                    UserProfile.objects.create(user=user)
                return Response(status=201, data={'status': 'Успешно создан'})
            return Response(status=400, data={'error': 'Пользователь уже зарегистрирован!'})
        return Response(status=400, data={'error': 'Неверный запрос!'})
