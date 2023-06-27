from django.urls import path
from . import views

urlpatterns = [
    path('',views.cargarInicio, name='home'),
    path('clima',views.cargarClima),
    path('agregarProducto', views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('registrarse',views.signup, name='signup'),
    path('iniciarSesion',views.signin, name='signin'),
    path('cerrarSesion',views.signout, name='logout'),
    path('carrito',views.carrito)

]