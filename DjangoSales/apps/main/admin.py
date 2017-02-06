from django.contrib import admin
from .models import(
    Proveedor,
    Producto,
    Inventario,
    Unidad,
    Entradas
)

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Unidad)
admin.site.register(Entradas)
