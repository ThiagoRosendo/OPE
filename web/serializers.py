from rest_framework import serializers
from .models import Servicos, Agenda


class ServicosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Servicos
        fields = '__all__'


class AgendaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Agenda
        fields = '__all__'