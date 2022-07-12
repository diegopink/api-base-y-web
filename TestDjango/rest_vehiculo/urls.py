from django.urls import URLPattern, path
from rest_vehiculo.views import lista_vehiculos

urlpatterns = [
    path('lista_vehiculos', lista_vehiculos, name="lista_vehiculos"),
]