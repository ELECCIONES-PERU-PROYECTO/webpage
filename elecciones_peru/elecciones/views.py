from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def candidatos(request):
  candidatos = DatosPersonales.objects.raw(
    "select * from datos_personales;"
  )
    
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos': candidatos})


def candidato_by_dni(request, dni):
  candidatos_by_dni = DatosPersonales.objects.raw(
    "select * from datos_personales where dni_candidato = '" + dni + "';"
  )
    
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos_by_dni': candidatos_by_dni})


def grado_estudios(request, niv_acad): 
  if(niv_acad == 'maestro_doctor'):
    estudios = EstudioPostgrado.objects.raw(
      "SELECT DP.id, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion "
      "FROM  estudio_postgrado AS EP JOIN  datos_personales AS DP USING (dni_candidato) "
      "WHERE (EP.es_maestro= 'SI' OR EP.es_doctor = 'SI') "
      "AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  "
      "DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  "
      "DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA'); "
    )
  else:
    if(niv_acad == 'concluyo_primaria' or niv_acad == 'concluyo_secundaria'):
      tabla = 'educacion_basica'
      modelo = EducacionBasica
    elif(niv_acad == 'concluyo_estudio_tecnico'):
      tabla = 'estudio_tecnico'
      modelo = EstudioTecnico
    elif(niv_acad == 'concluyo_estudio_no_universitario'):
      tabla = 'estudio_no_universitario'
      modelo = EstudioNoUniversitario
    elif(niv_acad == 'concluyo_estudio_universitario'):
      tabla = 'estudio_universitario'
      modelo = EstudioUniversitario
    elif(niv_acad == 'concluyo_estudio_postgrado'):
      tabla = 'estudio_postgrado'
      modelo = EstudioPostgrado
  
    estudios = modelo.objects.raw(
      "SELECT DP.id, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion "
      "FROM " + tabla + " AS EB JOIN  datos_personales AS DP USING (dni_candidato) "
      "WHERE EB." + niv_acad + " = 'SI' "
      "AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  "
      "DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  "
      "DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA'); "
    )

  return render(request,
                'elecciones/dashboard.html',
                {'estudios': estudios})
