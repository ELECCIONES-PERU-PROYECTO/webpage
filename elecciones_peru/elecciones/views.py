from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *


def function_filtros_normales(lis):  
  print("function_filtros_normales")
  print(lis)

  return ""


def function_filtros_ob(lista_):
  print("function_filtros_ob")
  print(lista_)
  return ""

def function_filtro_normal(self):
  print("self",self)
  if self[0] != "":
    if(self[0] == 'maestro_doctor'):
      query_total = "SELECT DP.id  , DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE (EP.es_maestro= 'SI' OR EP.es_doctor = 'SI') AND   (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR   DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA')   "
      
      return query_total  
    else:
      tabla = ""
      if(self[0] == 'concluyo_primaria' or self[0] == 'concluyo_secundaria'):
        self[0]=""
        tabla = 'educacion_basica'  
      elif(self[0] == 'concluyo_estudio_tecnico'):
        tabla = 'estudio_tecnico'
      elif(self[0] == 'concluyo_estudio_no_universitario'):
        tabla = 'estudio_no_universitario'
      elif(self[0] == 'concluyo_estudio_universitario'):
        tabla = 'estudio_universitario'
      elif(self[0] == 'concluyo_estudio_postgrado'):
        tabla = 'estudio_postgrado'
      retorno = "SELECT DP.id, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM " + tabla + " AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." + self[0] + " = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE  DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
      print(retorno)
      return retorno
  
  if self[4] != "": 
    self[4]=""
    return "SELECT DP.id  DP.url ,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion,  DP.dni_candidato FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[4]+"' ) AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion  ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
  
  
  if self[5] == "NO":
    self[5]=""
    return "SELECT DP.id, DP.url,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion,  DP.dni_candidato FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO' "
  
  
  
  if self[12] != "":
    self[12]=""
    return "SELECT DP.id, DP.url ,   DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM tabla_edad AS TE JOIN    datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN "+ (self[12])[:2]+ " AND " +(self[12])[3:5]    + " AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR   DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') " 
  if self[13] != "":
    self[13]=""
    return "SELECT id,  url, candidato, organizacion_politica, cargo_eleccion FROM  datos_personales WHERE   departamento_nacimiento = '"+ self[15]+"' AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion   ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
  
  
  
  if self[14]!="":
    self[14]=""
    return "SELECT id, url, candidato, organizacion_politica, cargo_eleccion FROM datos_personales WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion ='PRIMER  VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
  
  if self[16]!="":
    self[16]=""
    return "SELECT url, candidato, organizacion_politica, cargo_eleccion FROM  datos_personales  WHERE cargo_eleccion = '"+  self[16]+"' "
  
  if self[17]!= "":
    self[17]=""
    return "SELECT id, url, candidato, organizacion_politica, cargo_eleccion FROM  datos_personales WHERE organizacion_politica  = '"+self[17]+"' AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA  REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
  
  
  if self[18]!="":
    self[18]=""
    return "SELECT id, url , candidato, organizacion_politica, distrito_elec FROM  datos_personales WHERE distrito_elec = '" +self[18]+"' AND  (cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') "




