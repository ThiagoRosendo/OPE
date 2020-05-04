from django.db import models
from .agenda import agenda
from datetime import date

ficha = (
    (u'1', u'Bom'),
    (u'2', u'Regular'),
    (u'3', u'Péssimo')
)
booleano = (
    (u'1', u'Sim'),
    (u'2', u'Não')
)

horarios = (
    ('07:30', '07:30'), ('08:00', '08:00'), ('08:30', '08:30'), ('09:00', '09:00'), ('09:30', '09:30'),
    ('10:00', '10:00'), ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'),
    ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'), ('13:30', '13:30'),
    ('14:00', '14:00'), ('14:30', '14:30'), ('15:00', '15:00'), ('15:30', '15:30'),
    ('16:00', '16:00'), ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'),
    ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'), ('19:30', '19:30'),
    ('20:00', '20:00'), ('20:30', '20:30'), ('21:00', '21:00'), ('21:30', '21:30')
)

class ClienteModel(models.Model):
    sexo_choices = [['Feminino', 'Feminino'], ['Masculino', 'Masculino']]
    data_cadastro = models.DateTimeField('Data de cadastro', auto_now_add=True)

    nome = models.CharField('Nome', max_length=50)
    cpf = models.CharField('CPF', primary_key=True, null=False, max_length=14)
    rg = models.CharField('RG', max_length=20, null=True)
    data_nascimento = models.DateField('Data de nascimento')
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

    def idade(self):
        hoje = date.today()
        idade = hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day)) 
        return '%d anos' % idade

    def data_formatada(self):
        dia = self.data_nascimento.day
        mes = self.data_nascimento.month
        ano = self.data_nascimento.year
        data = date(ano, mes, dia)
        return data

class Servicos(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField('Nome', default='', null=False, max_length=50, unique=True)
    valor = models.DecimalField('Valor', null=False, max_digits=7, decimal_places=2)
    descricao = models.TextField('Descrição', default='', null=False)
    images = models.FileField('Imagens', blank=True, upload_to="servicos/imagens/")
    
    def __str__(self):
        return self.nome

    def get_valor(self):
        return self.valor

    def get_nome(self):
        return self.nome
       

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(ClienteModel, related_name='cliente_pedido', verbose_name='cliente', on_delete=models.CASCADE)
    data = models.DateField('Data do pedido', auto_now_add=True)
    valor_total = models.DecimalField('Valor Total', max_digits=7, decimal_places=2)
    desconto = models.DecimalField('Desconto', decimal_places=1, max_digits=3, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'

    

class PedidoDetail(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='pedido_det', on_delete=models.CASCADE)
    servico = models.ForeignKey(Servicos, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField('Quantidade')
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    subtotal = models.DecimalField('Subtotal', max_digits=7, decimal_places=2)
    

    def __str__(self):

        return '(%s) %s' % (self.pedido, self.servico)

    def get_cliente_name(self):
        return self.pedido.cliente.nome

class FichaAnamnese(models.Model):
    cliente = cliente = models.ForeignKey(ClienteModel, related_name='ficha_cliente', verbose_name='cliente', on_delete=models.CASCADE)

    # Hábitos díarios

    tratamento_anterior = models.CharField('Tratamento Anterior', choices=booleano, max_length=1)
    lentes_contato = models.CharField('Lentes de contato', choices=booleano, max_length=1)
    cosmeticos = models.CharField('Cosméticos', choices=booleano, max_length=1)
    exposicao_sol = models.CharField('Exposição ao Sol', choices=booleano, max_length=1)
    filtro_solar = models.CharField('Filtro Solar', choices=booleano, max_length=1)
    tabagismo = models.CharField('Tabagismo', choices=booleano, max_length=1)
    bebida_alcoolica = models.CharField('Bebida Alcoólica', choices=booleano, max_length=1)
    intestino = models.CharField(choices=ficha, max_length=1)
    sono = models.CharField(choices=ficha, max_length=1)
    alimentacao = models.CharField(choices=ficha, max_length=1)
    atv_fisica = models.CharField('Atividade Física', choices=booleano, max_length=1)
    anticoncepcional = models.CharField('Anticoncepcional', choices=booleano, max_length=1)
    gestante = models.CharField('Gestante', choices=booleano, max_length=1)
    

    # Histórico Clínico

    tratamento_medico = models.CharField('Tratamento Médico', choices=booleano, max_length=1)
    alergias = models.CharField('Antecedentes Alérgicos', choices=booleano, max_length=1)
    marcapasso = models.CharField('Portador de Marcapasso', choices=booleano, max_length=1)
    cardiaco = models.CharField('Alterações Cardíacas', choices=booleano, max_length=1)
    h_tensao = models.CharField('Hipo/hipertensão arterial', choices=booleano, max_length=1)
    d_circulatorio = models.CharField('Distúrbio Circulatório', choices=booleano, max_length=1)
    d_renal = models.CharField('Distúrbio Renal', choices=booleano, max_length=1)
    d_hormonal = models.CharField('Distúrbio Hormonal', choices=booleano, max_length=1)
    d_gastro = models.CharField('Distúrbio gastro-intestinal', choices=booleano, max_length=1)
    epilepsia = models.CharField('Epilepsia- convulsões', choices=booleano, max_length=1)
    alteracoes_psic = models.CharField('Alterações psicológicas/ psiquiátricas', choices=booleano, max_length=1)
    estresse = models.CharField('Estresse', choices=booleano, max_length=1)
    diabetes = models.CharField('Diabetes', choices=booleano, max_length=1)
    doenca = models.CharField('Algum tipo de doença', choices=booleano, max_length=1)
    

class Agenda(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(ClienteModel, related_name='cliente_agenda', verbose_name='cliente', on_delete=models.CASCADE)
    pedido = models.ForeignKey(PedidoDetail, related_name='pedido_agenda', verbose_name='pedido', on_delete=models.CASCADE)
    servico = models.CharField('Serviço', max_length=50)
    data = models.DateField()
    hora_inicio = models.CharField(choices=horarios, max_length=5)
    hora_fim = models.CharField(choices=horarios, max_length=5)
    



