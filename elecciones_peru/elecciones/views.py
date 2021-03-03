from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from .models import *
from itertools import chain

def function_filtros_ob(self, query_normal, normnob1, SELECT_candidato, WHERE_candidato):
  query_total = ""
  subquery_list = list()
  for i in range(0, len(self)):
    index_ = self[i].find('_')
    indice = self[i].find("(")
    valor = self[i][index_+1:]
    nrorden = self[i][indice+1:indice+3:1]
    uwu = nrorden.find("_")
    quitar = self[i][index_-1:]

    if int(valor) > 9 and uwu==-1:
      quitar = self[i][index_-2:]
    aux = self[i].replace("("+quitar, "") 
    self[i] = aux

    if valor == "1":
      if len(self) > 1 or normnob1 == True: #cargos previos
        subquery = " SELECT DP.id, SUM(CE.total_anhio_eleccion) AS conteo, DP.dni_candidato FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND "+ WHERE_candidato+ " GROUP BY (DP.id, DP.dni_candidato)  "       
        subquery_list.append(subquery)
      else:
        subquery = " SELECT DP.id, SUM( CE.total_anhio_eleccion )AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "  +  SELECT_candidato + " FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND "  + WHERE_candidato + "  GROUP BY (  Dp.id, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+ ") ORDER BY conteo " +self[i]
        return subquery
    elif valor == "2":# cant sentencia penal 
      if len(self) >1 or normnob1 == True :
        subquery =   " SELECT DP.id, COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND " + WHERE_candidato+" GROUP BY (DP.id,DP.dni_candidato)  "
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT DP.id, COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "+ SELECT_candidato  +"  FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  " +  WHERE_candidato  +" GROUP BY (Dp.id, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo  " +self[i] 
        return subquery                            
    elif valor == "3": #cantidad sentencia obligaciones
      if len(self) >1 or normnob1 == True :
        subquery = " SELECT DP.id, COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  " +   WHERE_candidato +    " GROUP BY (DP.id,DP.dni_candidato) "
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT  DP.id, COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +  " FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND " +  WHERE_candidato +"   GROUP BY (" + SELECT_candidato + ", DP.dni_candidato,DP.candidato, DP.organizacion_politica, DP.id) ORDER BY conteo  " +self[i]
        return subquery
    elif valor == "6":#cantidad ingresos
      subquery = " SELECT  DP.id,total_ingresos AS  conteo, DP.dni_candidato FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND "+ WHERE_candidato +"  GROUP BY (DP.id,  DP.dni_candidato, conteo) "
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT DP.id, total_ingresos AS  conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica," + SELECT_candidato  +   " FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND "+ WHERE_candidato +" GROUP BY ( DP.id,DP.dni_candidato, total_ingresos, DP.candidato, DP.organizacion_politica, "  +  SELECT_candidato +") ORDER BY conteo "  + self[i]
        return subquery
    elif valor == "7":#cantidad inmueble
      subquery = " SELECT  DP.id,COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND "+ WHERE_candidato+"  GROUP BY (DP.id,DP.dni_candidato) " 
      if len(self) >1 or ( normnob1 == True):
        subquery_list.append(subquery)
      else:
        subquery = "SELECT  DP.id, COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+" FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND " + WHERE_candidato+"  GROUP BY (DP.id,DP.dni_candidato, DP.candidato, DP.organizacion_politica," + SELECT_candidato+ ") ORDER BY conteo " + self[i]             
        return subquery            
    elif valor == "8":  #valor inmuebles
      subquery = " SELECT DP.id, SUM (BI.autovaluo) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND  "+   WHERE_candidato +"  GROUP BY (DP.id,DP.dni_candidato)  "
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT  DP.id,SUM (BI.autovaluo) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +"  FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND " + WHERE_candidato+ " GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.id, "+ SELECT_candidato +" ) ORDER BY conteo " + self[i]
        return subquery 
    elif valor == "9" : # cantidad muebles
      subquery = " SELECT DP.id,COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  "+  WHERE_candidato +  " GROUP BY (DP.id,DP.dni_candidato) " 
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT DP.id,COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+ " FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  " +  WHERE_candidato+ " GROUP BY (DP.id,DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+SELECT_candidato+"  ) ORDER BY conteo "+self [i]                
        return subquery
    elif valor == "10"  : #valor muebles
      subquery = " SELECT DP.id, SUM (BM.valor ) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND " + WHERE_candidato+ " GROUP BY (DP.id,DP.dni_candidato)  " 
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT DP.id,SUM (BM.valor ) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+" FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND "  + WHERE_candidato+ " GROUP BY (DP.id,DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+ SELECT_candidato+" ) ORDER BY conteo  " + self[i]
        return subquery
    elif valor == "11": #renuncias
      subquery = " SELECT DP.id,COUNT(R.dni_candidato) AS conteo, DP.dni_candidato FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  "+WHERE_candidato+" GROUP BY (DP.id,DP.dni_candidato)  "
      if len(self) >1 or normnob1 == True:
        subquery_list.append(subquery)
      else: 
        subquery = " SELECT  DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica, " + SELECT_candidato+", COUNT(R.dni_candidato) AS conteo FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND "+ WHERE_candidato+" GROUP BY ( DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo "+ self[i]                
        return subquery

  #return subquery_list
  if normnob1 == True:
    return subquery_list
  SELECT = " SELECT DP.id,  DP.candidato,DP.dni_candidato, DP.organizacion_politica,  "+ SELECT_candidato 
  WHERE = " WHERE  "+ WHERE_candidato
  Qs = "" 
  ORDER_BY = ""
  #print(len(subquery_list))

  for i in range(0, len(subquery_list)):
    Qs = Qs + " Q"+str(i+1)+".conteo "
    if i < len(subquery_list)-1:
      Qs = Qs + ", "
  Qs_ = ""
  for i in range(0, len(subquery_list)):
    Qs_ = Qs_ + " Q"+str(i+1)+".conteo "+self[i]
    if i < len(subquery_list)-1:
      Qs_ = Qs_ + ", "
  
  FROM = ""
  GROUP_BY_ = " GROUP BY (DP.id,DP.candidato,DP.dni_candidato, DP.organizacion_politica,  "+  SELECT_candidato+" , "+ Qs+" ) "
  #print("query_normal: ",query_normal)
  for i in range(0, len(subquery_list)):          
    if i == 0 and query_normal != "":
      FROM = " FROM ( " + query_normal+ " ) AS  QN JOIN datos_personales AS DP USING (dni_candidato) "  
    if i == 0 and query_normal == "":
      FROM = " FROM ("+ subquery_list[i] +" ) AS "+" Q"+str(i+1)+ " JOIN datos_personales AS DP USING (dni_candidato) "     
      continue
    FROM = FROM + " JOIN ("+subquery_list[i]   +" ) AS Q" +str(i+1)+ " USING (dni_candidato) "    
  ORDER_BY = " ORDER BY "+Qs_
  query_total = SELECT + ", " + Qs + FROM + WHERE + GROUP_BY_ + ORDER_BY

  #print("query_total_function: ", query_total)

  return query_total

