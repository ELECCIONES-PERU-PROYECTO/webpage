from django.contrib import admin
from .models import *

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

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'centro_laboral',
    'oficio',
    'ruc_empresa_laboral',
    'direccion_laboral',
    'desde',
    'hasta',
    'pais_laboral',
    'departamento_laboral',
    'provincia_laboral',
  )

@admin.register(EducacionBasica)
class EducacionBasicaAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'tiene_estudio_primaria',
    'concluyo_primaria',
    'tiene_estudio_secundaria',
    'concluyo_secundaria',
  )

@admin.register(EstudioTecnico)
class EstudioTecnicoAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'tiene_estudio_tecnico',
    'centro_estudio_tecnico',
    'carrera_tecnica',
    'concluyo_estudio_tecnico',
    'comentario_estudio_tecnico',
  )

@admin.register(EstudioNoUniversitario)
class EstudioNoUniversitarioAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'tiene_estudio_no_universitario',
    'centro_estudio_no_universitario',
    'carrera_no_universitaria',
    'concluyo_estudio_no_universitario',
  )

@admin.register(EstudioUniversitario)
class EstudioUniversitarioAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'tiene_estudio_universitario',
    'centro_estudio_universitario',
    'concluyo_estudio_universitario',
    'grado_universitario',
    'es_egresado_universitario',
    'anhio_obtencion_universitario',
    'comentario_estudio_universitario',
  )

@admin.register(EstudioPostgrado)
class EstudioPostgradoAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'tiene_postgrado',
    'centro_estudio_postgrado',
    'grado_postgrado',
    'concluyo_estudio_postgrado',
    'es_egresado_postgrado',
    'es_maestro',
    'es_doctor',
    'anhio_obtencion_postgrado',
    'comentario_estudio_postgrado',
  )

@admin.register(CargoPartidario)
class CargoPartidarioAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'organizacion_politica',
    'cargo',
    'desde',
    'hasta',
    'comentario',
  )

@admin.register(CargoEleccionPopular)
class CargoEleccionPopularAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'organizacion_politica',
    'cargo',
    'desde',
    'hasta',
    'comentario',
  )

@admin.register(Renuncia)
class RenunciaAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'organización_politica',
    'anhio',
    'comentario',
  )

@admin.register(SentenciaPenal)
class SentenciaPenalAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'n_experiente_penal',
    'fecha_sentencia_firme',
    'organo_judicial',
    'delito_penal',
    'fallo_pena',
    'modalidad_penal',
    'cumplimiendo_del_fallo',
  )

@admin.register(SentenciaCivil)
class SentenciaCivilAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'materia_demanda_civil',
    'n_experiente_civil',
    'organo_judicial',
    'fallo_pena',
  )

@admin.register(BienRenta)
class BienRentaAdmin(admin.ModelAdmin):
  list_display = (
    'anhio',
    'total_bien_muebles',
    'total_ingresos',
  )

@admin.register(BienInmueble)
class BienInmuebleAdmin(admin.ModelAdmin):
  list_display = (
    'total_ingresos',
    'numero',
    'tipo_bien',
    'direccion_inmueble',
    'esta_inscrito_sunarp',
    'partida_inmueble',
    'valor_inmueble',
    'comentario_inmueble',
  )

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
  list_display = (
    'total_bien_muebles',
    'total_ingresos',
    'numero',
    'vehiculo',
    'placa_vehiculo',
    'caracteristicas_vehiculo',
    'valor',
    'comentario_vehiculo',
  )

@admin.register(InformacionAdicional)
class InformacionAdicionalAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
    'info',
  )

@admin.register(TieneInfoA)
class TieneInfoAAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
  )

@admin.register(TieneBR)
class TieneBRAdmin(admin.ModelAdmin):
  list_display = (
    'dni_candidato',
  )
