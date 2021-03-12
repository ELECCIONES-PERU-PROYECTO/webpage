from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export import resources
class DatosPersonalesResource(resources.ModelResource):
  from .models import DatosPersonales
  class Meta:
    model = DatosPersonales

@admin.register(DatosPersonales)
class DatosPersonalesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = DatosPersonalesResource
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

class ExperienciaLaboralResource(resources.ModelResource):
  from .models import ExperienciaLaboral
  class Meta:
    model = ExperienciaLaboral
@admin.register(ExperienciaLaboral)
class ExperienciaLaboralAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = ExperienciaLaboralResource
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
  list_filter = (
    'id',
  )
class EducacionBasicaResource(resources.ModelResource):
  from .models import EducacionBasica
  class Meta:
    model = EducacionBasica

@admin.register(EducacionBasica)
class EducacionBasicaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = EducacionBasicaResource
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

class EstudioTecnicoResource(resources.ModelResource):
  from .models import EstudioTecnico
  class Meta:
    model = EstudioTecnico

@admin.register(EstudioTecnico)
class EstudioTecnicoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = EstudioTecnicoResource
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

class RenunciaResource(resources.ModelResource):
  from .models import Renuncia

  class Meta:
    model = Renuncia

@admin.register(Renuncia)
class RenunciaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  list_display = (
    'organizacion_politica',
    'distrito_elec',
    'dni_candidato',
    'candidato',
    'tiene_info_por_declarar',
    'organización_renuncia',
    'comentario',
  )
  list_filter = (
    'id',
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


class BienInmuebleResource(resources.ModelResource):
  from .models import BienInmueble

  class Meta:
    model = BienInmueble

@admin.register(BienInmueble)
class BienInmuebleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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
  list_filter = (
    'id',
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
from .models import FinanciamientoPrivado, FinanciamientoPublico
@admin.register(FinanciamientoPrivado)
class FinanciamientoPrivadoAdmin(admin.ModelAdmin):
  pass

@admin.register(FinanciamientoPublico)
class FinanciamientoPublicoAdmin(admin.ModelAdmin):
  pass

class TablaEdadResource(resources.ModelResource):
  from .models import TablaEdad

  class Meta:
    model = TablaEdad

@admin.register(TablaEdad)  

class TablaEdadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = TablaEdadResource
  list_display = (
    'edad',
    'organizacion_politica',
    'dni_candidato',
    'id',
  )

  list_filter = (
    'edad',
  )


class OrganizacionesPoliticasResource(resources.ModelResource):
  from .models import OrganizacionesPoliticas

  class Meta:
    model = OrganizacionesPoliticas

@admin.register(OrganizacionesPoliticas)  

class OrganizacionesPoliticasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
  resource_class = OrganizacionesPoliticasResource
  list_display = (
    'organizacion_politica',
    'url',
  )