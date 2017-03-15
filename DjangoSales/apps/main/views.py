from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework import serializers, viewsets, generics, filters
from rest_framework import authentication, permissions
from apps.users.models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView
from .serializers import (ProductoSerializer, UnidadSerializer,
                          EntradasSerializer, ProveedorSerializer, InventarioSerializer,
                          ProductCreateSerializer,ProveedorCreateSerializer
                          )
from .models import (Proveedor, Producto,
                     Unidad, Inventario, Entradas)
import json

class IndexView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect('http://localhost:9000')

class CreateProductView(CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductCreateSerializer

    def create(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(id=request.data['proveedor'])
        unidad = Unidad.objects.get(id=request.data['unidad'])
        entrada = Producto.objects.create(nombre=request.data['nombre'],
                                          upc=request.data['upc'],
                                          unidad=unidad,
                                          proveedor=proveedor,
                                          precio_entrada=request.data[
                                              'precio_entrada'],
                                          precio_salida=request.data['precio_salida'])
        inv = Inventario()
        inv.producto = entrada
        inv.cantidad = 0
        inv.save()
        return Response({"Message":"Producto creado exitosamente."})

class UpdateProductView(UpdateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductCreateSerializer

    def update(self, request, *args, **kwargs):
        updated_instance = Producto.objects.get(pk=request.data["id"])
        proveedor = Proveedor.objects.get(id=request.data["proveedor"])
        unidad = Unidad.objects.get(id=request.data["unidad"])
        updated_instance.upc = request.data['upc']
        updated_instance.nombre = request.data['nombre']
        updated_instance.unidad = unidad
        updated_instance.proveedor = proveedor
        updated_instance.precio_entrada = request.data['precio_entrada']
        updated_instance.precio_salida = request.data['precio_salida']
        updated_instance.save()
        return Response({"Message":"Producto actualizado exitosamente."})

class ProductsListView(ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('upc', 'is_active')

class SingleProductView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class DeleteProductView(DestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductCreateSerializer

class EntriesListView(ListAPIView):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('upc',)

class SingleEntryView(RetrieveAPIView):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer

class UpdateEntryView(UpdateAPIView):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer

    def update(self, request, *args, **kwargs):
        updated_instance = Entradas.objects.get(pk=request.data["id"])
        proveedor = Proveedor.objects.get(id=request.data["proveedor"])
        unidad = Unidad.objects.get(id=request.data["unidad"])
        updated_instance.upc = request.data['upc']
        updated_instance.nombre = request.data['nombre']
        updated_instance.unidad = unidad
        updated_instance.proveedor = proveedor
        updated_instance.precio_entrada = request.data['precio_entrada']
        updated_instance.precio_salida = request.data['precio_salida']
        updated_instance.save()
        return Response({"Message": "Entrada actualizada correctamente."})


class DeleteEntryView(DestroyAPIView):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer


class ProveedorListView(ListAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class SingleProveedorView(RetrieveAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class CreateProveedorView(CreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorCreateSerializer

class DeleteProveedorView(DestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class InventarioListView(ListAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('producto__upc',)

class SingleInventarioView(RetrieveAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class UpdateInventarioView(UpdateAPIView):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()

    def update(self, request, *args, **kwargs):
        if request.data['update'] == True:
            productos = request.data['productos']
            for x in productos:
                updated_instance = Inventario.objects.get(pk=x['id'])
                updated_instance.cantidad = float(
                    updated_instance.cantidad) + float(x['cantidad'])
                updated_instance.save()
                entry = Entradas()
                entry.upc = updated_instance.producto.upc
                entry.nombre = updated_instance.producto.nombre
                entry.proveedor = Proveedor.objects.get(
                    pk=updated_instance.producto.proveedor.id)
                entry.unidad = Unidad.objects.get(
                    pk=updated_instance.producto.unidad.id)
                entry.precio_entrada = updated_instance.producto.precio_entrada
                entry.precio_salida = updated_instance.producto.precio_salida
                entry.cantidad = updated_instance.cantidad
                entry.save()
        else:
            updated_instance = Inventario.objects.get(pk=request.data['id'])
            updated_instance.cantidad = request.data['cantidad']
            updated_instance.save()
        return Response({'Message': 'Producto editado exitosamente'})


class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
