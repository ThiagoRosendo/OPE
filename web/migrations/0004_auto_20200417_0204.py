# Generated by Django 2.2.10 on 2020-04-17 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200417_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedidodetail',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, verbose_name='Desconto'),
        ),
    ]
