# Generated by Django 3.2 on 2021-04-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encurtadorLink', '0011_alter_urlsencurtadas_data_expiracao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlsencurtadas',
            name='data_expiracao',
            field=models.DateField(verbose_name='Data de Expiracao'),
        ),
    ]