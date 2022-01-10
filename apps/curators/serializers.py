"""
    Сериализаторы API кураторов
"""

from rest_framework import serializers

from apps.curators.models import Curator


class CuratorsSerializer(serializers.ModelSerializer):
    """
        Сериализатор кураторов
    """

    class Meta:
        model = Curator
        fields = ('name', 'description', 'image',)
