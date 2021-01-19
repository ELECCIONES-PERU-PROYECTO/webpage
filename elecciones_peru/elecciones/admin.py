from django.contrib import admin
from .models import *

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'carnet_extranjeria',
    'apellido_paterno',
    'apellido_materno',
    'nombres',
    'sexo',
    'fecha_nacimiento',
    'pais_nacimiento',
    'departamento_nacimiento',
    'provincia_nacimiento',
    'distrito_nacimiento',
    'departamento_domicilio',
    'provincia_domicilio',
    'distrito_domicilio',
    'direccion_domicilio',
    'cargo_eleccion',
  )

