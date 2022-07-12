from django.urls import path
from .views import form_del_vehiculo, form_vehiculo, home,form_mod_vehiculo

urlpatterns = [
    path('', home,name="home"),
    path('form-vehiculo', form_vehiculo, name="form_vehiculo"),
    path('form-mod-vehiculo/<id>' , form_mod_vehiculo, name="form_mod_vehiculo"),
    path('form-delvehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),
]
