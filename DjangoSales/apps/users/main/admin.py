from django.contrib import admin
from .models import(
	Proveedor,
	Producto,
	Inventario,
	CatalogoCategoria,
	CatalogoUnidades,
	Entradas
	)

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(CatalogoCategoria)
admin.site.register(CatalogoUnidades)
admin.site.register(Entradas)
