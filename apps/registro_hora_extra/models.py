from django.db import models
from apps.colaboradores.models import Colaborador

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100, help_text='Motivo da Hora Extra')
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
