"""Модуль пользователей"""
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.db.models import Q
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.models import UserProfile
from apps.auth.serializers import UsersAuthSerializer


@extend_schema(tags=['Аунтентификация'])
class UsersView(viewsets.GenericViewSet):
    """Класс для работы с пользователями"""
    serializer_class = UsersAuthSerializer

    @classmethod
    @action(detail=False, methods=['post'])
    def register(cls, request):
        """Регистрация пользователей"""
        if request.method == 'POST':
            username = request.data['username']
            email = request.data['email']
            validate_email(email)
            is_found = UserProfile.objects.filter(Q(user__username=username) | Q(user__email=email))
            if not is_found:
                password = request.data['password']
                first_name = request.data.get('first_name')
                last_name = request.data.get('last_name')
                user = User.objects.create_user(username=username, email=email,
                                                password=password, first_name=first_name,
                                                last_name=last_name)
                profile_picture = request.data.get('profile_picture')
                if profile_picture:
                    UserProfile.objects.create(user=user, profile_picture=profile_picture)
                else:
                    UserProfile.objects.create(user=user)
                return Response(status=201, data={'status': 'Успешно создан'})
            return Response(status=400, data={'error': 'Пользователь уже зарегистрирован!'})
        return Response(status=400, data={'error': 'Неверный запрос!'})


@extend_schema(tags=['Токены'])
class CustomTokenObtainPairView(TokenObtainPairView):
    pass


@extend_schema(tags=['Токены'])
class CustomTokenRefreshView(TokenRefreshView):
    pass
