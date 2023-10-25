from django.db import models
from apps.authentication.models import Account
from rest_framework import serializers
from apps.atendimentos.models import Sala, Convenio, Area, Procedimento, Atendimentos

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class ProcedimentoSerializer(serializers.ModelSerializer):  # Inherit from serializers.ModelSerializer
    class Meta:
        model = Procedimento
        fields = '__all__'

class AtendimentoSerializer(serializers.ModelSerializer):  # Inherit from serializers.ModelSerializer
    class Meta:
        model = Atendimentos
        fields = '__all__'
