from django.urls import path

from apps.empresas.views import EmpresaCriar, EmpresaEditar

urlpatterns = [
    path('novo', EmpresaCriar.as_view(), name='criar_empresa'),
    path('editar/<int:pk>/', EmpresaEditar.as_view(), name='editar_empresa'),
]
