# Generated by Django 3.2 on 2021-04-21 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encurtadorLink', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlsencurtadas',
            name='url_encurtada_sugestao',
            field=models.URLField(blank=True, null=True, unique=True, verbose_name='URL Encurtada'),
        ),
    ]
