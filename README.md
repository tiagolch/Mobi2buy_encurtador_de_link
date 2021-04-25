# Desafio Tecnico Mobi2buy

## Implementação:

- Clonar projeto.
- Criar a virtual env `virtualenv -p python3 .vEnv`
- Ativar o virtualização `..vEnv/bin/activate`
- Instalar django, djangorestframework e django-filter `pip install -r requirements.txt`

- Adicionar `rest_framework` e `encurtadorLink` ao INSTALLED_APPS em Settings.

- Rodar `python manage.py makemigrations` e em seguida `python manage.py migrate`
- Criar o usuario admin com `python manage.py createsuperuser` e seguir o que se pede.
- Rodar `pyhton manage.py runserver`, pronto sua aplicação esta rodando.

## Documentação Endpoints

- https://short-link-mobi2buy.herokuapp.com/documentacao/
- https://short-link-mobi2buy.herokuapp.com/swagger/

