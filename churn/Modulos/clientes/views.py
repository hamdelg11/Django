from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Clientes
# Create your views here.

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoClientes(ListView):
    model = Clientes
    template_name = 'clientes/listado_clientes.html'
    context_object_name = 'clientes'

