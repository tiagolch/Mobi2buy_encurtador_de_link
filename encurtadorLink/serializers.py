from rest_framework import serializers

from .models import urlsEncurtadas
from rest_framework.decorators import action


class urlEncurtadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = urlsEncurtadas
        fields = [
            'id',
            'url_original',
            'url_encurtada_sugestao',
            'data_expiracao'
            ]

