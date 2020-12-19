from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.colaboradores.models import Colaborador


class ColaboradoresListar(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)


class ColaboradorEditar(UpdateView):
    model = Colaborador
    fields = ['nome', 'departamentos']


class ColaboradorDeletar(DeleteView):
    model = Colaborador
    success_url = reverse_lazy('listar_colaboradores')
