# Generated by Django 2.2 on 2020-03-12 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20200311_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientemodel',
            name='image',
        ),
    ]