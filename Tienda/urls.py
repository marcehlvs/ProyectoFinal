from django.urls import path, include
from Tienda.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    #path('', home, name='home'),

    #___ productos

    path('productos/', ProductoList.as_view(), name='productos'),
    path('productoCreate/', ProductoCreate.as_view(), name='productoCreate'),
    path('productoUpdate/<int:pk>/', ProductoUpdate.as_view(), name='productoUpdate'),
    path('productoDelete/<int:pk>/', ProductoDelete.as_view(), name='productoDelete'),
    path('productoDetail/<int:pk>/', ProductoDetail.as_view(), name='productoDetail'),

    #___ categorias

    path('categorias/', CategoriaList.as_view(), name='categorias'),
    path('categoriaCreate/', CategoriaCreate.as_view(), name='categoriaCreate'),
    path('cateogoriaUpdate/<int:pk>/', CategoriaUpdate.as_view(), name='categoriaUpdate'),
    path('categoriaDelete/<int:pk>/', CategoriaDelete.as_view(), name='categoriaDelete'),

    #___ pedidos


    #___ login

    path('login/', loginRequest, name='login'),

    #___ logout con cbv
    path('logout/', LogoutView.as_view(template_name="Tienda/logout.html"), name='logout'),

    #__ registro
    path('registro/', register, name='registro'),

    #__editProfile

    path('perfil/', editProfile, name="perfil"),

    #__formularioPassword

    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),

    #__agregarAvatar
    path('agregar_avatar/', agregarAvatar, name='agregar_avatar'),

    #__pedidos

    path('pedidos/', PedidoList.as_view(), name='pedidos'),
    path('pedidoCreate/', PedidoCreate.as_view(), name='pedidoCreate'),
    path('pedidoUpdate/<int:pk>/', PedidoUpdate.as_view(), name='pedidoUpdate'),
    path('pedidoDelete/<int:pk>/', PedidoDelete.as_view(), name='pedidoDelete'),

]