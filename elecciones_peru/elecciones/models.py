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

  class Meta:
    db_table = 'candidato'

