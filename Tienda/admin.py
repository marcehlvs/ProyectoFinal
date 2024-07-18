from django.contrib import admin

# Register your models here.

from .models import Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "precio", "categoria")
    list_filter = ("categoria",)

class CategoriaAdmin(admin.ModelAdmin):
    list_filter = ("nombre",)

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Categoria, CategoriaAdmin)



