# Generated by Django 2.2.10 on 2020-04-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20200425_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='data',
            field=models.CharField(max_length=10),
        ),
    ]