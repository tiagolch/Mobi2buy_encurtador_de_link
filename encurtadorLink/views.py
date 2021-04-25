from datetime import datetime, timedelta
from random import choices
from string import ascii_letters

from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from rest_framework import viewsets

from .models import urlsEncurtadas
from .serializers import urlEncurtadasSerializer

short_URL = 'https://tiag.o'


class urlViewSet(viewsets.ModelViewSet):
    filtro = datetime.today() - timedelta(days=7)
    queryset = urlsEncurtadas.objects.filter(data_criacao__gte=filtro)
    serializer_class = urlEncurtadasSerializer

    def perform_create(self, serializer):
        if not self.request.data['url_encurtada_sugestao']:
            short = short_URL + '/' + self.request.data['url_encurtada_sugestao'].join(choices(ascii_letters, k=5))
            serializer.save(url_encurtada_sugestao=short)
        else:
            short = short_URL + '/' + self.request.data['url_encurtada_sugestao']
            serializer.save(url_encurtada_sugestao=short)


class urlRedirect(View):
    def get(self, request, url_encurtada_sugestao, *args, **kwargs):
        linkEncurtado = short_URL + '/' + self.kwargs['url_encurtada_sugestao']
        redirect_link = urlsEncurtadas.objects.filter(url_encurtada_sugestao=linkEncurtado).first().url_original
        return redirect(redirect_link)
