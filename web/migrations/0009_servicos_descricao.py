# Generated by Django 2.2 on 2020-02-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_servicos_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicos',
            name='descricao',
            field=models.TextField(default='', verbose_name='Descrição'),
        ),
    ]
