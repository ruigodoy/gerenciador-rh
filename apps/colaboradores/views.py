from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (ListView,
                                  UpdateView,
                                  DeleteView,
                                  CreateView
                                  )

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


class ColaboradorCriar(CreateView):
    model = Colaborador
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        colaborador = form.save(commit=False)
        username = colaborador.nome.split(' ')[0] + colaborador.nome.split(' ')[1]
        colaborador.empresa = self.request.user.colaborador.empresa
        colaborador.user = User.objects.create(username=username)
        colaborador.save()

        return super(ColaboradorCriar, self).form_valid(form)

