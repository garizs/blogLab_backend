from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.users.models import UserProfile
from apps.users.serializers import UsersSerializers


class UsersView(viewsets.GenericViewSet):
    """Класс для работы с пользователями"""
    serializer_class = UsersSerializers

    @action(detail=False, methods=['get'], permission_classes=(permissions.IsAuthenticated,))
    def current_user(self, request):
        user = UserProfile.objects.all().filter(user=request.user).first()
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)
