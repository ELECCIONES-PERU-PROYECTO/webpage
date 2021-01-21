from django.db import models
# test_datos = DatosPersonales(organizacion_politica='MRTA', distrito_elec='dist_test', dni_candidato='87654321', carnet_extranjeria='13456678', apellido_paterno='si' , candidato='esteban si no' , apellido_materno='no', nombres='esteban', sexo='no sabe', fecha_nacimiento='18/34/45', pais_nacimiento='peru', departamento_nacimiento='peru', provincia_nacimiento='peru', distrito_nacimiento='peru' , departamento_domicilio='peru', provincia_domicilio='peru', distrito_domicilio='peru', direccion_domicilio='peru', cargo_eleccion='niu')
class DatosPersonales(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
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
  distrito_domicilio = models.CharField(max_length=80)
  direccion_domicilio = models.CharField(max_length=200)
  cargo_eleccion = models.CharField(max_length=200)

  class Meta:
    db_table = 'datos_personales'
    unique_together = ('dni_candidato', 'cargo_eleccion',)


class ExperienciaLaboral(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_experiencia_laboral = models.CharField(max_length=10)
  centro_laboral = models.CharField(max_length=300)
  ocupacion = models.CharField(max_length=200)
  ruc_empresa_laboral = models.CharField(max_length=30)
  direccion_laboral = models.CharField(max_length=100)
  desde_anhio = models.CharField(max_length= 20)
  hasta_anhio = models.CharField(max_length= 20)
  pais_laboral = models.CharField(max_length=80)
  departamento_laboral = models.CharField(max_length=80)
  provincia_laboral = models.CharField(max_length=80)
  distrito_laboral = models.CharField(max_length=80)

  class Meta:
    db_table = 'experiencia_laboral'


class EducacionBasica(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_educacion_basica = models.CharField(max_length=10)
  tiene_estudio_primaria = models.CharField(max_length=10)
  concluyo_primaria = models.CharField(max_length=10)
  tiene_estudio_secundaria = models.CharField(max_length=10)
  concluyo_secundaria = models.CharField(max_length=10)

  class Meta:
    db_table = 'educacion_basica'


class EstudioTecnico(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_estudio_tecnico = models.CharField(max_length=10)
  centro_estudio_tecnico = models.CharField(max_length=200)
  carrera_tecnica = models.CharField(max_length=200)
  concluyo_estudio_tecnico = models.CharField(max_length=10)
  comentario_estudio_tecnico = models.TextField()

  class Meta:
    db_table = 'estudio_tecnico'


class EstudioNoUniversitario(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_estudio_no_universitario = models.CharField(max_length=10)
  centro_estudio_no_universitario = models.CharField(max_length=200)
  carrera_no_universitaria = models.CharField(max_length=200)
  concluyo_estudio_no_universitario = models.CharField(max_length=10)

  class Meta:
    db_table = 'estudio_no_universitario'


class EstudioUniversitario(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_estudio_universitario = models.CharField(max_length=10)
  universidad = models.CharField(max_length=200)
  carrera_universitaria = models.CharField(max_length=150)
  concluyo_estudio_universitario = models.CharField(max_length=10)
  es_egresado_universitario = models.CharField(max_length=10)
  anhio_obtencion_universitario = models.CharField(max_length=4)
  comentario_estudio_universitario = models.TextField()

  class Meta:
    db_table = 'estudio_universitario'


class EstudioPostgrado(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_postgrado = models.CharField(max_length=10)
  centro_estudio_postgrado = models.CharField(max_length=200, null=True)
  especialidad = models.CharField(max_length=200, null=True)
  concluyo_estudio_postgrado = models.CharField(max_length=10, null=True)
  es_egresado_postgrado = models.CharField(max_length=10, null=True)
  es_maestro = models.CharField(max_length=10, null=True)
  es_doctor = models.CharField(max_length=10, null=True)
  anhio_obtencion_postgrado = models.CharField(max_length=10, null=True)
  comentario_estudio_postgrado = models.TextField()

  class Meta:
    db_table = 'estudio_postgrado'


class CargoPartidario(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_cargo_partidario = models.CharField(max_length=10)
  org_politica_cargo = models.CharField(max_length=250)
  cargo = models.CharField(max_length=300)
  desde_anhio = models.CharField(max_length=4)
  hasta_anhio = models.CharField(max_length=4)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_partidario'


class CargoEleccion(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_info_por_declarar = models.CharField(max_length=10)
  org_politica_cargo = models.CharField(max_length=250)
  desde_anhio = models.CharField(max_length=20)
  hasta_anhio = models.CharField(max_length=20)
  cargo = models.CharField(max_length=300)
  comentario = models.TextField()

  class Meta:
    db_table = 'cargo_eleccion'


class Renuncia(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_info_por_declarar = models.CharField(max_length=10)
  organización_renuncia = models.CharField(max_length=140) 
  comentario = models.TextField()

  class Meta:
    db_table = 'renuncia'


class SentenciaPenal(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_info_por_declarar = models.CharField(max_length=10)
  n_experiente_penal = models.CharField(max_length=40)
  fecha_sentencia_penal = models.CharField(max_length=40)
  organo_judicial = models.CharField(max_length=100)
  delito_penal = models.CharField(max_length=120) 
  fallo_penal = models.CharField(max_length=300) 
  modalidad_penal = models.CharField(max_length=100) 
  otra_modalidad = models.CharField(max_length=100) 
  cumplimiento_del_fallo = models.TextField()

  class Meta:
    db_table = 'sentencia_penal'


class SentenciaObligacion(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_info_por_declarar = models.CharField(max_length=10)
  materia_sentencia = models.CharField(max_length=140) 
  n_experiente_obliga = models.CharField(max_length=40)
  organo_judicial = models.CharField(max_length=100) 
  fallo_obliga = models.CharField(max_length=500) 

  class Meta:
    db_table = 'sentencia_obligacion'


class Ingreso(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_ingresos = models.CharField(max_length=10)
  anhio_ingresos = models.CharField(max_length=4)
  total_ingresos = models.FloatField()

  class Meta:
    db_table = 'ingreso'


class BienInmueble(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_inmueble = models.CharField(max_length=10)
  tipo_inmueble = models.CharField(max_length=150)
  direccion_inmueble = models.CharField(max_length=400)
  esta_inscrito_sunarp = models.CharField(max_length=10)
  partida_inmueble_sunarp = models.CharField(max_length=100)
  autovaluo = models.FloatField(default=0, null=True)
  comentario_inmueble = models.TextField()

  class Meta:
    db_table = 'bien_inmueble'


class BienMueble(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_bien_mueble = models.CharField(max_length=10)
  vehiculo = models.CharField(max_length=200)
  placa = models.CharField(max_length=20)
  valor = models.FloatField(default=0)
  caracteristicas_vehiculo = models.TextField()
  comentario_vehiculo = models.TextField()

  class Meta:
    db_table = 'bien_mueble'


class InformacionAdicional(models.Model):
  id = models.CharField(max_length=10, primary_key=True)
  organizacion_politica = models.CharField(max_length=250)
  distrito_elec = models.CharField(max_length=100)
  dni_candidato = models.CharField(max_length=8)
  candidato = models.CharField(max_length=250)
  tiene_info_adicional = models.CharField(max_length=10)
  info = models.TextField()

  class Meta:
    db_table = 'informacion_adicional'