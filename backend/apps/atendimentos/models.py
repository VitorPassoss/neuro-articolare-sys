from django.db import models
from apps.authentication.models import Account


class Sala(models.Model):
    nome =  models.CharField(max_length=155)

class Convenio(models.Model):
    nome =  models.CharField(max_length=155)

class Area(models.Model):
    nome =  models.CharField(max_length=155)

class Procedimento(models.Model):
    nome = models.CharField(max_length=155)


STATUS = [("AG", "Agendado"), 
          ("NA", "Nao atendido"), 
          ("A", "Atendido"), 
          ("NAS", "Nao atendido (sem cobrança)"), 
          ("R", "Remarcar"),
          ("F", "Faltou"),
          ("PC", "Presença confirmada"),
          ("C", "Cancelado"),
          ]


class Atendimentos(models.Model):
    profissional =  models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='profissional')
    paciente =  models.ForeignKey(Account, on_delete=models.CASCADE, null=True, related_name='paciente') 
    sala =  models.ForeignKey(Sala, on_delete=models.CASCADE, null=True)
    convenio = models.ForeignKey(Convenio, on_delete=models.CASCADE, null=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.CASCADE, null=True)
    status = models.CharField(
        max_length=4, choices=STATUS
    )
    detalhes = models.CharField(max_length=155)
    dt_atend = models.DateTimeField(auto_now_add=True, null=True)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    celular_atd = models.CharField(max_length=155)
    lembrete_sms = models.CharField(max_length=155)
    lembrete_wpp = models.CharField(max_length=155)
    dt_inicio = models.DateTimeField(auto_now_add=True)
    dt_fim = models.DateTimeField(auto_now_add=True)