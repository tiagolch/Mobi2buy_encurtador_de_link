from datetime import date, timedelta
from random import choices
from string import ascii_letters

from django.shortcuts import redirect
from django.views import View
from rest_framework import viewsets

from .models import urlsEncurtadas
from .serializers import urlEncurtadasSerializer

short_URL = 'https://short-link-mobi2buy.herokuapp.com'
filtro = date.today() - timedelta(days=7)


class urlViewSet(viewsets.ModelViewSet):
    queryset = urlsEncurtadas.objects.filter(data_criacao__gte=filtro)
    serializer_class = urlEncurtadasSerializer

    def perform_create(self, serializer):
        if not self.request.data['url_encurtada_sugestao']:
            short = short_URL + '/' + self.request.data['url_encurtada_sugestao'].join(choices(ascii_letters, k=5))
            if self.request.data['data_expiracao']:
                serializer.save(url_encurtada_sugestao=short, data_expiracao__isnull=filtro)
            else:
                serializer.save(url_encurtada_sugestao=short)
        else:
            short = short_URL + '/' + self.request.data['url_encurtada_sugestao']
            if self.request.data['data_expiracao']:
                serializer.save(url_encurtada_sugestao=short, data_expiracao__isnull=filtro)
            else:
                serializer.save(url_encurtada_sugestao=short)


class urlRedirect(View):
    def get(self, request, url_encurtada_sugestao, *args, **kwargs):
        linkEncurtado = short_URL + '/' + self.kwargs['url_encurtada_sugestao']
        redirect_link = urlsEncurtadas.objects.filter(url_encurtada_sugestao=linkEncurtado).first().url_original
        return redirect(redirect_link)



