# Generated by Django 2.2.10 on 2020-05-25 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200524_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='servico',
            field=models.CharField(max_length=255, verbose_name='Serviço'),
        ),
        migrations.AlterField(
            model_name='pedidodetail',
            name='servico',
            field=models.CharField(max_length=255, verbose_name='Serviço'),
        ),
    ]