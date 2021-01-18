from django.db import models

class DatosPersonales(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=200)
  carnet_extranjeria = models.CharField(max_length=12, default='-')
  apellido_paterno = models.CharField(max_length=100)
  apellido_materno = models.CharField(max_length=100)
  nombres = models.CharField(max_length=150)
  sexo = models.CharField(max_length=10)
  fecha_nacimiento = models.CharField(max_length=40)
  pais_nacimiento = models.CharField(max_length=80)
  departamento_nacimiento = models.CharField(max_length=80)
  provincia_nacimiento = models.CharField(max_length=80)
  distrito_nacimiento = models.CharField(max_length=100)
  departamento_domicilio = models.CharField(max_length=80)
  provincia_domicilio = models.CharField(max_length=80)
  distrito_domicilio = models.CharField(max_length=100)
  direccion_domicilio = models.CharField(max_length=200)
  cargo_eleccion = models.CharField(max_length=200)

  class Meta:
    db_table = 'datos_personales'


class ExperienciaLaboral(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=200)
  tiene_experiencia_laboral = models.CharField(max_length=2)
  centro_laboral = models.CharField(max_length=300)
  ocupacion = models.CharField(max_length=400)
  ruc_empresa_laboral = models.CharField(max_length=30)
  direccion_laboral = models.CharField(max_length=100)
  desde_anhio = models.CharField(max_length= 20)
  hasta_anhio = models.CharField(max_length= 20)
  pais_laboral = models.CharField(max_length=80)
  departamento_laboral = models.CharField(max_length=80)
  provincia_laboral = models.CharField(max_length=80)

  class Meta:
    db_table = 'experiencia_laboral'
    unique_together = ('ruc_empresa_laboral', 'desde_anhio', 'hasta_anhio', 'dni_candidato',)


