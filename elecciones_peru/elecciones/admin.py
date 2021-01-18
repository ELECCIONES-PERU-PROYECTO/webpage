from django.contrib import admin
from .models import Candidato, ExperienciaLaboral

@admin.register(Candidato)
class CandidatpAdmin(admin.ModelAdmin):
  list_display = (
    'link_foto',
    'dni',
    'sexo',
    'apellido_paterno',
    'apellido_materno',
    'nombres',
    'fecha_nacimiento',
    'carnet_extranjeria',
    'l_n_pais',
    'l_n_departamento',
    'l_n_provincia',
    'l_n_distrito',
    'l_d_departamento',
    'l_d_provincia',
    'l_d_distrito',
    'l_d_direccion',
    'org_politica_postulate',
    'cargo_postula',
  )