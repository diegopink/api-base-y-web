from unicodedata import category
from django.contrib import admin
from .models import Categoria, Vehiculo

# Register your models here.
#permite administrar el modelo completo

admin.site.register(Categoria)
admin.site.register(Vehiculo)