class EducacionBasica(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_educacion_basica = models.CharField(max_length=2)
  tiene_estudio_primaria = models.CharField(max_length=2)
  concluyo_primaria = models.CharField(max_length=2)
  tiene_estudio_secundaria = models.CharField(max_length=2)
  concluyo_secundaria = models.CharField(max_length=2)

  class Meta:
    db_table = 'educacion_basica'


class EstudioTecnico(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_estudio_tecnico = models.CharField(max_length=2)
  centro_estudio_tecnico = models.CharField(max_length=200)
  carrera_tecnica = models.CharField(max_length=200)
  concluyo_estudio_tecnico = models.CharField(max_length=10)
  comentario_estudio_tecnico = models.TextField()

  class Meta:
    db_table = 'estudio_tecnico'


class EstudioNoUniversitario(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_estudio_no_universitario = models.CharField(max_length=2)
  centro_estudio_no_universitario = models.CharField(max_length=200)
  carrera_no_universitaria = models.CharField(max_length=200)
  concluyo_estudio_no_universitario = models.CharField(max_length=2)

  class Meta:
    db_table = 'estudio_no_universitario'


class EstudioUniversitario(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_estudio_universitario = models.CharField(max_length=2)
  universidad = models.CharField(max_length=200)
  carrera_universitaria = models.CharField(max_length=150)
  concluyo_estudio_universitario = models.CharField(max_length=2)
  es_egresado_universitario = models.CharField(max_length=2)
  anhio_obtencion_universitario = models.CharField(max_length=4)
  comentario_estudio_universitario = models.TextField()

  class Meta:
    db_table = 'estudio_universitario'


class EstudioPostgrado(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_postgrado = models.CharField(max_length=2)
  centro_estudio_postgrado = models.CharField(max_length=200)
  especialidad = models.CharField(max_length=200)
  concluyo_estudio_postgrado = models.CharField(max_length=2)
  es_egresado_postgrado = models.CharField(max_length=2)
  es_maestro = models.CharField(max_length=2)
  es_doctor = models.CharField(max_length=2)
  anhio_obtencion_postgrado = models.CharField(max_length=2) 
  comentario_estudio_postgrado = models.TextField()

  class Meta:
    db_table = 'estudio_postgrado'


class CargoPartidario(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_cargo_partidario = models.CharField(max_length=2)
  organizacion_politica = models.CharField(max_length=150)
  cargo = models.CharField(max_length=300)
  desde_anhio = models.CharField(max_length=4)
  hasta_anhio = models.CharField(max_length=4)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_partidario'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_carg_parti'
      )
    ]


class CargoEleccion(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_info_por_declarar = models.CharField(max_length=2)
  organizacion_politica = models.CharField(max_length=150)
  desde_anhio = models.CharField(max_length=20)
  hasta_anhio = models.CharField(max_length=20)
  cargo = models.CharField(max_length=300)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_eleccion'
    constraints = [
      models.UniqueConstraint(
        fields=['dni_candidato'],
        name='unique dni_elecc_popu'
      )
    ]


class Renuncia(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_info_por_declarar = models.CharField(max_length=2)
  organización_politica = models.CharField(max_length=140) 
  comentario = models.TextField()

  class Meta:
    db_table = 'renuncia'
    unique_together = ('dni_candidato', 'organización_politica',)


class SentenciaPenal(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_info_por_declarar = models.CharField(max_length=2)
  n_experiente_penal = models.CharField(max_length=40, primary_key=True)
  fecha_sentencia_firme = models.CharField(max_length=40)
  organo_judicial = models.CharField(max_length=100)
  delito_penal = models.CharField(max_length=120) 
  fallo_pena = models.CharField(max_length=120) 
  modalidad_penal = models.CharField(max_length=100) 
  otra_modalidad = models.CharField(max_length=100) 
  cumplimiendo_del_fallo = models.TextField()  

  class Meta:
    db_table = 'sentencia_penal'


class SentenciaObligacion(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_info_por_declarar = models.CharField(max_length=2)
  materia_sentencia = models.CharField(max_length=140) 
  n_experiente_obliga = models.CharField(max_length=40, primary_key=True)
  organo_judicial = models.CharField(max_length=100) 
  fallo_obliga = models.CharField(max_length=120) 

  class Meta:
    db_table = 'sentencia_obligacion'


class Ingresos(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_ingresos = models.CharField(max_length=2)
  anhio_ingresos = models.CharField(max_length=4)
  remu_bruta_pub = models.FloatField()
  remu_bruta_priv = models.FloatField()
  renta_indiv_pub = models.FloatField()
  renta_indiv_priv = models.FloatField()
  otro_ingreso_pub = models.FloatField()
  otro_ingreso_priv = models.FloatField()

  class Meta:
    db_table = 'ingresos'


class BienInmueble(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_inmueble = models.CharField(max_length=2)
  tipo_inmueble = models.CharField(max_length=150)
  direccion_inmueble = models.CharField(max_length=200)
  esta_inscrito_sunarp = models.CharField(max_length=10)
  partida_inmueble_sunarp = models.CharField(max_length=100)
  autovaluo = models.FloatField()
  comentario_inmueble = models.TextField()

  class Meta:
    db_table = 'bien_inmueble'


class BienMueble(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_bien_mueble = models.CharField(max_length=2)
  vehiculo = models.CharField(max_length=200)
  placa = models.CharField(max_length=8)
  valor = models.FloatField()
  caracteristicas_vehiculo = models.TextField()
  comentario_vehiculo = models.TextField()

  class Meta:
    db_table = 'bien_mueble'


class InformacionAdicional(models.Model):
  organizacion_politica = models.CharField(max_length=100)
  distrito_eleccion = models.CharField(max_length=100)
  dni_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
  candidato = models.CharField(max_length=200)
  tiene_info_adicional = models.CharField(max_length=2)
  info = models.TextField()

  class Meta:
    db_table = 'informacion_adicional'