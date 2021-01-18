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
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, default='-')
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
    unique_together = ('ruc_empresa_laboral', 'desde', 'hasta', 'dni_candidato',)


class EducacionBasica(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  tiene_estudio_primaria = models.CharField(max_length=10)
  concluyo_primaria = models.CharField(max_length=10)
  tiene_estudio_secundaria = models.CharField(max_length=10)
  concluyo_secundaria = models.CharField(max_length=10)

  class Meta:
    db_table = 'educacion_basica'


class EstudioTecnico(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  tiene_estudio_tecnico = models.CharField(max_length=10)
  centro_estudio_tecnico = models.CharField(max_length=200)
  carrera_tecnica = models.CharField(max_length=200)
  concluyo_estudio_tecnico = models.CharField(max_length=10)
  comentario_estudio_tecnico = models.TextField()

  class Meta:
    db_table = 'estudio_tecnico'


class EstudioNoUniversitario(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  tiene_estudio_no_universitario = models.CharField(max_length=10)
  centro_estudio_no_universitario = models.CharField(max_length=200)
  carrera_no_universitaria = models.CharField(max_length=200)
  concluyo_estudio_no_universitario = models.CharField(max_length=10)

  class Meta:
    db_table = 'estudio_no_universitario'


class EstudioUniversitario(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  tiene_estudio_universitario = models.CharField(max_length=10)
  centro_estudio_universitario = models.CharField(max_length=200)
  concluyo_estudio_universitario = models.CharField(max_length=10)
  grado_universitario = models.CharField(max_length=150)
  es_egresado_universitario = models.CharField(max_length=10)
  anhio_obtencion_universitario = models.CharField(max_length=10)
  comentario_estudio_universitario = models.TextField()

  class Meta:
    db_table = 'estudio_universitario'


class EstudioPostgrado(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
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


class CargoPartidario(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  organizacion_politica = models.CharField(max_length=150)
  cargo = models.CharField(max_length=300)
  desde = models.CharField(max_length=20)
  hasta = models.CharField(max_length=20)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_partidario'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_carg_parti'
      )
    ]


class CargoEleccionPopular(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  organizacion_politica = models.CharField(max_length=150)
  cargo = models.CharField(max_length=300)
  desde = models.CharField(max_length=20)
  hasta = models.CharField(max_length=20)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_eleccion_popular'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_elecc_popu'
      )
    ]


class Renuncia(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  organización_politica = models.CharField(max_length=140) 
  anhio = models.CharField(max_length=10)
  comentario = models.TextField()

  class Meta:
    db_table = 'renuncia'
    unique_together = ('dni_candidato', 'organización_politica', 'anhio',)


class SentenciaPenal(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  n_experiente_penal = models.CharField(max_length=40, primary_key=True)
  fecha_sentencia_firme = models.CharField(max_length=40)
  organo_judicial = models.CharField(max_length=100)
  delito_penal = models.CharField(max_length=120) 
  fallo_pena = models.CharField(max_length=120) 
  modalidad_penal = models.CharField(max_length=100) 
  cumplimiendo_del_fallo = models.TextField()  

  class Meta:
    db_table = 'sentencia_penal'


class SentenciaCivil(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  materia_demanda_civil = models.CharField(max_length=140) 
  n_experiente_civil = models.CharField(max_length=40, primary_key=True)
  organo_judicial = models.CharField(max_length=100) 
  fallo_pena = models.CharField(max_length=120) 

  class Meta:
    db_table = 'sentencia_civil'


# es Ingresos en JSON
class BienRenta(models.Model):
  anhio = models.CharField(max_length=10)
  total_bien_muebles = models.FloatField()
  total_ingresos = models.FloatField()

  class Meta:
    db_table = 'bien_renta'
    unique_together = ('total_bien_muebles', 'total_ingresos',)


class BienInmueble(models.Model):
  total_ingresos = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  numero = models.IntegerField()
  tipo_bien = models.CharField(max_length=100)
  direccion_inmueble = models.CharField(max_length=300)
  esta_inscrito_sunarp = models.CharField(max_length=10)
  partida_inmueble = models.CharField(max_length=100)
  valor_inmueble = models.FloatField()
  comentario_inmueble = models.TextField()

  class Meta:
    db_table = 'bien_inmueble'

# agregué el atr vehiculo ya que no existía en el modelo ER
class Vehiculo(models.Model):
  total_bien_muebles = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='total_bien_muebles')
  total_ingresos = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='total_ingresos')
  numero = models.IntegerField()
  vehiculo = models.CharField(max_length=100)
  placa_vehiculo = models.CharField(max_length=10)
  caracteristicas_vehiculo = models.TextField()
  valor = models.FloatField()
  comentario_vehiculo = models.TextField()

  class Meta:
    db_table = 'vehiculo'
    unique_together = ('total_bien_muebles', 'total_ingresos', 'placa_vehiculo',)


class InformacionAdicional(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  info = models.TextField()

  class Meta:
    db_table = 'informacion_adicional'


class TieneTP(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

  class Meta:
    db_table = 'tiene_trayectoria_partidaria'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_tp'
      )
    ]


class TieneInfoA(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

  class Meta:
    db_table = 'tiene_informacion_adicional'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_infoA'
      )
    ]


class TieneBR(models.Model):
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

  class Meta:
    db_table = 'tiene_bien_renta'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_tieneBR'
      )
    ]