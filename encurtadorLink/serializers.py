from rest_framework import serializers

from .models import urlsEncurtadas


class urlEncurtadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = urlsEncurtadas
        fields = [
            'id',
            'url_original',
            'url_encurtada_sugestao',
            'data_expiracao'
            ]

