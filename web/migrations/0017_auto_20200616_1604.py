# Generated by Django 2.2.10 on 2020-06-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20200616_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='cargo',
            field=models.CharField(max_length=30, verbose_name='Cargo'),
        ),
    ]
