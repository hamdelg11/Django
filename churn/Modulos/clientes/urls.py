from django.urls import path
from .views import *

urlpatterns= [ 
    path('listar_cliente/',ListadoClientes.as_view(), name = 'listar_cliente'),

]