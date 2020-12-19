from django.urls import path

from apps.colaboradores.views import (ColaboradoresListar,
                                      ColaboradorEditar,
                                      ColaboradorDeletar,
                                      ColaboradorCriar
                                      )

urlpatterns = [
    path('', ColaboradoresListar.as_view(), name='listar_colaboradores'),
    path('editar/<int:pk>/', ColaboradorEditar.as_view(), name='atualizar_colaborador'),
    path('deletar/<int:pk>/', ColaboradorDeletar.as_view(), name='deletar_colaborador'),
    path('novo/', ColaboradorCriar.as_view(), name='criar_colaborador'),
]
