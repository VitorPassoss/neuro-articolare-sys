
from django.db import models
from django.contrib.auth.models import User



class Account(models.Model):
    nome = models.CharField(max_length=155)
    cargo = models.CharField(max_length=155)
    tipo = models.BooleanField(default=False)
    permissao = models.JSONField(default=None)
    colaborador = models.BooleanField(default=False)
    dt_nasc = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    id_ref = models.CharField(max_length=155)
    ref = models.CharField(max_length=155)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta: 
        ordering = ['-created_at'] 

CONTATO = [
    ("E", "Email"),
    ("T", "Telefone"),
    ("C", "Celular"),

]

class Contatos(models.Model):
    nome_contato = models.CharField(max_length=100, blank=True)
    tipo_contato = models.CharField(
        max_length=1, choices=CONTATO, blank=True
    )
    contato = models.CharField(max_length=100, blank=True)
    id_ref =  models.CharField(max_length=100, blank=True)
    ref =  models.CharField(max_length=100, blank=True)
