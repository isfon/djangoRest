from django.conf.urls import url, include
from .models import CatalogoCategoria, Proveedor, Producto, CatalogoUnidades, Inventario, Entradas
from rest_framework import routers, serializers, viewsets, generics
from rest_framework.response import Response
from rest_framework import filters

class UnidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogoUnidades
        fields = ('id','nombre')

class UnidadViewSet(viewsets.ModelViewSet):
    queryset = CatalogoUnidades.objects.all()
    serializer_class = UnidadSerializer

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CatalogoCategoria
        fields = ('id','nombre')

class CategoriarViewSet(viewsets.ModelViewSet):
	queryset = CatalogoCategoria.objects.all()
	serializer_class = CategoriaSerializer

class ProveedorProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id','nombre')

# Serializers define the API representation.
class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    #serializers.PrimaryKeyRelatedField(source='proveedor.nombre', queryset=Proveedor.objects.all())
    categoria = CategoriaSerializer()
    unidad = UnidadSerializer()
    proveedor = ProveedorProductosSerializer()

    class Meta:
        model = Producto
        fields = ('id', 'upc', 'proveedor', 'nombre', 'categoria', 'unidad','precio_entrada','precio_salida', 'is_active')

# ViewSets define the view behavior.
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('upc','is_active')

    def create(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(id=request.data['proveedor'])
        categoria = CatalogoCategoria.objects.get(id=request.data['categoria'])
        unidad = CatalogoUnidades.objects.get(id=request.data['unidad'])
        entrada = Producto.objects.create(nombre=request.data['nombre'],
            upc=request.data['upc'],
            unidad=unidad,
            categoria=categoria,
            proveedor=proveedor,
            precio_entrada=request.data['precio_entrada'],
            precio_salida=request.data['precio_salida'])
        inv = Inventario()
        inv.producto = entrada
        inv.cantidad = 0
        inv.save()
        return Response({'producto':entrada.nombre})

    def update(self, request, *args, **kwargs):
        updated_instance = Producto.objects.get(pk=request.data["id"])
        proveedor = Proveedor.objects.get(id=request.data["proveedor"])
        unidad = CatalogoUnidades.objects.get(id=request.data["unidad"])
        categoria = CatalogoCategoria.objects.get(id=request.data["categoria"])
        updated_instance.upc=request.data['upc']
        updated_instance.nombre=request.data['nombre']
        updated_instance.unidad=unidad
        updated_instance.categoria=categoria
        updated_instance.proveedor=proveedor
        updated_instance.precio_entrada=request.data['precio_entrada']
        updated_instance.precio_salida=request.data['precio_salida']
        updated_instance.save()
        return Response({'producto':updated_instance.nombre})


class EntradasSerializer(serializers.HyperlinkedModelSerializer):
    #serializers.PrimaryKeyRelatedField(source='proveedor.nombre', queryset=Proveedor.objects.all())
    categoria = CategoriaSerializer()
    unidad = UnidadSerializer()
    proveedor = ProveedorProductosSerializer()

    class Meta:
        model = Entradas
        fields = ('id', 'upc', 'proveedor', 'nombre', 'categoria', 'unidad','precio_entrada','precio_salida', 'cantidad', 'fecha')

# ViewSets define the view behavior.
class EntradasViewSet(viewsets.ModelViewSet):
    queryset = Entradas.objects.all()
    serializer_class = EntradasSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('upc',)

    def create(self, request, *args, **kwargs):
        proveedor = Proveedor.objects.get(id=request.data['proveedor'])
        categoria = CatalogoCategoria.objects.get(id=request.data['categoria'])
        unidad = CatalogoUnidades.objects.get(id=request.data['unidad'])
        entrada = Entradas.objects.create(nombre=request.data['nombre'],
            upc=request.data['upc'],
            unidad=unidad,
            categoria=categoria,
            proveedor=proveedor,
            cantidad=request.data['cantidad'],
            fecha=request.data['fecha'],
            precio_entrada=request.data['precio_entrada'],
            precio_salida=request.data['precio_salida'])
        return Response({'producto':entrada.nombre})

    def update(self, request, *args, **kwargs):
        updated_instance = Entradas.objects.get(pk=request.data["id"])
        proveedor = Proveedor.objects.get(id=request.data["proveedor"])
        unidad = CatalogoUnidades.objects.get(id=request.data["unidad"])
        categoria = CatalogoCategoria.objects.get(id=request.data["categoria"])
        updated_instance.upc=request.data['upc']
        updated_instance.nombre=request.data['nombre']
        updated_instance.unidad=unidad
        updated_instance.categoria=categoria
        updated_instance.proveedor=proveedor
        updated_instance.precio_entrada=request.data['precio_entrada']
        updated_instance.precio_salida=request.data['precio_salida']
        updated_instance.cantidad=request.data['cantidad']
        updated_instance.fecha=request.data['fecha']
        updated_instance.save()
        return Response({'producto':updated_instance.nombre})

class ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proveedor
        fields = ('id','nombre','telefono','correo','direccion')

class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

class InventarioSerializer(serializers.HyperlinkedModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = Inventario
        fields = ('id', 'producto', 'cantidad')

class InventarioViewSet(viewsets.ModelViewSet):
    serializer_class = InventarioSerializer
    queryset = Inventario.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('producto__upc',)

    def update(self, request, *args, **kwargs):
        updated_instance = Inventario.objects.get(pk=request.data['id'])
        if(request.data['update'] == True):
            updated_instance.cantidad = float(updated_instance.cantidad) + float(request.data['cantidad'])
            entry = Entradas()
            entry.upc = updated_instance.producto.upc
            entry.nombre = updated_instance.producto.nombre
            entry.proveedor = Proveedor.objects.get(pk = updated_instance.producto.proveedor.id)
            entry.categoria = CatalogoCategoria.objects.get(pk = updated_instance.producto.categoria.id)
            entry.unidad = CatalogoUnidades.objects.get(pk = updated_instance.producto.unidad.id)
            entry.precio_entrada = updated_instance.producto.precio_entrada
            entry.precio_salida = updated_instance.producto.precio_salida
            entry.cantidad = updated_instance.cantidad
            entry.save()
        else:
            updated_instance.cantidad = request.data['cantidad']
            print(request.data['cantidad'])
        updated_instance.save()
        return Response({'producto':updated_instance.producto.nombre})
