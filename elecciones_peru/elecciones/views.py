from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

def presis(request):
  list_pres = DatosPersonales.objects.raw(
    "SELECT DP.id, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion "
    "FROM educacion_basica AS EB JOIN  datos_personales AS DP USING (dni_candidato) "
    "WHERE EB.concluyo_primaria   = 'SI' "
    "AND DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR "
    "DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR "
    "DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA'")

    
  return render(request,
                'elecciones/presis.html',
                {'list_pres': list_pres})
