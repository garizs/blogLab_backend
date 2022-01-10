"""Модуль кураторов"""
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.curators.models import Curator
from apps.curators.serializers import CuratorsSerializer


@extend_schema(tags=['Кураторы'])
class CuratorsViewSet(viewsets.ModelViewSet):
    """Класс кураторов"""
    serializer_class = CuratorsSerializer
    queryset = Curator.objects.filter(is_main=True)
    http_method_names = ['get']
