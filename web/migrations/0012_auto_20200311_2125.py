# Generated by Django 2.2 on 2020-03-12 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20200311_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientemodel',
            name='image',
            field=models.ImageField(blank=True, default='clientes/profile/default.png', upload_to='clientes/profiles'),
        ),
    ]