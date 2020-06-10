# Generated by Django 2.2.10 on 2020-06-09 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20200606_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor')),
                ('vencimento', models.DateField(verbose_name='Vencimento')),
                ('Status', models.CharField(choices=[('0', 'Pago'), ('1', 'A Pagar')], max_length=1, verbose_name='Status')),
            ],
        ),
    ]
