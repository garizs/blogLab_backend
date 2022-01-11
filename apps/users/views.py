from django.core.validators import validate_email
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.users.models import UserProfile
from apps.users.serializers import UsersSerializers


class UsersView(viewsets.GenericViewSet):
    """Класс для работы с пользователями"""
    serializer_class = UsersSerializers

    @extend_schema(tags=['Пользователи'], description='Получение аутенфтицированного пользователя')
    @action(detail=False, methods=['get'], permission_classes=(permissions.IsAuthenticated,))
    def current_user(self, request):
        user = UserProfile.objects.all().filter(user=request.user).first()
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)

    @extend_schema(tags=['Пользователи'], description='Изменение личных данных пользователя', )
    @action(detail=False, methods=['post'], permission_classes=(permissions.IsAuthenticated,))
    def change_user(self, request):
        user = request.user
        user_profile = UserProfile.objects.filter(user=user).first()
        data = request.data
        first_name = data.get('first_name')
        if first_name:
            user.first_name = first_name
        last_name = data.get('last_name')
        if last_name:
            user.last_name = last_name
        email = data.get('email')
        if email and validate_email(email):
            user.email = email
        password = data.get('password')
        if password:
            user.set_password(password)
        user.save()
        profile_picture = data.get('profile_picture')
        if profile_picture:
            user_profile.update(profile_picture=profile_picture)
        serializer = self.get_serializer(user_profile, many=False)
        return Response(serializer.data)

    @extend_schema(tags=['Пользователи'], description='Получение пользователя профиля',
                   parameters=[
                       OpenApiParameter(name='username', location='query',
                                        description='Никнейм пользователя')
                   ])
    @action(detail=False, methods=['get'])
    def get_user_profile(self, request):
        username = request.query_params.get('username')
        user_profile = UserProfile.objects.filter(user__username=username).first()

        serializer = self.get_serializer(user_profile, many=False)
        return Response(serializer.data)
