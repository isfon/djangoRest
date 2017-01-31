from django import forms
from .models import (
    Proveedor, Producto, Entradas
)
from django.utils import six


class ProveedorForm():
    nombre = forms.CharField(widget=forms.TextInput(attrs={
                             'class': 'form-control'}), error_messages={'required': 'Please let us know what to call you!'})
    direccion = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), error_messages={'required': 'Please let us know what to call you!'})
    telefono = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}), error_messages={'required': 'Please let us know what to call you!'})
    correo = forms.CharField(widget=forms.TextInput(attrs={
                             'class': 'form-control'}), error_messages={'required': 'Please let us know what to call you!'})

    class Meta:
        model = Proveedor
        fields = ('nombre', 'telefono', 'correo', 'direccion')

        def __init__(self, *args, **kwargs):
            form = super(ProveedorForm, self).__init__(*args, **kwargs)
            for visible in form.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


class ProductoForm():

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = ' '
            field.widget.attrs['class'] = 'form-control border-input'

    class Meta:
        model = Producto
        fields = ('upc', 'proveedor', 'nombre', 'categoria',
                  'unidad', 'precio_entrada', 'precio_salida')


class EntradasForm():

    def __init__(self, *args, **kwargs):
        super(EntradasForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['required'] = ' '
            field.widget.attrs['class'] = 'form-control border-input'

    class Meta:
        model = Entradas
        fields = ('upc', 'proveedor', 'nombre', 'categoria', 'unidad',
                  'precio_entrada', 'precio_salida', 'cantidad', 'fecha')
