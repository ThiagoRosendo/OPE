from django.db import models

class ClienteModel(models.Model):
    sexo_choices = [['Feminino', 'Feminino'], ['Masculino', 'Masculino']]
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)

    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', primary_key=True, null=False, max_length=14)
    rg = models.CharField('RG', max_length=20, null=True)
    data_nascimento = models.CharField('Data de nascimento', max_length=10, null=False, default='01/01/1900')
    sexo = models.CharField(max_length=9, choices=sexo_choices, null=True, blank=True)
    photo = models.ImageField('Foto de perfil', upload_to='profile', default='default.jpg', blank=True)
    
    # Contato

    tel_fixo = models.CharField('Telefone Residencial', max_length=15, blank=True)
    tel_cel = models.CharField('Telefone Celular', max_length=15, blank=True)
    tel_emergency = models.CharField('Telefone Emergência', max_length=15, blank=True)
    email = models.EmailField('E-mail', blank=True)

    # Endereço
    cep = models.CharField('CEP', null=False, blank=False, default='', max_length=9)
    logradouro = models.CharField('Endereço', max_length=100, null=False, default='')
    numero = models.CharField('Número', null=False, max_length=5, blank=False, default=0)
    complemento = models.CharField('Complemento', max_length=30, null=False, blank=True)
    bairro = models.CharField('Bairro', max_length=100, null=False, blank=False, default='')
    cidade = models.CharField('Cidade', max_length=100, null=False, blank=False, default='')
    uf = models.CharField('Estado', max_length=2, null=False, blank=False, default='')
    

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Servicos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', default='', null=False, max_length=50)
    valor = models.FloatField('Valor', null=False, default=0)
    descricao = models.TextField('Descrição', default='', null=False)
    images = models.FileField('Imagens', blank=True, upload_to="servicos/imagens/")
    
    
    
    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

