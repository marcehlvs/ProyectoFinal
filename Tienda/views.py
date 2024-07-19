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
    template_name = 'Tienda/producto_list.html'
    context_object_name = 'productos'

    def get_queryset(self):
        queryset = super().get_queryset()
        buscar = self.request.GET.get('buscar', None)
        if buscar:
            queryset = queryset.filter(nombre__icontains=buscar)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['buscar'] = self.request.GET.get('buscar', '')
        return context

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
