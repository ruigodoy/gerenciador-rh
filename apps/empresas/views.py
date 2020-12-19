from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView

from apps.empresas.models import Empresa


class EmpresaCriar(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        objeto = form.save()
        colaborador = self.request.user.colaborador
        colaborador.empresa = objeto
        colaborador.save()
        return HttpResponse('Ok')


class EmpresaEditar(UpdateView):
    model = Empresa
    fields = ['nome']