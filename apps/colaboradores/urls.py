from django.urls import path

from apps.colaboradores.views import ColaboradoresListar, ColaboradorEditar

urlpatterns = [
    path('', ColaboradoresListar.as_view(), name='listar_colaboradores'),
    path('editar/<int:pk>/', ColaboradorEditar.as_view(), name='atualizar_colaborador'),
]
