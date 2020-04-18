# Generated by Django 2.2.10 on 2020-04-17 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_auto_20200417_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichaanamnese',
            name='alimentacao',
            field=models.CharField(choices=[('1', 'Bom'), ('2', 'Regular'), ('3', 'Péssimo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='anticoncepcional',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Anticoncepcional'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='atv_fisica',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Atividade Física'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='bebida_alcoolica',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Bebida Alcoólica'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='cosmeticos',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Cosméticos'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='exposicao_sol',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Exposição ao Sol'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='filtro_solar',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Filtro Solar'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='gestante',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Gestante'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='intestino',
            field=models.CharField(choices=[('1', 'Bom'), ('2', 'Regular'), ('3', 'Péssimo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='lentes_contato',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Lentes de contato'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='sono',
            field=models.CharField(choices=[('1', 'Bom'), ('2', 'Regular'), ('3', 'Péssimo')], max_length=1),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='tabagismo',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Tabagismo'),
        ),
        migrations.AlterField(
            model_name='fichaanamnese',
            name='tratamento_anterior',
            field=models.CharField(choices=[('1', 'Sim'), ('2', 'Não')], max_length=1, verbose_name='Tratamento Anterior'),
        ),
    ]
