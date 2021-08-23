
from django.contrib import admin
from django.urls import path, include
from Modulos.clientes.views import Inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Inicio.as_view(), name = 'index'),
    path('clientes/',include(('Modulos.clientes.urls','clientes'))),
]
