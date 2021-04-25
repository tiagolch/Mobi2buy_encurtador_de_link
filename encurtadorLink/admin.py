from django.contrib import admin

from .models import urlsEncurtadas


@admin.register(urlsEncurtadas)
class EncurtadorLinkAdmin(admin.ModelAdmin):
    list_display = [
        'url_original',
        'url_encurtada_sugestao',
        'ativo',
        'get_data_de_criacao',
        'get_data_de_expiracao',

    ]
    list_filter = ['data_criacao']
