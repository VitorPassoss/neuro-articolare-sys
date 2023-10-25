from django.db import models


GENERO = [("F", "Feminino"), ("M", "Masculino"), ("O", "Outro")]


class Pacientes(models.Model):
    nome = models.CharField(max_length=155)
    celular = models.CharField(max_length=155)
    dt_nasc = models.DateTimeField(auto_now_add=True, null=True)
    cpf = models.CharField(max_length=155)
    cidade =  models.CharField(max_length=155) 
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    genero =  models.CharField(
        max_length=2, choices=GENERO
    )

    class Meta: 
        ordering = ['-created_at'] 