# Generated by Django 2.2.10 on 2020-04-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20200427_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='data_nascimento',
            field=models.CharField(max_length=10, verbose_name='Data de nascimento'),
        ),
    ]