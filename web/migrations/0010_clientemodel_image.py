# Generated by Django 2.2 on 2020-03-11 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_servicos_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientemodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='web/media/profiles'),
        ),
    ]
