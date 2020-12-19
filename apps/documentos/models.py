from django.db import models
from apps.colaboradores.models import Colaborador


class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do Documento')
    dono_documento = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
