from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

query = 'NO'
test = " AND DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR "

def candidatos(request):
  candidatos = DatosPersonales.objects.raw(
    "select * from datos_personales;")
    
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos': candidatos})
