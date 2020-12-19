from django.urls import path

from apps.colaboradores.views import home

urlpatterns = [
    path('', home),
]
