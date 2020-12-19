from django.views.generic import ListView, UpdateView

from apps.colaboradores.models import Colaborador


class ColaboradoresListar(ListView):
    model = Colaborador

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Colaborador.objects.filter(empresa=empresa_logada)


class ColaboradorEditar(UpdateView):
    model = Colaborador
    fields = ['nome', 'departamentos']