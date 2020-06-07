from django import forms
from .models import *
from .agenda import agenda

from django.forms import formset_factory


class ClienteCadForm(forms.ModelForm):

    class Meta:
        model = ClienteModel
        fields = [
            'nome', 'cpf', 'rg', 'data_nascimento', 'email',
            'tel_fixo', 'sexo', 'logradouro', 'numero', 'complemento',
            'bairro', 'cidade', 'uf', 'tel_cel', 'tel_emergency', 'cep', 'photo'
            ]


class ServicesForm(forms.ModelForm):

    class Meta:
        model = Servicos
        fields = [
            'nome', 'valor', 'descricao', 'images'
        ]

class PedidoForm(forms.ModelForm):
    
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoDetailForm(forms.ModelForm):
    
    class Meta:
        model = PedidoDetail
        fields = '__all__'


class AnamneseForm(forms.ModelForm):
    # Hábitos diários
    
    tratamento_anterior = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    lentes_contato = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    cosmeticos = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    exposicao_sol = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    filtro_solar = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    tabagismo = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    bebida_alcoolica = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    intestino = forms.CharField(widget=forms.RadioSelect(choices=ficha))
    sono = forms.CharField(widget=forms.RadioSelect(choices=ficha))
    alimentacao = forms.CharField(widget=forms.RadioSelect(choices=ficha))
    atv_fisica = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    anticoncepcional = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    gestante = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    
    # Histórico Clínico

    tratamento_medico = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    alergias = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    marcapasso = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    cardiaco = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    h_tensao = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    d_circulatorio = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    d_renal = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    d_hormonal = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    d_gastro = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    epilepsia = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    alteracoes_psic = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    estresse = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    diabetes = forms.CharField(widget=forms.RadioSelect(choices=booleano))
    doenca = forms.CharField(widget=forms.RadioSelect(choices=booleano)) 
    
    class Meta:

        model = FichaAnamnese
        fields = '__all__'


class AgendaForm(forms.ModelForm):
    
    
    class Meta:
        model = Agenda
        fields = '__all__'
    
class RegistroSessaoForm(forms.ModelForm):

    class Meta:
        model = RegistroSessao
        fields = '__all__'