def function_filtro_normal(self, stack_, SELECT_candidato,WHERE_candidato ):
  # print("self",self)
  print("SELECT_candidato: ", SELECT_candidato)
  print("WHERE_candidato: ", WHERE_candidato)
  if stack_== False:
    if self[0] != "":
      print("self[0]: ",self[0])
      if(self[0] == 'maestro_doctor'):
        query_total = "SELECT DISTINCT DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+  SELECT_candidato+ "  FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE ((EP.es_maestro= 'SI' ) OR (EP.es_doctor = 'SI')) AND  "+ WHERE_candidato
        return query_total
      else:
        tabla = ""
        if(self[0] == 'concluyo_primaria' or self[0] == 'concluyo_secundaria'):
          tabla = 'educacion_basica'
        elif(self[0] == 'concluyo_estudio_tecnico'):
          tabla = 'estudio_tecnico'
        elif(self[0] == 'concluyo_estudio_no_universitario'):
          tabla = 'estudio_no_universitario'
        elif(self[0] == 'concluyo_estudio_universitario'):
          print("ASDADSADSADSADASADSAD")
          tabla = 'estudio_universitario'
        elif(self[0] == 'concluyo_estudio_postgrado'):
          tabla = 'estudio_postgrado'
        retorno = "SELECT DISTINCT DP.id, DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +"  FROM " + tabla + \
          " AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." +  self[0] + " = 'SI' AND "+ WHERE_candidato
        self[0] = ""
        return retorno
    if self[4] != "":
      retorno = "SELECT DISTINCT DP.id, DP.dni_candidato,  DP.candidato, DP.organizacion_politica,  "+ SELECT_candidato +",  DP.dni_candidato FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[
        4]+"' ) AND  " + WHERE_candidato
      self[4] = ""
      return retorno
    if self[5] == "NO":
      retorno = "SELECT DISTINCT DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica,  "+SELECT_candidato+"  FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO'  AND "+ WHERE_candidato
      self[5] = ""
      return retorno
    if self[12] != "":
      retorno = "SELECT DISTINCT DP.id,  DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+ SELECT_candidato+"  FROM tabla_edad AS TE JOIN  datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + ( self[12])[3:5] + " AND  "+WHERE_candidato
      self[12] = ""
      return retorno
    if self[13] == "SI":
      retorno = "SELECT  DISTINCT DP.id, DP.dni_candidato, DP.candidato, Dp.organizacion_politica, " + SELECT_candidato+"   FROM datos_personales AS DP  WHERE    departamento_nacimiento = '"+ self[15]+"' AND "+WHERE_candidato 
      self[13] = ""
      return retorno
    if self[14] != "":
      retorno = "SELECT DISTINCT  DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,  "+ SELECT_candidato +"  FROM datos_personales AS DP  WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND  "+ WHERE_candidato
      self[14] = ""
      return retorno
    if self[16] != "":
      retorno = "SELECT  DISTINCT DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,  "+ SELECT_candidato +"  FROM  datos_personales AS DP  WHERE cargo_eleccion = '"+ self[16]+"' "
      self[16] = ""
      return retorno
    if self[17] != "":
      retorno = "SELECT DISTINCT  DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+SELECT_candidato+" FROM  datos_personales AS DP WHERE organizacion_politica  = '" +self[17]+"' AND  "+ WHERE_candidato
      self[17] = ""
      return retorno
    if self[18] != "":
      retorno = "SELECT  DISTINCT DP.id,   DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+SELECT_candidato+" FROM  datos_personales AS DP WHERE distrito_elec = '" + self[18] + "' AND  "+ WHERE_candidato
      self[18] = ""
      return retorno
  elif stack_ == True:
    if self[0] != "":
      print("self[0]: ",self[0])
      if( self[0] == 'maestro_doctor'):
        query_total = "SELECT  DISTINCT  DP.dni_candidato FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE (EP.es_maestro= 'SI' OR EP.es_doctor = 'SI') AND " + WHERE_candidato
        self[0] = ""
        return query_total
      else:
        tabla = ""
        if(self[0] == 'concluyo_primaria' or self[0] == 'concluyo_secundaria'):
          tabla = 'educacion_basica'
        elif(self[0] == 'concluyo_estudio_tecnico'):
          tabla = 'estudio_tecnico'
        elif(self[0] == 'concluyo_estudio_no_universitario'):
          tabla = 'estudio_no_universitario'
        elif(self[0] == 'concluyo_estudio_universitario'):
          tabla = 'estudio_universitario'
        elif(self[0] == 'concluyo_estudio_postgrado'):
          tabla = 'estudio_postgrado'
        retorno = "SELECT DISTINCT  DP.dni_candidato FROM " + tabla +" AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." +  self[0] + " = 'SI' AND  " + WHERE_candidato
        self[0] = ""
        return retorno
    if self[4] != "":
      retorno = "SELECT  DISTINCT DP.dni_candidato  FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[4]+"' ) AND  "+WHERE_candidato
      self[4] = ""
      return retorno
    if self[5] == "NO":
      retorno = "SELECT DISTINCT  DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO' "
      self[5] = ""
      return retorno
    if self[12] != "":
      retorno = "SELECT  DISTINCT  DP.dni_candidato FROM tabla_edad AS TE JOIN    datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + ( self[12])[3:5] + " AND "+ WHERE_candidato
      self[12] = ""
      return retorno
    if self[13] == "SI":
      retorno = "SELECT DISTINCT  DP.dni_candidato FROM  datos_personales AS DP WHERE   departamento_nacimiento = '"+ self[15]+"' AND  "+WHERE_candidato 
      self[13] = ""
      return retorno
    if self[14] != "":
      retorno = "SELECT   DISTINCT  DP.dni_candidato FROM datos_personales AS DP WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND  "+WHERE_candidato
      self[14] = ""
      return retorno
    if self[16] != "":
      retorno = "SELECT   DISTINCT  DP.dni_candidato FROM  datos_personales AS DP WHERE cargo_eleccion = '" + self[16]+"' "
      self[16] = ""
      return retorno
    if self[17] != "":
      retorno = "SELECT DISTINCT    DP.dni_candidato FROM  datos_personales AS DP WHERE organizacion_politica  = '" +self[17]+"' AND  "+WHERE_candidato
      self[17] = ""
      return retorno
    if self[18] != "":
      retorno = "SELECT  DISTINCT   DP.dni_candidato FROM  datos_personales AS DP WHERE distrito_elec = '" + self[18] + "' AND  (cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA' ) "
      self[18] = ""
      return retorno

