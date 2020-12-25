from django.urls import path
from .views import DepartamentosList, DepartamentoCriar, DepartamentoAtualizar, DepartamentoDeletar


urlpatterns = [
    path('list', DepartamentosList.as_view(), name='listar_departamentos'),
    path('novo', DepartamentoCriar.as_view(), name='criar_departamento'),
    path('atualizar/<int:pk>/', DepartamentoAtualizar.as_view(), name='atualizar_departamento'),
    path('deletar/<int:pk>/', DepartamentoDeletar.as_view(), name='deletar_departamento'),
]
