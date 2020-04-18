# Generated by Django 2.2.10 on 2020-04-16 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClienteModel',
            fields=[
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de cadastro')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=14, primary_key=True, serialize=False, verbose_name='CPF')),
                ('rg', models.CharField(max_length=20, null=True, verbose_name='RG')),
                ('data_nascimento', models.CharField(default='01/01/1900', max_length=10, verbose_name='Data de nascimento')),
                ('sexo', models.CharField(blank=True, choices=[['Feminino', 'Feminino'], ['Masculino', 'Masculino']], max_length=9, null=True)),
                ('photo', models.ImageField(blank=True, default='default.jpg', upload_to='profile', verbose_name='Foto de perfil')),
                ('tel_fixo', models.CharField(blank=True, max_length=15, verbose_name='Telefone Residencial')),
                ('tel_cel', models.CharField(blank=True, max_length=15, verbose_name='Telefone Celular')),
                ('tel_emergency', models.CharField(blank=True, max_length=15, verbose_name='Telefone Emergência')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail')),
                ('cep', models.CharField(default='', max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(default='', max_length=100, verbose_name='Endereço')),
                ('numero', models.CharField(default=0, max_length=5, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=30, verbose_name='Complemento')),
                ('bairro', models.CharField(default='', max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(default='', max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(default='', max_length=2, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(auto_now_add=True, verbose_name='Data do pedido')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente_pedido', to='web.ClienteModel', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
        ),
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='', max_length=50, verbose_name='Nome')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor')),
                ('descricao', models.TextField(default='', verbose_name='Descrição')),
                ('images', models.FileField(blank=True, upload_to='servicos/imagens/', verbose_name='Imagens')),
            ],
            options={
                'verbose_name': 'Serviço',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='PedidoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField(verbose_name='Quantidade')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedido_det', to='web.Pedido')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Servicos')),
            ],
        ),
    ]
