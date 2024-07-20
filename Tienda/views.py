from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import *
from Tienda.models import *

#decorators and mixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm


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

class ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen_url']
    success_url = reverse_lazy("productos")

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'categoria', 'imagen_url']
    success_url = reverse_lazy("productos")


class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")

#__ Categoria

class CategoriaList(ListView):
    model = Categoria


class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields= ['nombre']
    success_url = reverse_lazy("categorias")

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nombre']
    success_url = reverse_lazy("categorias")


class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    success_url = reverse_lazy("categorias")


#login-logout-registration

def loginRequest(request):
    if request.method == "POST":  # Ya llego la información.
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "Tienda/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()  # Creo formulario vacio
    return render(request, "Tienda/login.html", {"form": miForm})


#registrate

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()
    return render(request, "Tienda/registro.html", {"form": miForm})