def filter_function(request, nivel_academico, cargos_previos_order, orden_cant_sentencia, orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,cargo_postula, org_politica, dist_electoral, tipo_candidato_):
  lista_valores = [nivel_academico, cargos_previos_order, orden_cant_sentencia,
    orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,
    orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,
    cargo_postula, org_politica, dist_electoral, tipo_candidato_
  ]

  if lista_valores[4] != "unk":
    index = lista_valores[4].find("(")
    aux = lista_valores[4][index:len(lista_valores[4]) :+1]
    lista_valores[4] = "FAMILIA / ALIMENTARIA"+aux
  
  print("tipo_candidato_: ", tipo_candidato_)
  SELECT_candidato = ""
  WHERE_candidato = ""
  GROUP_by = ""

  if tipo_candidato_ == "presidenciales":
    SELECT_candidato =  " DP.cargo_eleccion "
    WHERE_candidato = " (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion  ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
  elif tipo_candidato_ == "congresales":
    SELECT_candidato = " DP.distrito_elec "
    WHERE_candidato = " (DP.cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') "
  elif tipo_candidato_ == "parlamento":
    SELECT_candidato = " DP.cargo_eleccion "
    WHERE_candidato = " (DP.cargo_eleccion = 'REPRESENTANTE ANTE EL PARLAMENTO ANDINO') "

  #print("SELECT_candidato: ", SELECT_candidato)
  #print("WHERE_candidato: ", WHERE_candidato)
  lista_filtros_normales = list()
  lista_filtros_ob = list()
  lista_val_new = list()
  lista_orden = list()
  lista_ids_new = list()
  lista_ids = list()
  lista_ob_dict = list()
  tienes_al_menos1 = False

  for i in range(0, len(lista_valores)-1):
    print("lista_valores[",i,"]: ", lista_valores[i])
    if lista_valores[13] != "unk" and i == 15:
      continue
    if lista_valores[i] != "unk":
      tienes_al_menos1 = True
      index_ = lista_valores[i].find('(')
      valor = lista_valores[i][index_+1:]
      lista_valores[i] = lista_valores[i] + str("_") + str(i)
      if (i >= 1 and i <= 3) or (i >= 6 and i <= 11):
        lista_filtros_ob.append(lista_valores[i])
      else:
        lista_filtros_normales.append(lista_valores[i])
      lista_val_new.append(lista_valores[i])
      lista_orden.append(valor)
    elif lista_valores[i] == "unk":
      lista_valores[i] = ""

  lista_index = list()

  if (tienes_al_menos1 == True):
    j = 1
    for i in range(0, len(lista_orden)):
      val = lista_orden.index(str(j))
      lista_index.append(val)
      j += 1
    LN = list()
    for i in lista_index:
      LN.append(lista_val_new[i])

    lista_filtros_ob_new = list()
    for i in range(0, len(LN)):
      if(LN[i] in lista_filtros_ob):
        lista_filtros_ob_new.append(LN[i])

  query_total = ""

  for i  in range(0, len(lista_valores)):
    index_ = lista_valores[i].find('(')
    if index_ != -1:  
      quitar = lista_valores[i][index_:]
      if int(valor) > 9:
        quitar = lista_valores[i][index_-2:]    
      aux = lista_valores[i].replace(quitar, "")
      lista_valores[i] = aux

  print("lista_filtros_normales: ", lista_filtros_normales)
  print("lista_filtros_ob_new: ", lista_filtros_ob_new)

  if len(lista_filtros_normales) == 0:
    print("Lista de filtros normales esta vacia")
    query_normal = ""
    query_total = function_filtros_ob(lista_filtros_ob_new,query_normal,False, SELECT_candidato,WHERE_candidato )
  
  
  elif len(lista_filtros_ob_new) == 0:
    print("Lista de filtros ob esta vacio")
    print("lista_filtros_normales: ",lista_filtros_normales)
    #caso solo 1 filtro de normales
    if len(lista_filtros_normales) == 1:
      print("if len(lista_filtros_normales) == 1:")
      query_total = query_total + function_filtro_normal(lista_valores, False, SELECT_candidato,WHERE_candidato )
    elif len(lista_filtros_normales) > 1: 
      query = ""
      print("len(lista_filtros_normales)  > 1")
      query = query + function_filtro_normal(lista_valores, True, SELECT_candidato,WHERE_candidato )
      print("query: ",query)
      for i in range(1, len(lista_filtros_normales)):
          query = query +" INTERSECT "+ function_filtro_normal(lista_valores, True, SELECT_candidato,WHERE_candidato )
      query_total = "SELECT  DISTINCT DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,   " + SELECT_candidato+ "   FROM  ( "+query + " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) WHERE " + WHERE_candidato  
  

  
  elif len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)>1:
    query_total_filtros_normales = ""
    query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
    for i in range(1, len(lista_filtros_normales)):
      query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
    filtro_ob = function_filtros_ob(lista_filtros_ob_new, "",True, SELECT_candidato,WHERE_candidato )

    for i in range(0, len(lista_filtros_ob_new)):
      index_ = lista_filtros_ob_new[i].find('_')
      valor = lista_filtros_ob_new[i][index_+1:]
      quitar = lista_filtros_ob_new[i][index_-1:]
      print("-------------")
      print("quitar: ", quitar)
      print("-------------")
      #if int(valor) > 9:
      #  quitar = lista_filtros_ob_new[i][index_-2:]
      aux = lista_filtros_ob_new[i].replace("("+quitar, "")
      lista_filtros_ob_new[i] = aux
    query_total = " SELECT  DP.id,  " + SELECT_candidato + ",  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE " + WHERE_candidato+ "  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +") ORDER BY conteo " + lista_filtros_ob_new[0]
  
  
  elif ((len(lista_filtros_normales)>1 and len(lista_filtros_ob_new) ==  1))  or  (len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)==1):
    query_total_filtros_normales = ""
    query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
    if len(lista_filtros_normales) >1:  
      for i in range(1, len(lista_filtros_normales)):
        query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
    filtro_ob = function_filtros_ob(lista_filtros_ob_new, "",True, SELECT_candidato,WHERE_candidato )
    for i in range(0, len(lista_filtros_ob_new)):
      index_ = lista_filtros_ob_new[i].find('_')
      valor = lista_filtros_ob_new[i][index_+1:]
      quitar = lista_filtros_ob_new[i][index_-1:]
      aux = lista_filtros_ob_new[i].replace("("+quitar, "")
      lista_filtros_ob_new[i] = aux
    query_total = " SELECT  DP.id,  " + SELECT_candidato + ",  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE "+ WHERE_candidato+"  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica,  "+SELECT_candidato +" ) ORDER BY conteo " + lista_filtros_ob_new[0]
  
  
  elif len(lista_filtros_normales)>1 and len(lista_filtros_ob_new)>1:
    query_total_filtros_normales = ""
    query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
    for i in range(1, len(lista_filtros_normales)):
      query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores, True, SELECT_candidato,WHERE_candidato )
    
    print("query_total_filtros_normales: ",query_total_filtros_normales)
    query_total = function_filtros_ob(lista_filtros_ob_new, query_total_filtros_normales, False, SELECT_candidato, WHERE_candidato)

  print("-----------------------------------------------------------------")
  print("query_total", query_total)
  print("-----------------------------------------------------------------")
  candidatos = DatosPersonales.objects.raw(query_total)

  # Paginator 
  paginator = Paginator(candidatos, 20)
  page_number = request.GET.get('page')

  try:
    page_obj = paginator.get_page(page_number)
  except PageNotAnInteger:
    # If page is not an integer deliver the first page
    posts = paginator.page(1)
  except EmptyPage:
    # If page is out of range deliver last page of results
    posts = paginator.page(paginator.num_pages)
  
  return render(request,
                'elecciones/dashboard.html',
                {'page': page_obj}) 

