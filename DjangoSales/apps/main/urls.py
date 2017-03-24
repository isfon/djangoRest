from django.conf.urls import url, include
from .views import (
    IndexView, CreateProductView,UpdateProductView,
    ProductsListView, SingleProductView,
    DeleteProductView, EntriesListView,
    SingleEntryView, UpdateEntryView,
    DeleteEntryView, ProveedorListView,
    SingleProveedorView, CreateProveedorView,
    DeleteProveedorView,InventarioListView,
    SingleInventarioView, UpdateInventarioView,
    CategoryProductsListView, SingleCategoryProductView
    )

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='redirect'),
    url(r'^api/products/$', ProductsListView.as_view(), name='products_list'),
    url(r'^api/product/delete/(?P<pk>\d+)/$', DeleteProductView.as_view(), name='delete_product'),
    url(r'^api/product/create/$', CreateProductView.as_view(), name='create_product'),
    url(r'^api/product/update/$', UpdateProductView.as_view(), name='update_product'),
    url(r'^api/product/(?P<pk>\d+)/$', SingleProductView.as_view(), name='single_product'),
    url(r'^api/entries/$', EntriesListView.as_view(), name='enties_list'),
    url(r'^api/entry/(?P<pk>\d+)/$', SingleEntryView.as_view(), name='single_entry'),
    url(r'^api/entry/update/$', UpdateEntryView.as_view(), name='update_entry'),
    url(r'^api/entry/delete/(?P<pk>\d+)/$', DeleteEntryView.as_view(), name='delete_entry'),
    url(r'^api/proveedores/$', ProveedorListView.as_view(), name='proveedor_list'),
    url(r'^api/proveedor/(?P<pk>\d+)/$', SingleProveedorView.as_view(), name='single_proveedor'),
    url(r'^api/proveedor/create/$', CreateProveedorView.as_view(), name='create_proveedor'),
    url(r'^api/proveedor/delete/(?P<pk>\d+)/$', DeleteProveedorView.as_view(), name='delete_proveedor'),
    url(r'^api/inventario/$', InventarioListView.as_view(), name='inventario_list'),
    url(r'^api/inventario/(?P<pk>\d+)/$', SingleInventarioView.as_view(), name='single_inventario'),
    url(r'^api/inventario/update/$', UpdateInventarioView.as_view(), name='update_inventario'),
    url(r'^api/categories/$', CategoryProductsListView.as_view(), name='categories_list'),
    url(r'^api/category/(?P<pk>\d+)/$', SingleCategoryProductView.as_view(), name='single_category'),
]
