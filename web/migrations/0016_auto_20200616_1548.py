# Generated by Django 2.2.10 on 2020-06-16 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_auto_20200616_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to='profile', verbose_name='Foto de perfil'),
        ),
    ]