def filter_function_orga(request, filtro_id, info_extra, orden):
  #- before column name mean descending order without - mean ascending. 
  query_total = "select * from datos_personales;"
  print("################################xd###########################")
  print("filtro_id: ",filtro_id)
  print("info_extra: ",info_extra)
  print("orden: ",orden)
  candidatos = ""

  if filtro_id =="edad":
    rango = info_extra.find("-")
    var1 = info_extra[0:rango:+1] 
    var2 = info_extra[rango+1:len(filtro_id)+1:+1]
    print("var1: ", var1)
    print("var2: ", var2)
    # le falta PK
    #query_total = " SELECT  COUNT (*),partido FROM tabla_edad WHERE edad BETWEEN " +var1+ " AND " +var2+" GROUP BY (partido)"    
    #query_total = " SELECT  dni_candidato, candidato, organizacion_politica, cargo_eleccion FROM datos_personales "
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM tabla_edad  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica)  WHERE edad BETWEEN " +var1+ " AND " +var2+"  GROUP BY (OP.organizacion_politica , OP.url)  ORDER BY (conteo) "+orden

    # candidatos = OrganizacionPolitica.objects.raw ("SELECT OP.organizacion_politica ,COUNT (DP.dni_candidato) AS conteo FROM datos_personales AS DP JOIN organizaciones_politicas AS OP  USING(organizacion_politica) WHERE  sexo = 'MASCULINO' GROUP BY (OP.organizacion_politica) ORDER BY (conteo) DESC")
  
  elif filtro_id == "primaria":
    #query_total = " SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM educacion_basica WHERE concluyo_secundaria  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM educacion_basica  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_primaria  = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
    #query_total = " SELECT nombre , url from organizacion_politica"
    
  elif filtro_id == "secundaria":
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM educacion_basica  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_secundaria  = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden

  elif filtro_id == "tecnicos":
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_tecnico  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_tecnico = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
    #query_total = "SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_tecnico WHERE concluyo_estudio_tecnico  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
  
  elif filtro_id == "nouni":
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_no_universitario  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_no_universitario = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
    #query_total = "SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_no_universitario WHERE concluyo_estudio_no_universitario  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
  
  elif filtro_id == "uni":
    #query_total = "SELECT id, COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_universitario WHERE concluyo_estudio_universitario  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_universitario  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_universitario = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
  
  elif filtro_id == "postgrado":
    #query_total = "SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_postgrado WHERE concluyo_estudio_postgrado  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_postgrado  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_postgrado = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden

  elif filtro_id == "maestrodoctor":
    #query_total = "SELECT id, COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_postgrado WHERE ( es_maestro  = 'SI' OR es_doctor = 'SI') GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_postgrado  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE ( es_maestro  = 'SI' OR es_doctor = 'SI') GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden

  elif filtro_id == "genero":
    #query_total = "SELECT COUNT (DP.dni_candidato) AS conteo, OP.organizacion_politica FROM datos_personales AS DP JOIN organizaciones_politicas AS OP USING(organizacion_politica) WHERE  sexo = '" + info_extra+ "' GROUP BY (OP.organizacion_politica) ORDER BY (conteo) " + orden
    query_total =" SELECT OP.organizacion_politica , OP.url , COUNT (DP.dni_candidato) AS conteo FROM datos_personales AS DP JOIN organizaciones_politicas AS OP USING(organizacion_politica) WHERE sexo = '"+info_extra+"' GROUP BY (OP.organizacion_politica) ORDER BY (conteo)  "+ orden

  elif filtro_id == "cant_sen_penal_obliga":
    #query_total = " SELECT id,SUM(conteo) AS total, organizacion_politica FROM (SELECT  COUNT(dni_candidato) AS conteo, organizacion_politica  FROM sentencia_penal   WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica) UNION ALL SELECT  COUNT(dni_candidato) AS conteo, organizacion_politica  FROM sentencia_obligacion   WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica)) TABLA GROUP BY partido ORDER BY total " +orden 
    query_total= "SELECT SUM(conteo) AS total, organizacion_politica FROM (SELECT  COUNT(dni_candidato) AS conteo , organizacion_politica FROM sentencia_penal WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica) UNION ALL SELECT  COUNT(dni_candidato) AS conteo , organizacion_politica  FROM sentencia_obligacion WHERE  tiene_info_por_declarar   = 'SI' GROUP BY (organizacion_politica)) TABLA GROUP BY organizacion_politica ORDER BY total "+orden
    #query_total = " SELECT OP.organizacion_politica, OP.url, COUNT (DP.dni_candidato)  AS conteo FROM sentencia_penal AS DP JOIN organizaciones_politicas AS OP USING(organizacion_politica) WHERE DP.tiene_info_por_declarar= 'SI' "
  
  elif filtro_id =="cant_sen_penal":
    #query_total = " SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM sentencia_penal WHERE  tiene_info_por_declarar   = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) "+orden
    query_total = " SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM sentencia_penal  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE tiene_info_por_declarar   = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
  
  elif filtro_id =="cant_sen_civil":
    query_total = " SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM sentencia_obligacion  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE tiene_info_por_declarar   = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
    #query_total = "SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM sentencia_obligacion  WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) "+orden
  
  elif filtro_id =="org_oriundo":
    #query_total = "SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica FROM datos_personales  WHERE departamento_nacimiento = '"+ info_extra+"' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    query_total =" SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM datos_personales  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE departamento_nacimiento = '"+ info_extra+"' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden
  
  elif filtro_id =="elecvsnacimiento_name":
    #query_total = "SELECT id,COUNT (dni_candidato) AS conteo, organizacion_politica  FROM datos_personales  WHERE departamento_nacimiento <> distrito_elec AND  distrito_elec <> 'PERUANOS RESIDENTES EN EL EXTRANJERO' AND distrito_elec <> 'LIMA PROVINCIAS' GROUP BY (organizacion_politica,id) ORDER BY (conteo) "+orden
    query_total = " SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM datos_personales  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE departamento_nacimiento <> distrito_elec AND  distrito_elec <> 'PERUANOS RESIDENTES EN EL EXTRANJERO' AND distrito_elec <> 'LIMA PROVINCIAS' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) "+orden

  elif filtro_id =="2019priv":
    query_total =  "SELECT total_ingresos AS monto, OP.organizacion_politica FROM financiamiento_privado AS EB  JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE  estado   = '"+info_extra+"' AND  anhio = '2019' GROUP BY (OP.organizacion_politica,monto,OP.url) ORDER BY (monto) "+orden

  elif filtro_id =="2018priv":
    query_total =  "SELECT total_ingresos AS monto, OP.organizacion_politica FROM financiamiento_privado AS EB  JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE  estado   = '"+info_extra+"' AND  anhio = '2018' GROUP BY (OP.organizacion_politica,monto,OP.url) ORDER BY (monto) "+orden

  elif filtro_id =="2017priv":
    query_total =  "SELECT total_ingresos AS monto, OP.organizacion_politica FROM financiamiento_privado AS EB  JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE  estado   = '"+info_extra+"' AND  anhio = '2017' GROUP BY (OP.organizacion_politica,monto,OP.url) ORDER BY (monto) "+orden

  elif filtro_id =="monto_quinque":
    query_total =  " SELECT monto_quinquenal AS monto, OP.organizacion_politica, EB.num_votos_congresales FROM financiamiento_publico AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) GROUP BY (EB.num_votos_congresales,OP.organizacion_politica,monto,OP.url) ORDER BY (monto) "+orden

  print("-------LLEGA A FINAL CASI DE LA FUNCION------------")
  print("query_total: ",query_total)
  ##candidatos = DatosPersonales.objects.raw("SELECT * FROM datos_personales")
  #candidatos = DatosPersonales.objects.raw(query_total)
  candidatos = OrganizacionesPoliticas.objects.raw(query_total)
  # Paginator 
  paginator = Paginator(candidatos, 20)
  page_number = request.GET.get('page')
  #page_number = request.GET.get('page')

  try:
      page_obj = paginator.get_page(page_number)
  except PageNotAnInteger:
      # If page is not an integer deliver the first page
      posts = paginator.page(1)
  except EmptyPage:
      # If page is out of range deliver last page of results
      posts = paginator.page(paginator.num_pages)

  return render(request,
                'elecciones/dashboard.html',
                {
                  'page': page_obj,
                  'organizaciones_return': page_obj
                } )

