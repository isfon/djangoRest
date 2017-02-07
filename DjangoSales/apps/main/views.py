from django.views.generic import TemplateView
from django.shortcuts import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, viewsets, generics, filters
from rest_framework import authentication, permissions
from apps.users.models import User
from .serializers import (ProductoSerializer, UnidadSerializer,
                          EntradasSerializer, ProveedorSerializer, InventarioSerializer)
from .models import (Proveedor, Producto,
                     Unidad, Inventario, Entradas)
import json


class IndexView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        return HttpResponseRedirect('http://localhost:9000')


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('upc', 'is_active')

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
        return Response({'producto': entrada.nombre})

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
        return Response({'producto': updated_instance.nombre})


class EntradasViewSet(viewsets.ModelViewSet):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('upc',)

    def create(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(id=request.data['proveedor'])
        unidad = Unidad.objects.get(id=request.data['unidad'])
        entrada = Entradas.objects.create(nombre=request.data['nombre'],
                                          upc=request.data['upc'],
                                          unidad=unidad,
                                          categoria=categoria,
                                          proveedor=proveedor,
                                          cantidad=request.data['cantidad'],
                                          fecha=request.data['fecha'],
                                          precio_entrada=request.data[
                                              'precio_entrada'],
                                          precio_salida=request.data['precio_salida'])
        return Response({'producto': entrada.nombre})

    def update(self, request, *args, **kwargs):
        updated_instance = Entradas.objects.get(pk=request.data["id"])
        proveedor = Proveedor.objects.get(id=request.data["proveedor"])
        unidad = Unidad.objects.get(id=request.data["unidad"])
        updated_instance.upc = request.data['upc']
        updated_instance.nombre = request.data['nombre']
        updated_instance.unidad = unidad
        updated_instance.categoria = categoria
        updated_instance.proveedor = proveedor
        updated_instance.precio_entrada = request.data['precio_entrada']
        updated_instance.precio_salida = request.data['precio_salida']
        updated_instance.cantidad = request.data['cantidad']
        updated_instance.fecha = request.data['fecha']
        updated_instance.save()
        return Response({'producto': updated_instance.nombre})


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('producto__upc',)

    def update(self, request, *args, **kwargs):
        updated_instance = Inventario.objects.get(pk=request.data['id'])
        if(request.data['update'] == True):
            updated_instance.cantidad = float(
                updated_instance.cantidad) + float(request.data['cantidad'])
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
            updated_instance.cantidad = request.data['cantidad']
            print(request.data['cantidad'])
        updated_instance.save()
        return Response({'producto': updated_instance.producto.nombre})


class UnidadViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadSerializer
