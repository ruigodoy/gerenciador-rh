from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.departamentos.models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.colaborador.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCriar(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.colaborador.empresa
        departamento.save()

        return super(DepartamentoCriar, self).form_valid(form)


class DepartamentoAtualizar(UpdateView):
    model = Departamento
    fields = ['nome']


class DepartamentoDeletar(DeleteView):
    model = Departamento
    fields = ['nome']
    success_url = reverse_lazy('listar_departamentos')