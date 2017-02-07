from django.conf.urls import url, include
from .models import (Proveedor, Producto,
                     Unidad, Inventario, Entradas)
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.response import Response
from rest_framework import filters
from .forms import ProveedorForm


class UnidadSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Unidad
        fields = ('id', 'nombre')


class ProveedorProductosSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('id', 'nombre')


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    unidad = UnidadSerializer()
    proveedor = ProveedorProductosSerializer()

    class Meta:
        model = Producto
        fields = ('id', 'upc', 'proveedor', 'nombre',
                  'unidad', 'precio_entrada', 'precio_salida', 'is_active')


class EntradasSerializer(serializers.HyperlinkedModelSerializer):
    unidad = UnidadSerializer()
    proveedor = ProveedorProductosSerializer()

    class Meta:
        model = Entradas
        fields = ('id', 'upc', 'proveedor', 'nombre', 'unidad',
                  'precio_entrada', 'precio_salida', 'cantidad', 'fecha')


class ProveedorSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Proveedor
        fields = ('id', 'nombre', 'telefono', 'correo', 'direccion')


class InventarioSerializer(serializers.HyperlinkedModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = Inventario
        fields = ('id', 'producto', 'cantidad', 'fecha')
