from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from Tienda.models import *


# Create your views here.

def home(request):
    return render(request, 'Tienda/index.html')

#__ Producto

class ProductoList(ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen_url']
    success_url = reverse_lazy("productos")

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen_url']
    success_url = reverse_lazy("productos")

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")

#__ Categoria

class CategoriaList(ListView):
    model = Categoria
class CategoriaCreate(CreateView):
    model = Categoria
    fields= ['nombre']
    success_url = reverse_lazy("categorias")

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nombre']
    success_url = reverse_lazy("categorias")

class CategoriaDelete(DeleteView):
    model = Categoria
    success_url = reverse_lazy("categorias")
