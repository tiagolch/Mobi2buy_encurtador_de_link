# Generated by Django 3.2 on 2021-04-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encurtadorLink', '0005_alter_urlsencurtadas_url_encurtada_sugestao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlsencurtadas',
            name='url_encurtada_sugestao',
            field=models.URLField(blank=True, default='http://tiag.o/', null=True, unique=True, verbose_name='URL Encurtada'),
        ),
    ]
