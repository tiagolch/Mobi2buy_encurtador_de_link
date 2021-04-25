from datetime import datetime, timedelta
from django.utils import timezone

from django.db import models


class urlsEncurtadas(models.Model):
    url_original = models.URLField(verbose_name='URL Original', unique=True)
    url_encurtada_sugestao = models.CharField(max_length=50,
                                              blank=True,
                                              null=True,
                                              verbose_name='URL Encurtada',
                                              unique=True)
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True,
                                        verbose_name='Data de Criação')
    data_expiracao = models.DateField(verbose_name='Data de Expiracao', blank=True)

    def get_data_de_criacao(self):
        return self.data_criacao.strftime('%d/%m/%Y - %H:%M:%S')

    def get_data_de_expiracao(self):
        return self.data_expiracao.strftime('%d/%m/%Y')

    def __str__(self):
        return f'{self.url_original}'

    class Meta:
        verbose_name_plural = 'URLS Encurtadas'