def candidatos(request):
  candidatos = DatosPersonales.objects.raw(
    "select * from datos_personales;"
  )
    
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos': candidatos})

def hojadevida_by_dni(request, dni_hoja_de_vida, cargo_postula_dato):
  #expertiencia laboral = ExperienciaLaboral.objects.raw()
  # if cargo_postula_dato == "favicon.png":
  #     return
  # print("dni_hoja_de_vida: ",dni_hoja_de_vida)
  # print("----cargo_eleccion_-----: ",cargo_postula_dato)
  #if (len(dni_hoja_de_vida)>8 or len(cargo_eleccion_)>13):
  #    return 
  if cargo_postula_dato == "PRIMER":
      cargo_postula_dato ="PRIMER VICEPRESIDENTE DE LA REPÚBLICA"
  elif cargo_postula_dato =="PRESIDENTE":
      cargo_postula_dato = "PRESIDENTE DE LA REPÚBLICA"
  elif cargo_postula_dato == "SEGUNDO":
      cargo_postula_dato = "SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA"
  elif cargo_postula_dato == "REPRESENTANTE":
      cargo_postula_dato = "REPRESENTANTE ANTE EL PARLAMENTO ANDINO"
  elif cargo_postula_dato== "CONGRESISTA":
      cargo_postula_dato= "CONGRESISTA DE LA REPÚBLICA"
  elif cargo_postula_dato == "PRIMER":
      cargo_postula_dato = "PRIMER VICEPRESIDENTE DE LA REPÚBLICA"

  print("dni_hoja_de_vida: ",dni_hoja_de_vida)     
  nombre_ = DatosPersonales.objects.raw("SELECT DP.id, DP.candidato, OP.url FROM datos_personales as DP INNER JOIN organizaciones_politicas as OP on DP.organizacion_politica = OP.organizacion_politica AND dni_candidato = '" +dni_hoja_de_vida+  "' LIMIT 1")
  datos_personales_ = DatosPersonales.objects.raw("SELECT DISTINCT * FROM datos_personales WHERE dni_candidato = '" +dni_hoja_de_vida+  "' LIMIT 1 ")
  cargo_eleccion_ = DatosPersonales.objects.raw("SELECT  id,cargo_eleccion FROM datos_personales WHERE dni_candidato = '" +dni_hoja_de_vida+  "'")  
  
  ifexpe_ = ExperienciaLaboral.objects.raw("SELECT DISTINCT DP.id, EP.tiene_experiencia_laboral FROM experiencia_laboral AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "' ")
  experiencia_laboral_ = ExperienciaLaboral.objects.raw("SELECT DISTINCT DP.id, centro_laboral, tiene_experiencia_laboral, ocupacion,ruc_empresa_laboral, direccion_laboral, desde_anhio,hasta_anhio,pais_laboral,departamento_laboral,provincia_laboral FROM experiencia_laboral AS EP  RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  
  edubasica_ = EducacionBasica.objects.raw("SELECT * from educacion_basica where dni_candidato ='"+dni_hoja_de_vida+"' LIMIT 1")
  
  edu_tecnic_ = EstudioTecnico.objects.raw("SELECT DISTINCT DP.id, EP.tiene_estudio_tecnico FROM estudio_tecnico AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE EP.centro_estudio_tecnico != 'null' AND  DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  estudios_en_institutos_ = EstudioTecnico.objects.raw("SELECT DISTINCT DP.id, carrera_tecnica, centro_estudio_tecnico, concluyo_estudio_tecnico, comentario_estudio_tecnico FROM estudio_tecnico AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  edu_uni_ = EstudioUniversitario.objects.raw("SELECT DISTINCT DP.id, EP.tiene_estudio_universitario  FROM estudio_universitario AS EP  RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  estudio_univs = EstudioUniversitario.objects.raw("SELECT DISTINCT DP.id, tiene_estudio_universitario, carrera_universitaria, anhio_obtencion_universitario, universidad, concluyo_estudio_universitario, comentario_estudio_universitario FROM estudio_universitario AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
    
  edu_no_uni_ = EstudioNoUniversitario.objects.raw("SELECT DISTINCT DP.id, EP.tiene_estudio_no_universitario  FROM estudio_no_universitario AS EP  RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  estudios_no_universitarios_ = EstudioNoUniversitario.objects.raw("SELECT DISTINCT DP.id, centro_estudio_no_universitario, concluyo_estudio_no_universitario FROM estudio_no_universitario AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  edu_post_ = EstudioPostgrado.objects.raw("SELECT DISTINCT DP.id, EP.tiene_postgrado  FROM estudio_postgrado AS EP  RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE  DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  estudios_en_postgrado_ = EstudioPostgrado.objects.raw("SELECT DISTINCT DP.id, tiene_postgrado, especialidad, centro_estudio_postgrado, concluyo_estudio_postgrado, es_maestro, es_doctor,anhio_obtencion_postgrado, comentario_estudio_postgrado, es_egresado_postgrado FROM estudio_postgrado AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  
  carg_eleccion_pop_ = CargoEleccion.objects.raw("SELECT DISTINCT DP.id, CE.tiene_info_por_declarar FROM cargo_eleccion AS CE  RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  cargo_eleccion_popular_ = CargoEleccion.objects.raw("SELECT DISTINCT DP.id, CE.tiene_info_por_declarar, CE.org_politica_cargo, CE.organizacion_politica,CE.cargo, CE.desde_anhio, CE.hasta_anhio, CE.comentario FROM cargo_eleccion AS CE RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion = '"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  
    
  renuncias_ = Renuncia.objects.raw("SELECT DISTINCT DP.id, EP.organización_renuncia, EP.comentario FROM renuncia AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
  ifreuncia_ = Renuncia.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_por_declarar FROM renuncia AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  if_penal_ = SentenciaPenal.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_por_declarar FROM sentencia_penal AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "' ")
  sentencia_penales_ = SentenciaPenal.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_por_declarar, EP.fallo_penal, EP.cumplimiento_del_fallo, EP.modalidad_penal  ,EP.n_experiente_penal, EP.fecha_sentencia_penal, EP.organo_judicial FROM sentencia_penal AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  if_oblig_ = SentenciaObligacion.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_por_declarar FROM sentencia_obligacion AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "' ")
  sentencia_obliga_ = SentenciaObligacion.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_por_declarar, EP.materia_sentencia, EP.fallo_obliga, EP.n_experiente_obliga, EP.organo_judicial FROM sentencia_obligacion AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  # si es que tiene ingresos, solo da DP.id, EP.tiene_ingresos 
  if_ingreso_ = Ingreso.objects.raw("SELECT DISTINCT DP.id, EP.tiene_ingresos FROM ingreso AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "' ")
  # el ingreso en cierto año da columnas EP.anhio_ingresos, EP.total_ingresos
  ingresos_ = Ingreso.objects.raw("SELECT DISTINCT DP.id, EP.anhio_ingresos, EP.total_ingresos FROM ingreso AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  # si es que tiene que declarar bienes inmuebles solo da dp.id, 
  if_bien_inmueble_ = BienInmueble.objects.raw("SELECT DISTINCT DP.id, EP.tiene_inmueble FROM bien_inmueble AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "' ")
  # los bienes inmuebles da columnas EP.tipo_inmueble, EP.direccion_inmueble,EP.esta_inscrito_sunarp, EP.partida_inmueble_sunarp ,EP.comentario_inmueble  
  bienes_inmuebles_ = BienInmueble.objects.raw("SELECT DISTINCT DP.id, EP.tiene_inmueble, EP.tipo_inmueble, EP.direccion_inmueble,EP.esta_inscrito_sunarp, EP.partida_inmueble_sunarp ,EP.comentario_inmueble FROM bien_inmueble AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
 
  if_bien_mueble_ = BienMueble.objects.raw("SELECT DISTINCT DP.id, EP.tiene_bien_mueble FROM bien_mueble AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "' ")
  bienes_muebles_ = BienMueble.objects.raw("SELECT DISTINCT DP.id, EP.tiene_bien_mueble, EP.vehiculo, EP.placa,EP.valor, EP.caracteristicas_vehiculo ,EP.comentario_vehiculo FROM bien_mueble AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  informacio_adicional_ = InformacionAdicional.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_adicional, EP.info FROM informacion_adicional AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")

  return render(request, 'elecciones/hdv.html', {
                  'nombre': nombre_,
                  'datos_personales': datos_personales_,
                  'cargo_eleccion': cargo_eleccion_,
                  'ifexpe': ifexpe_,
                  'experiencia_laboral': experiencia_laboral_,
                  'educacion_basica': edubasica_,
                  'estudio_tecnico': edu_tecnic_,
                  'estudio_no_univ':  edu_no_uni_,
                  'estudio_univ': edu_uni_,
                  'estudio_postgrado': edu_post_,
                  'estudios_en_institutos': estudios_en_institutos_,
                  'estudios_en_la_u': estudio_univs,
                  'estudios_no_universitarios': estudios_no_universitarios_,
                  'estudios_en_postgrado': estudios_en_postgrado_,
                  'carg_eleccion_pop': carg_eleccion_pop_,
                  'cargo_eleccion_popular': cargo_eleccion_popular_,
                  'ifreuncia':ifreuncia_,
                  'renuncias': renuncias_,
                  'if_penal': if_penal_,
                  'setencia_penales': sentencia_penales_,
                  'if_oblig':if_oblig_,
                  'sentencia_obliga':sentencia_obliga_,
                  'if_ingreso': if_ingreso_,
                  'ingresos': ingresos_,
                  'if_bien_inmueble':if_bien_inmueble_,
                  'bienes_inmuebles':bienes_inmuebles_,
                  'if_bien_mueble':if_bien_mueble_ ,
                  'bienes_muebles':bienes_muebles_,
                  'informacio_adicional':informacio_adicional_
                })

def mainpage(request):
  return render(request,'elecciones/landingpage.html',{})

def analisisGraficos(request):
  return render(request,'elecciones/graphics.html',{})

def analisisGraficosPresi(request):
  return render(request, 'elecciones/graphics-presi.html',{})

def test(request):
  print('////////////////////////////')
  print(request.method)
  print('////////////////////////////')

    