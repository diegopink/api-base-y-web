from django.urls import URLPattern, path
from rest_vehiculo.views import detalle_vehiculo, lista_vehiculos
from rest_vehiculo.viewslogin import login

urlpatterns = [
    path('lista_vehiculos', lista_vehiculos, name="lista_vehiculos"),
    path('detalle_vehiculo/<id>', detalle_vehiculo, name="detalle_vehiculo"),
    path('login', login, name="login"),
]