def filter_function(request, nivel_academico,cargos_previos_order , orden_cant_sentencia, orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,cargo_postula, org_politica, dist_electoral, tipo_candidato_):
  lista_valores = [nivel_academico,cargos_previos_order , orden_cant_sentencia,
    orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,
    orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,
    cargo_postula, org_politica, dist_electoral, tipo_candidato_
  ]
  print(len(lista_valores))

  lista_filtros_normales = list()
  lista_filtros_ob = list()



  tienes_al_menos1 = False
  lista_val_new = list()
  lista_orden = list()
  #for item in lista_valores:
  for i in range(0,len(lista_valores)-1):
    if lista_valores[i] != "unk":
      tienes_al_menos1 = True
      index_ = lista_valores[i].find('(')
      valor = lista_valores[i][index_+1:]
      lista_valores[i] = lista_valores[i].replace("("+valor, "")
      if (i>=1 and i<=3) or ( i>=6 and i<=11): 
        lista_filtros_ob.append(lista_valores[i])
      else:
        lista_filtros_normales.append(lista_valores[i])

      lista_val_new.append(lista_valores[i])
      lista_orden.append(valor)

  print(lista_val_new)
  print(lista_orden)


  lista_index = list()
  if (tienes_al_menos1  == True):
    j=1 
    for i in range(0, len(lista_orden)):
      val = lista_orden.index(str(j))
      lista_index.append(val)
      j+=1
    print(lista_index)

    LN = list()
    for i in lista_index:
      LN.append(lista_val_new[i])
    print(LN)

    print("------------------------------")
    print(lista_filtros_ob)
    lista_filtros_ob_new = list()
    for i in range(0, len(LN)):
      if(LN[i] in lista_filtros_ob):
        lista_filtros_ob_new.append(LN[i])

    print(lista_filtros_ob_new)
  query_total = ""
  if len(lista_filtros_normales) == 0:
    function_filtros_ob(lista_filtros_ob)
    print("hola")  #llamar funcion order by 
  elif len(lista_filtros_ob) == 0:
    query_total = query_total + function_filtro_normal(lista_valores)
    for i in range(1, len(lista_filtros_normales)):
      query_total = query_total +" INTERSECT "+ function_filtro_normal(lista_valores)

  print(query_total)
  candidatos = DatosPersonales.objects.raw(query_total)
  
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos': candidatos}) 


def test_query(request, nivel_academico):
  print("test_query: NIVEL ACADEMICO ", nivel_academico)
  test = DatosPersonales.objects.raw(
    "select * from datos_personales;"
  )
  return render(request,'elecciones/dashboard.html',{'test': test})

def candidatos(request):
  candidatos = DatosPersonales.objects.raw(
    "select * from datos_personales;"
  )
    
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos': candidatos})


def candidato_by_dni(request, dni):
  #candidatos_by_dni = DatosPersonales.objects.raw(
  #  "select * from datos_personales where dni_candidato = '" + dni + "';"
  #   "select * from datos_personales;"
  #)
  candidatos_by_dni = DatosPersonales.objects.raw("SELECT  id ,candidato, organizacion_politica, distrito_elec FROM  datos_personales WHERE departamento_nacimiento = 'AMAZONAS' AND  (cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') INTERSECT SELECT DP.id ,   DP.candidato, DP.organizacion_politica, DP.distrito_elec FROM estudio_postgrado AS EP  JOIN  datos_personales AS DP USING (dni_candidato) WHERE   EP.concluyo_estudio_postgrado = 'SI' AND  (DP.cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') ")
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos_by_dni': candidatos_by_dni})


def grado_estudios(request, niv_acad):

  ''' 
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
    )'''
  
  object2 = EducacionBasica.objects.filter(concluyo_primaria="SI")

  querysetretorno = EducacionBasica.objects.none()

  #variable tipo queryset VAR
  object1 = DatosPersonales.objects.all()
  print(len(object1))
  for item in object1:
    #print("dasa")
    print(item.id)
    item_append = item.get_edu_join(object2)
    querysetretorno = querysetretorno | item_append




  #object1.get_edu_join(object1, object2)
  #object1[0].get_edu_join(object2)
  #for item in object1:
  #  item.get_edu_join(object2)
  for item in querysetretorno:
    print(item.dni_candidato, item.candidato)
  
  #all_objects = DatosPersonales.objects.all()
  #pubs = publication.objects.select_related('country', 'country_state', 'city')

  #objects = DatosPersonales.objects.filter(EducacionBasica)
  #
  #qry1 = "SELECT DP.id, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM EducacionBasica AS EB,  datos_personales AS DP  WHERE EB.dni_candidato=%s EB." + niv_acad + " = 'SI' " "AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA');"
  #
  #cars = DatosPersonales.objects.raw(qry1,[dni_candidato])
  #
  #for obj in objects:
  #  print(obj.dni_candidato)

#  return render(request,'elecciones/dashboard.html',{'estudios': estudios})
  return render(request,'elecciones/dashboard.html',{})
