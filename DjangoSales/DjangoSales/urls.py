from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework import routers
from apps.users.serializers import TokenViewSet
from apps.main.serializers import (
	ProductoViewSet, ProveedorViewSet,
	CategoriarViewSet, InventarioViewSet,
	UnidadViewSet, EntradasViewSet
	)

router = routers.DefaultRouter()
router.register(r'userdata', TokenViewSet, 'User')
router.register(r'productos', ProductoViewSet)
router.register(r'proveedores', ProveedorViewSet)
router.register(r'categorias', CategoriarViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'unidades', UnidadViewSet)
router.register(r'entradas', EntradasViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
]
