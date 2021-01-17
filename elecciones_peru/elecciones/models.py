from django.db import models

class candidato(models.Model):
  dni = models.IntegerField(primary_key=True)
  apellido_paterno = models.CharField(max_length=50)
  apellido_materno = models.CharField(max_length=50)
  nombres = models.CharField(max_length=50)
  fecha_nacimiento = models.DateTimeField()
  cargo_postula = models.CharField(max_length=50)
  sexo = models.CharField(max_length=1)
  carnet_extranjeria = models.TextField()
  l_n_pais = models.CharField(max_length=80)
  l_n_departamento = models.CharField(max_length=80)
  l_n_provincia = models.CharField(max_length=80)
  l_n_distrito = models.CharField(max_length=80)
  l_d_departamento = models.CharField(max_length=80)
  l_d_provincia = models.CharField(max_length=80)
  l_d_distrito = models.CharField(max_length=80)
  l_d_direccion = models.CharField(max_length=100)
  org_politica_postulate = models.CharField(max_length=90)
  link_foto = models.URLField(max_length=200)

  class Meta(CandidatoPresidencial.Meta):
    db_table = 'candidato'

class sentenciaPenal(models.Model):
  n_experiente_penal = models.IntegerField(primary_key=True)
  fecha_sentencia_firme = models.DateField()
  organo_judicial = models.CharField(max_length=100) # checar
  modalidad_penal = models.CharField(max_length=100) # checar
  fallo_pena = models.CharField(max_length=100) # checar
  delito_penal = models.CharField(max_length=100) # checar
  cumplimiendo_del_fallo = models.DateField()

  class Meta(sentenciaPenal.Meta):
    db_table = 'sentencia_penal'


class sentenciaCivil(models.Model):
  n_experiente_civil = models.IntegerField(primary_key=True)
  materia_demanda_civil = models.CharField(max_length=100) # checar
  organo_judicial = models.CharField(max_length=100) # checar
  fallo_pena = models.CharField(max_length=100) # checar

  class Meta(sentenciaCivil.Meta):
    db_table = 'sentencia_civil'


class renuncia(models.Model):
  n_experiente_civil = models.IntegerField(primary_key=True)
  materia_demanda_civil = models.CharField(max_length=100) # checar
  organo_judicial = models.CharField(max_length=100) # checar
  fallo_pena = models.CharField(max_length=100) # checar

  class Meta(renuncia.Meta):
    db_table = 'renuncia'


class experienciaLaboral(models.Model):
  ruc_empresa_laboral = models.IntegerField(primary_key=True)
  desde = models.DateField(primary_key=True)
  hasta = models.DateField(primary_key=True)
  direccion_laboral = models.CharField(max_length=100)
  pais_laboral = models.CharField(max_length=80)
  departamento_laboral = models.CharField(max_length=80)
  provincia_laboral = models.CharField(max_length=80)
  distrito_laboral = models.CharField(max_length=80)
  centro_laboral = models.CharField(max_length=100)
  oficio = models.CharField(max_length=100)

  class Meta(experienciaLaboral.Meta):
    db_table = 'experiencia_laboral'


# no tiene PK's
class educacionBasica(models.Model):
  tiene_estudio_primaria = models.BooleanField(default=True)
  concluyo_primaria = models.BooleanField(default=True)
  tiene_estudio_secundaria = models.BooleanField(default=True)
  concluyo_secundaria = models.BooleanField(default=True)

  class Meta(educacionBasica.Meta):
    db_table = 'educacion_basica'


class estudioTecnico(models.Model):
  centro_estudio_tecnico = models.CharField(max_length=100)
  carrera_tecnica = models.CharField(max_length=100)
  concluyo_estudio_tecnico = models.BooleanField(default=True)
  comentario_estudio_tecnico = models.TextField()
  tiene_estudio_tecnico = models.BooleanField(default=True)

  class Meta(estudioTecnico.Meta):
    db_table = 'estudio_tecnico'


class estudioUniversitario(models.Model):
  centro_estudio_universitario = models.CharField(max_length=100)
  concluyo_estudio_universitario = models.BooleanField(default=True)
  carrera_universitaria = models.CharField(max_length=100)
  grado_universitario = models.CharField(max_length=80)
  es_egresado_universitario = models.BooleanField(default=False)
  anhio_obtencion_universitario = models.IntegerField() 
  tiene_estudio_universitario = models.BooleanField(default=True)
  comentario_estudio_universitario = models.TextField()

  class Meta(estudioUniversitario.Meta):
    db_table = 'estudio_universitario'


class estudioNoUniversitario(models.Model):
  tiene_estudio_no_universitario = models.BooleanField(default=False)
  centro_estudio_no_universitario = models.CharField(max_length=100)
  carrera_no_universitaria = models.CharField(max_length=100)
  concluyo_estudio_no_universitario = models.BooleanField(default=True)

  class Meta(estudioNoUniversitario.Meta):
    db_table = 'estudio_no_universitario'


class estudioPostgrado(models.Model):
  tiene_postgrado = models.BooleanField(default=True)
  centro_estudio_postgrado = models.CharField(max_length=100)
  grado_postgrado = models.CharField(max_length=80)
  concluyo_estudio_postgrado = models.BooleanField(default=True)
  es_maestro = models.BooleanField(default=False)
  comentario_estudio_postgrado = models.TextField()
  es_doctor = models.BooleanField(default=False)
  anhio_obtencion_postgrado = models.IntegerField() 
  es_egresado_postgrado = models.BooleanField(default=False)

  class Meta(estudioPostgrado.Meta):
    db_table = 'estudio_postgrado'


class informacionAdicional(models.Model):
  tiene_info = models.BooleanField(default=False)
  info = models.Text()

  class Meta(informacionAdicional.Meta):
    db_table = 'informacion_adicional'


class bienRenta(models.Model):
  total_bien_muebles = models.FloatField(primary_key=True)
  total_ingresos = models.FloatField(primary_key=True)

  class Meta(bienRenta.Meta):
    db_table = 'bien _renta'


class bienInmueble(models.Model):
  esta_inscrito_sunarp = models.BooleanField(default=True)
  tipo_bien = models.CharField(max_length=20)
  direccion_inmueble = models.CharField(max_length=100)
  comentario_inmueble = models.TextField()
  partida_inmueble = models.CharField(max_length=50)
  valor_inmueble = models.FloatField()

  class Meta(bienInmueble.Meta):
    db_table = 'bien_inmueble'


class vehiculo(models.Model):
  comentario_vehiculo = models.TextField()
  valor = models.FloatField()
  placa_vehiculo = models.CharField(max_length=8)
  caracteristicas_vehiculo = models.TextField()

  class Meta(vehiculo.Meta):
    db_table = 'vehiculo'


class cargoPartidario(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  cargo = models.CharField(max_length=0)
  desde = models.DateField()
  hasta = models.DateField()
  comentario = models.TextField()

  class Meta(cargoPartidario.Meta):
    db_table = 'cargo_partidario'


class cargoEleccionPopular(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  cargo = models.CharField(max_length=0)
  desde = models.DateField()
  hasta = models.DateField()
  comentario = models.TextField()

  class Meta(cargoEleccionPopular.Meta):
    db_table = 'cargo_eleccion_popular'