from django import forms
from .models import ClienteModel, Servicos


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
        