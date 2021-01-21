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

  list_filter = (
    'organizacion_politica',
    'sexo',
    'pais_nacimiento',
    'cargo_eleccion',
  )

@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_experiencia_laboral',
    'centro_laboral',
    'ocupacion',
    'ruc_empresa_laboral',
    'direccion_laboral',
    'desde_anhio',
    'hasta_anhio',
    'pais_laboral',
    'departamento_laboral',
    'provincia_laboral',
    'distrito_laboral',
  )

@admin.register(EducacionBasica)
class EducacionBasicaAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_educacion_basica',
    'tiene_estudio_primaria',
    'concluyo_primaria',
    'tiene_estudio_secundaria',
    'concluyo_secundaria',
  )

@admin.register(EstudioTecnico)
class EstudioTecnicoAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_estudio_tecnico',
    'centro_estudio_tecnico',
    'carrera_tecnica',
    'concluyo_estudio_tecnico',
    'comentario_estudio_tecnico',
  )

@admin.register(EstudioNoUniversitario)
class EstudioNoUniversitarioAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_estudio_no_universitario',
    'centro_estudio_no_universitario',
    'carrera_no_universitaria',
    'concluyo_estudio_no_universitario',
  )

@admin.register(EstudioUniversitario)
class EstudioUniversitarioAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_estudio_universitario',
    'universidad',
    'carrera_universitaria',
    'concluyo_estudio_universitario',
    'es_egresado_universitario',
    'anhio_obtencion_universitario',
    'comentario_estudio_universitario',
  )

@admin.register(EstudioPostgrado)
class EstudioPostgradoAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_postgrado',
    'centro_estudio_postgrado',
    'especialidad',
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
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_cargo_partidario',
    'org_politica_cargo',
    'cargo',
    'desde_anhio',
    'hasta_anhio',
    'comentario',
  )

@admin.register(CargoEleccion)
class CargoEleccionAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_info_por_declarar',
    'org_politica_cargo',
    'desde_anhio',
    'hasta_anhio',
    'cargo',
    'comentario',
  )

@admin.register(Renuncia)
class RenunciaAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_info_por_declarar',
    'organización_renuncia',
    'comentario',
  )

@admin.register(SentenciaPenal)
class SentenciaPenalAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_info_por_declarar',
    'n_experiente_penal',
    'fecha_sentencia_penal',
    'organo_judicial',
    'delito_penal',
    'fallo_penal',
    'modalidad_penal',
    'otra_modalidad',
    'cumplimiento_del_fallo',
  )

@admin.register(SentenciaObligacion)
class SentenciaObligacionAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_info_por_declarar',
    'materia_sentencia',
    'n_experiente_obliga',
    'organo_judicial',
    'fallo_obliga',
  )

@admin.register(Ingreso)
class IngresoAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_ingresos',
    'anhio_ingresos',
    'total_ingresos',
  )

@admin.register(BienInmueble)
class BienInmuebleAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_inmueble',
    'tipo_inmueble',
    'direccion_inmueble',
    'esta_inscrito_sunarp',
    'partida_inmueble_sunarp',
    'autovaluo',
    'comentario_inmueble',
  )

@admin.register(BienMueble)
class BienMuebleAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_bien_mueble',
    'vehiculo',
    'placa',
    'valor',
    'caracteristicas_vehiculo',
    'comentario_vehiculo',
  )

@admin.register(InformacionAdicional)
class InformacionAdicionalAdmin(admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_info_adicional',
    'info',
  )
