from django.db import models

class Candidato(models.Model):
  link_foto = models.URLField(max_length=300)
  dni = models.CharField(max_length=8, primary_key=True)
  sexo = models.CharField(max_length=1)
  apellido_paterno = models.CharField(max_length=100)
  apellido_materno = models.CharField(max_length=100)
  nombres = models.CharField(max_length=150)
  fecha_nacimiento = models.CharField(max_length=40)
  carnet_extranjeria = models.CharField(max_length=12)
  l_n_pais = models.CharField(max_length=80)
  l_n_departamento = models.CharField(max_length=80)
  l_n_provincia = models.CharField(max_length=80)
  l_n_distrito = models.CharField(max_length=100)
  l_d_departamento = models.CharField(max_length=80)
  l_d_provincia = models.CharField(max_length=80)
  l_d_distrito = models.CharField(max_length=100)
  l_d_direccion = models.CharField(max_length=200)
  org_politica_postulate = models.CharField(max_length=100)
  cargo_postula = models.CharField(max_length=200)

  class Meta:
    db_table = 'candidato'


class ExperienciaLaboral(models.Model):
  centro_laboral = models.CharField(max_length=300)
  oficio = models.CharField(max_length=400)
  ruc_empresa_laboral = models.CharField(max_length=30)
  direccion_laboral = models.CharField(max_length=100)
  desde = models.CharField(max_length= 20)
  hasta = models.CharField(max_length= 20)
  pais_laboral = models.CharField(max_length=80)
  departamento_laboral = models.CharField(max_length=80)
  provincia_laboral = models.CharField(max_length=80)

  class Meta:
    db_table = 'experiencia_laboral'
    unique_together = ('ruc_empresa_laboral', 'desde', 'hasta',)


class EducacionBasica(models.Model):
  tiene_estudio_primaria = models.CharField(max_length=10)
  concluyo_primaria = models.CharField(max_length=10)
  tiene_estudio_secundaria = models.CharField(max_length=10)
  concluyo_secundaria = models.CharField(max_length=10)

  class Meta:
    db_table = 'educacion_basica'


class EstudioTecnico(models.Model):
  tiene_estudio_tecnico = models.CharField(max_length=10)
  centro_estudio_tecnico = models.CharField(max_length=200)
  carrera_tecnica = models.CharField(max_length=200)
  concluyo_estudio_tecnico = models.CharField(max_length=10)
  comentario_estudio_tecnico = models.TextField()

  class Meta:
    db_table = 'estudio_tecnico'


class EstudioNoUniversitario(models.Model):
  tiene_estudio_no_universitario = models.CharField(max_length=10)
  centro_estudio_no_universitario = models.CharField(max_length=200)
  carrera_no_universitaria = models.CharField(max_length=200)
  concluyo_estudio_no_universitario = models.CharField(max_length=10)

  class Meta:
    db_table = 'estudio_no_universitario'


class EstudioUniversitario(models.Model):
  tiene_estudio_universitario = models.CharField(max_length=10)
  centro_estudio_universitario = models.CharField(max_length=200)
  concluyo_estudio_universitario = models.CharField(max_length=10)
  grado_universitario = models.CharField(max_length=150)
  es_egresado_universitario = models.CharField(max_length=10)
  anhio_obtencion_universitario = models.CharField(max_length=10)
  comentario_estudio_universitario = models.TextField()
  # Falta atributo
  carrera_universitaria = models.CharField(max_length=200)

  class Meta:
    db_table = 'estudio_universitario'


class EstudioPostgrado(models.Model):
  tiene_postgrado = models.CharField(max_length=10)
  centro_estudio_postgrado = models.CharField(max_length=200)
  grado_postgrado = models.CharField(max_length=200)
  concluyo_estudio_postgrado = models.CharField(max_length=10)
  es_egresado_postgrado = models.CharField(max_length=10)
  es_maestro = models.CharField(max_length=10)
  es_doctor = models.CharField(max_length=10)
  anhio_obtencion_postgrado = models.CharField(max_length=10) 
  comentario_estudio_postgrado = models.TextField()

  class Meta:
    db_table = 'estudio_postgrado'


class Renuncia(models.Model):
  organización_politica_renuncia = models.CharField(max_length=140) 
  anhio_renuncia = models.CharField(max_length=10)
  comentario_renuncia = models.TextField()

  class Meta:
    db_table = 'renuncia'


class SentenciaPenal(models.Model):
  n_experiente_penal = models.CharField(max_length=40 primary_key=True)
  fecha_sentencia_firme = models.CharField(max_length=40)
  organo_judicial = models.CharField(max_length=100)
  delito_penal = models.CharField(max_length=120) 
  fallo_pena = models.CharField(max_length=120) 
  modalidad_penal = models.CharField(max_length=100) 
  cumplimiendo_del_fallo = models.TextField()  

  class Meta:
    db_table = 'sentencia_penal'


class SentenciaCivil(models.Model):
  materia_demanda_civil = models.CharField(max_length=140) 
  n_experiente_civil = models.CharField(max_length=40, primary_key=True)
  organo_judicial = models.CharField(max_length=100) 
  fallo_pena = models.CharField(max_length=120) 

  class Meta:
    db_table = 'sentencia_civil'


# Falta Ingresos here #


class BienInmueble(models.Model):
  numero = models.IntegerField()
  tipo_bien = models.CharField(max_length=100)
  direccion_inmueble = models.CharField(max_length=300)
  esta_inscrito_sunarp = models.CharField(max_length=10)
  partida_inmueble = models.CharField(max_length=100)
  valor_inmueble = models.FloatField()
  comentario_inmueble = models.TextField()

  class Meta:
    db_table = 'bien_inmueble'


# Faltan en el JSON
class CargoPartidario(models.Model):
  organizacion_politica = models.CharField(max_length=150)
  desde = models.CharField(max_length=20)
  hasta = models.CharField(max_length=20)
  cargo = models.CharField(max_length=300)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_partidario'


# Faltan en el JSON
class bienRenta(models.Model):
  total_bien_muebles = models.FloatField()
  total_ingresos = models.FloatField()

  class Meta:
    db_table = 'bien_renta'
    unique_together = ('total_bien_muebles', 'total_ingresos',)


# Falta tabla en JSON
class Vehiculo(models.Model):
  comentario_vehiculo = models.TextField()
  valor = models.FloatField()
  placa_vehiculo = models.CharField(max_length=10)
  caracteristicas_vehiculo = models.TextField()

  class Meta:
    db_table = 'vehiculo'


# Faltan en el JSON
class CargoEleccionPopular(models.Model):
  organizacion_politica = models.CharField(max_length=150)
  cargo = models.CharField(max_length=300)
  desde = models.CharField(max_length=20)
  hasta = models.CharField(max_length=20)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_eleccion_popular'


class InformacionAdicional(models.Model):
  info = models.TextField()

  class Meta:
    db_table = 'informacion_adicional'