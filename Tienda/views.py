from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import *
from Tienda.models import *

#decorators and mixin

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


#login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

#cambiarPassword

from django.contrib.auth.views import PasswordChangeView



# Create your views here.

def home(request):
    return render(request, 'Tienda/index.html')


#__ Importo para ver productos en el index
class IndexView(ListView):
    model = Producto
    template_name = 'Tienda/index.html'
    context_object_name = 'productos'

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
    fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'categoria', 'imagen_url']
    success_url = reverse_lazy("productos")

class ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'categoria', 'imagen_url']
    success_url = reverse_lazy("productos")


class ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")

class ProductoDetail(DetailView):
    model = Producto
    template_name = 'Tienda/producto_detail.html'
    context_object_name = 'producto'

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


#__ Pedidos

class PedidoList(ListView):
    model = Pedido
    template_name = 'Tienda/pedidos_list'
    context_object_name = 'pedidos'

class PedidoCreate(LoginRequiredMixin, CreateView):
    model = Pedido
    fields = ['productos']
    success_url = reverse_lazy("pedidos")

class PedidoUpdate(LoginRequiredMixin, UpdateView):
    model = Pedido
    fields = ['productos']
    success_url = reverse_lazy("pedidos")
class PedidoDelete(LoginRequiredMixin, DeleteView):
    model = Pedido
    success_url = reverse_lazy("pedidos")



#login-logout-registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #__ buscarAvatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session['avatar'] = avatar
            #_______________


            return redirect('home')  # Redirige a la vista 'home' que es IndexView
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
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

#__Edit profile

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "Tienda/editarPerfil.html", {"form": miForm})

#__cambiarClave

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
	template_name="Tienda/cambiar_clave.html"
	success_url = reverse_lazy("home")

#__Avatar

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #___borrar avatar viejo
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #___________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #___Envía la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy('home'))
    else:
        miForm = AvatarForm()
    return render(request, "Tienda/agregarAvatar.html", {"form": miForm})

