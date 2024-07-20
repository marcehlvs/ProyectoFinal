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
]