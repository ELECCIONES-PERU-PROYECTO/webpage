from django.db import models

class Candidato(models.Model):

  dni = models.CharField(max_length=8, primary_key=True)
  apellido_paterno = models.CharField(max_length=100)
  apellido_materno = models.CharField(max_length=100)
  nombres = models.CharField(max_length=150)
  fecha_nacimiento = models.CharField(max_length=40)
  cargo_postula = models.CharField(max_length=200)
  sexo = models.CharField(max_length=1)
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
  link_foto = models.URLField(max_length=300)

  class Meta(candidato.Meta):
    db_table = 'candidato'

class SentenciaPenal(models.Model):

  n_experiente_penal = models.CharField(max_length=40 primary_key=True)
  fecha_sentencia_firme = models.CharField(max_length=40)
  organo_judicial = models.CharField(max_length=100)
  modalidad_penal = models.CharField(max_length=100) 
  fallo_pena = models.CharField(max_length=120) 
  delito_penal = models.CharField(max_length=120) 
  cumplimiendo_del_fallo = models.TextField()  

  class Meta(sentenciaPenal.Meta):
    db_table = 'sentencia_penal'


class SentenciaCivil(models.Model):

  n_experiente_civil = models.CharField(max_length=40, primary_key=True)
  materia_demanda_civil = models.CharField(max_length=140) 
  organo_judicial = models.CharField(max_length=100) 
  fallo_pena = models.CharField(max_length=120) 

  class Meta(sentenciaCivil.Meta):
    db_table = 'sentencia_civil'


class Renuncia(models.Model):

  n_experiente_civil = models.CharField(max_length=40, primary_key=True)
  materia_demanda_civil = models.CharField(max_length=140) 
  organo_judicial = models.CharField(max_length=100) 
  fallo_pena = models.CharField(max_length=120) 


  class Meta(renuncia.Meta):
    db_table = 'renuncia'


class ExperienciaLaboral(models.Model):

  ruc_empresa_laboral = models.CharField(max_length=30, primary_key=True)
  desde = models.CharField(max_length= 20, primary_key=True)
  hasta = models.CharField(max_length= 20, primary_key=True)
  direccion_laboral = models.CharField(max_length=100)
  pais_laboral = models.CharField(max_length=80)
  departamento_laboral = models.CharField(max_length=80)
  provincia_laboral = models.CharField(max_length=80)
  distrito_laboral = models.CharField(max_length=100)
  centro_laboral = models.CharField(max_length=300)
  oficio = models.CharField(max_length=400)

  class Meta(experienciaLaboral.Meta):
    db_table = 'experiencia_laboral'



class EducacionBasica(models.Model):

  tiene_estudio_primaria = models.CharField(max_length=10)
  concluyo_primaria = models.CharField(max_length=10)
  tiene_estudio_secundaria = models.CharField(max_length=10)
  concluyo_secundaria = models.CharField(max_length=10)

  class Meta(educacionBasica.Meta):
    db_table = 'educacion_basica'



class EstudioTecnico(models.Model):

  tiene_estudio_tecnico = models.CharField(max_length=10)
  concluyo_estudio_tecnico = models.CharField(max_length=10)
  centro_estudio_tecnico = models.CharField(max_length=200)
  carrera_tecnica = models.CharField(max_length=200)
  comentario_estudio_tecnico = models.TextField()

  class Meta(estudioTecnico.Meta):
    db_table = 'estudio_tecnico'



class EstudioUniversitario(models.Model):

  tiene_estudio_universitario = models.CharField(max_length=10)
  concluyo_estudio_universitario = models.CharField(max_length=10)
  centro_estudio_universitario = models.CharField(max_length=200)
  carrera_universitaria = models.CharField(max_length=200)
  grado_universitario = models.CharField(max_length=150)
  es_egresado_universitario = models.CharField(max_length=10)
  anhio_obtencion_universitario = models.CharField(max_length=10)
  comentario_estudio_universitario = models.TextField()

  class Meta(estudioUniversitario.Meta):
    db_table = 'estudio_universitario'



class EstudioNoUniversitario(models.Model):

  tiene_estudio_no_universitario = models.CharField(max_length=10)
  concluyo_estudio_no_universitario = models.CharField(max_length=10)
  centro_estudio_no_universitario = models.CharField(max_length=200)
  carrera_no_universitaria = models.CharField(max_length=200)

  class Meta(estudioNoUniversitario.Meta):
    db_table = 'estudio_no_universitario'


class EstudioPostgrado(models.Model):

  tiene_postgrado = models.CharField(max_length=10)
  centro_estudio_postgrado = models.CharField(max_length=200)
  grado_postgrado = models.CharField(max_length=200)
  concluyo_estudio_postgrado = models.CharField(max_length=10)
  es_maestro = models.CharField(max_length=10)
  comentario_estudio_postgrado = models.TextField()
  es_doctor = models.CharField(max_length=10)
  anhio_obtencion_postgrado = models.CharField(max_length=10) 
  es_egresado_postgrado = models.CharField(max_length=10)

  class Meta(estudioPostgrado.Meta):
    db_table = 'estudio_postgrado'



class InformacionAdicional(models.Model):
  
  tiene_info = models.CharField(max_length=10)
  info = models.TextField()

  class Meta(informacionAdicional.Meta):
    db_table = 'informacion_adicional'



class BienRenta(models.Model):

  total_bien_muebles = models.FloatField(primary_key=True)
  total_ingresos = models.FloatField(primary_key=True)

  class Meta(bienRenta.Meta):
    db_table = 'bien _renta'


class BienInmueble(models.Model):

  esta_inscrito_sunarp = models.CharField(max_length=10)
  tipo_bien = models.CharField(max_length=100)
  direccion_inmueble = models.CharField(max_length=300)
  comentario_inmueble = models.TextField()
  partida_inmueble = models.CharField(max_length=100)
  valor_inmueble = models.FloatField()

  class Meta(bienInmueble.Meta):
    db_table = 'bien_inmueble'


class Vehiculo(models.Model):

  comentario_vehiculo = models.TextField()
  valor = models.FloatField()
  placa_vehiculo = models.CharField(max_length=10)
  caracteristicas_vehiculo = models.TextField()

  class Meta(vehiculo.Meta):
    db_table = 'vehiculo'


class CargoPartidario(models.Model):

  organizacion_politica = models.CharField(max_length=150)
  cargo = models.CharField(max_length=300)
  desde = models.CharField(max_length=20)
  hasta = models.CharField(max_length=20)
  comentario = models.TextField()

  class Meta(cargoPartidario.Meta):
    db_table = 'cargo_partidario'


class CargoEleccionPopular(models.Model):

  organizacion_politica = models.CharField(max_length=150)
  cargo = models.CharField(max_length=300)
  desde = models.CharField(max_length=20)
  hasta = models.CharField(max_length=20)
  comentario = models.TextField()

  class Meta(cargoEleccionPopular.Meta):
    db_table = 'cargo_eleccion_popular'
