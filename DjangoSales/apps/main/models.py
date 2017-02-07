from django.db import models
from datetime import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Unidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Catalogo Unidad"
        verbose_name_plural = "Catalogo Unidades"

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):

    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField(null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.nombre


class Producto(models.Model):

    upc = models.BigIntegerField(null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=50)
    proveedor = models.ForeignKey(Proveedor)
    unidad = models.ForeignKey(Unidad)
    precio_entrada = models.FloatField(default=0)
    precio_salida = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.nombre


class Inventario(models.Model):

    producto = models.ForeignKey(Producto)
    cantidad = models.FloatField(default=0)
    fecha = models.DateTimeField(default=date.today, null=True)

    def __str__(self):
        return '%s' % self.producto


class Entradas(models.Model):

    upc = models.BigIntegerField(null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=50, null=True, blank=True)
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True)
    unidad = models.ForeignKey(Unidad, null=True, blank=True)
    precio_entrada = models.FloatField(default=0)
    precio_salida = models.FloatField(default=0)
    cantidad = models.FloatField(default=0)
    fecha = models.DateField(default=date.today, null=True)

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.nombre


class Venta(models.Model):

    fecha = models.DateTimeField()
    usuario = models.CharField(max_length=50)
    total_compra = models.FloatField(default=0)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % self.usuario


class DescripcionVenta(models.Model):

    venta = models.ForeignKey(Venta)
    producto = models.CharField(max_length=50)
    cantidad = models.FloatField(default=0)
    precio_unitario = models.FloatField(default=0)

    class Meta:
        verbose_name = "DescripcionVenta"
        verbose_name_plural = "DescripcionVentas"

    def __str__(self):
        return self.producto
