from django.db import models


class Colaborador(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Colaborador')

    def __str__(self):
        return self.nome
