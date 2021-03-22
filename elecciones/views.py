from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from itertools import chain
from .models import *

def function_filtros_ob(self, query_normal, normnob1, SELECT_candidato, WHERE_candidato):
  query_total = ""
  subquery_list = list()
  for i in range(0, len(self)):
    index_ = self[i].find('_')
    indice = self[i].rfind("-")
    valor = self[i][index_+1:]
    nrorden = self[i][indice+1:indice+3:1]
    uwu = nrorden.find("_")
    quitar = self[i][index_-1:]

    # print("-------------------- VALOR DEL QUERY -----------------------")
    # print(valor)
    # print("-------------------- ORDEN DEL VALOR -----------------------")
    # print(nrorden)

    if int(valor) > 9 and uwu==-1:
      quitar = self[i][index_-2:]
    aux = self[i].replace("-"+quitar, "") 
    self[i] = aux

    if valor == "1":
      if len(self) > 1 or normnob1 == True: #cargos previos
        subquery = "SELECT DP.id, SUM(CE.total_anhio_eleccion) AS conteo, DP.dni_candidato FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND "+ WHERE_candidato+ " GROUP BY (DP.id, DP.dni_candidato)  "       
        subquery_list.append(subquery)
      else:
        subquery = "SELECT DP.id, SUM( CE.total_anhio_eleccion )AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "  +  SELECT_candidato + " FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND "  + WHERE_candidato + "  GROUP BY (  Dp.id, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+ ") ORDER BY conteo " +self[i]
        return subquery
    elif valor == "2":# cant sentencia penal 
      if len(self) >1 or normnob1 == True :
        subquery =   "SELECT DP.id, COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND " + WHERE_candidato+" GROUP BY (DP.id,DP.dni_candidato)  "
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT DP.id, COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "+ SELECT_candidato  +"  FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  " +  WHERE_candidato  +" GROUP BY (Dp.id, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo  " +self[i] 
        return subquery                            
    elif valor == "3": #cantidad sentencia obligaciones
      if len(self) >1 or normnob1 == True :
        subquery = "SELECT DP.id, COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  " +   WHERE_candidato +    " GROUP BY (DP.id,DP.dni_candidato) "
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT  DP.id, COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +  " FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND " +  WHERE_candidato +"   GROUP BY (" + SELECT_candidato + ", DP.dni_candidato,DP.candidato, DP.organizacion_politica, DP.id) ORDER BY conteo  " +self[i]
        return subquery
    elif valor == "6":#cantidad ingresos
      subquery = "SELECT  DP.id,total_ingresos AS  conteo, DP.dni_candidato FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND "+ WHERE_candidato +"  GROUP BY (DP.id,  DP.dni_candidato, conteo) "
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT DP.id, total_ingresos AS  conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica," + SELECT_candidato  +   " FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND "+ WHERE_candidato +" GROUP BY ( DP.id,DP.dni_candidato, total_ingresos, DP.candidato, DP.organizacion_politica, "  +  SELECT_candidato +") ORDER BY conteo "  + self[i]
        return subquery
    elif valor == "7":#cantidad inmueble
      subquery = "SELECT  DP.id,COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND "+ WHERE_candidato+"  GROUP BY (DP.id,DP.dni_candidato) " 
      if len(self) >1 or ( normnob1 == True):
        subquery_list.append(subquery)
      else:
        subquery = "SELECT  DP.id, COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+" FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND " + WHERE_candidato+"  GROUP BY (DP.id,DP.dni_candidato, DP.candidato, DP.organizacion_politica," + SELECT_candidato+ ") ORDER BY conteo " + self[i]             
        return subquery            
    elif valor == "8":  #valor inmuebles
      subquery = "SELECT DP.id, SUM (BI.autovaluo) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND  "+   WHERE_candidato +"  GROUP BY (DP.id,DP.dni_candidato)  "
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT  DP.id,SUM (BI.autovaluo) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +"  FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND " + WHERE_candidato+ " GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.id, "+ SELECT_candidato +" ) ORDER BY conteo " + self[i]
        return subquery 
    elif valor == "9" : # cantidad muebles
      subquery = "SELECT DP.id,COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble  = 'SI' AND  "+  WHERE_candidato +  " GROUP BY (DP.id,DP.dni_candidato) " 
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT DP.id,COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+ " FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  " +  WHERE_candidato+ " GROUP BY (DP.id,DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+SELECT_candidato+"  ) ORDER BY conteo "+self [i]                
        return subquery
    elif valor == "10"  : #valor muebles
      subquery = "SELECT DP.id, SUM (BM.valor ) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND " + WHERE_candidato+ " GROUP BY (DP.id,DP.dni_candidato)  " 
      if len(self) >1 or normnob1 == True :
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT DP.id,SUM (BM.valor ) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+" FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND "  + WHERE_candidato+ " GROUP BY (DP.id,DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+ SELECT_candidato+" ) ORDER BY conteo  " + self[i]
        return subquery
    elif valor == "11": #renuncias
      subquery = "SELECT DP.id,COUNT(R.dni_candidato) AS conteo, DP.dni_candidato FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  "+WHERE_candidato+" GROUP BY (DP.id,DP.dni_candidato)  "
      if len(self) >1 or normnob1 == True:
        subquery_list.append(subquery)
      else: 
        subquery = "SELECT  DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica, " + SELECT_candidato+", COUNT(R.dni_candidato) AS conteo FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND "+ WHERE_candidato+" GROUP BY ( DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo "+ self[i]                
        return subquery

  #return subquery_list
  if normnob1 == True:
    return subquery_list
  SELECT = "SELECT DP.id,  DP.candidato,DP.dni_candidato, DP.organizacion_politica,  "+ SELECT_candidato 
  WHERE = " WHERE  "+ WHERE_candidato
  Qs = "" 
  ORDER_BY = ""

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
  for i in range(0, len(subquery_list)):          
    if i == 0 and query_normal != "":
      FROM = " FROM ( " + query_normal+ " ) AS  QN JOIN datos_personales AS DP USING (dni_candidato) "  
    if i == 0 and query_normal == "":
      FROM = " FROM ("+ subquery_list[i] +" ) AS "+" Q"+str(i+1)+ " JOIN datos_personales AS DP USING (dni_candidato) "     
      continue
    FROM = FROM + " JOIN ("+subquery_list[i]   +" ) AS Q" +str(i+1)+ " USING (dni_candidato) "    
  ORDER_BY = " ORDER BY "+Qs_
  query_total = SELECT + ", " + Qs + FROM + WHERE + GROUP_BY_ + ORDER_BY


  return query_total

def function_filtro_normal(self, stack_, SELECT_candidato, WHERE_candidato):
  if stack_== False:
    if self[0] != "":
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
      # print("SELF >>>>>>>>>>>>>>>>>>>>>>>>> ", self[12])
      # print("Primer numero >>>>>>>>>>>>>>>>>>>>>>>>> ",(self[12])[:2])
      # print("Segundo numero >>>>>>>>>>>>>>>>>>>>>>>>> ",(self[12])[3:5])
      retorno = "SELECT DISTINCT DP.id,  DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+ SELECT_candidato+"  FROM tabla_edad AS TE JOIN  datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + (self[12])[3:5] + " AND  "+WHERE_candidato
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
      # print("self[0]: ",self[0])
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
      retorno = "SELECT  DISTINCT  DP.dni_candidato FROM tabla_edad AS TE JOIN datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + ( self[12])[3:5] + " AND "+ WHERE_candidato
      self[12] = ""
      return retorno
    if self[13] == "SI":
      retorno = "SELECT DISTINCT  DP.dni_candidato FROM  datos_personales AS DP WHERE departamento_nacimiento = '" + self[15] + "' AND  "+ WHERE_candidato 
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

def unkipify(value):
  return value if value != None else "unk"

def filter_function(request):
  # Tipo de Filtro
  tipo_candidato_ = unkipify(request.GET.get("tipo_filter"))

  # Si son candidatos
  if(tipo_candidato_ != 'org_politca'):
    ###############################################
    # Variables
    ###############################################
    # Candidatos
    nivel_academico = unkipify(request.GET.get("nivel_academico"))
    cargos_previos_order = unkipify(request.GET.get("anhio_servicio"))
    orden_cant_sentencia = unkipify(request.GET.get("cant_senten"))
    orden_cant_sentencia_oblig = unkipify(request.GET.get("cant_senten_oblig"))
    mat_demanda = unkipify(request.GET.get("opc_mat_demanda"))
    if(request.GET.get("ifsentencias") != None): # si o no, (se tuvo que hacer así xd)
      if(request.GET.get("ifsentencias") == "si"):
        no_tiene_sentencias = "unk"
      else:
        no_tiene_sentencias = request.GET.get("ifsentencias")
    else:
      no_tiene_sentencias = "unk"
    tipo_sentencia = unkipify(request.GET.get("tipo_sentencia"))
    orden_cant_ingreso = unkipify(request.GET.get("cant_ingreso"))
    orden_cant_inmueble = unkipify(request.GET.get("cant_inmuebles"))
    orden_valor_inmueble = unkipify(request.GET.get("valor_inmuebles"))
    orden_cant_mueble = unkipify(request.GET.get("cant_muebles"))
    orden_valor_mueble = unkipify(request.GET.get("valor_muebles"))
    orden_renuncias = unkipify(request.GET.get("cantidad_renuncia"))
    rango_edad_val = unkipify(request.GET.get("rango_edad"))
    print(">>>>>>>>>>>>>>> Rango edad", rango_edad_val)
    if(request.GET.get("oriundo_input") != None):
      index = request.GET.get("oriundo_input").rfind("-")
      ordxr = request.GET.get("oriundo_input")[index : len(request.GET.get("oriundo_input"))]
      if(request.GET.get("oriundo_input")[0: index] == "NO"):
        nacio_en_peru_no = "NO" + ordxr
        nacio_en_peru_si = "unk"
      else:
        nacio_en_peru_si = "SI" + ordxr
        nacio_en_peru_no = "unk"
    else:
      nacio_en_peru_no = "unk"
      nacio_en_peru_si = "unk"
    departamento_nacimiento = unkipify(request.GET.get("departamento_nacimiento"))
    cargo_postula = unkipify(request.GET.get("cargo_al_que_postula"))
    org_politica = unkipify(request.GET.get("org_politica"))
    dist_electoral = unkipify(request.GET.get("dist_electoral"))

    ###############################################
    # XD
    ###############################################
    lista_valores = [
      nivel_academico, cargos_previos_order, orden_cant_sentencia,
      orden_cant_sentencia_oblig, mat_demanda, no_tiene_sentencias, 
      orden_cant_ingreso, orden_cant_inmueble, orden_valor_inmueble,
      orden_cant_mueble, orden_valor_mueble, orden_renuncias, 
      rango_edad_val, nacio_en_peru_si, nacio_en_peru_no, 
      departamento_nacimiento, cargo_postula, org_politica, 
      dist_electoral, tipo_candidato_
    ]

    # print("********")
    # print(lista_valores)
    # print("********")

    if(lista_valores[4][0:lista_valores[4].rfind("-")] == "FamiliaAli"):
      order = lista_valores[4][lista_valores[4].rfind("-"):len(lista_valores[4]) :+1]
      lista_valores[4] = "FAMILIA / ALIMENTARIA" + order

    SELECT_candidato = ""
    WHERE_candidato = ""
    GROUP_by = ""

    if tipo_candidato_ == "presidenciales":
      SELECT_candidato =  " DP.cargo_eleccion "
      WHERE_candidato = " (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion = 'PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
    elif tipo_candidato_ == "congresales":
      SELECT_candidato = " DP.distrito_elec "
      WHERE_candidato = " (DP.cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') "
    elif tipo_candidato_ == "parlamento":
      SELECT_candidato = " DP.cargo_eleccion "
      WHERE_candidato = " (DP.cargo_eleccion = 'REPRESENTANTE ANTE EL PARLAMENTO ANDINO') "

    lista_filtros_normales = list()
    lista_filtros_ob = list()
    lista_val_new = list()
    lista_orden = list()
    lista_ids_new = list()
    lista_ids = list()
    lista_ob_dict = list()
    lista_index = list()
    tienes_al_menos1 = False
    query_total = ""

    for i in range(0, len(lista_valores)-1):
      # print("lista_valores[",i,"]: ", lista_valores[i])
      if lista_valores[13] != "unk" and i == 15:
        continue
      if lista_valores[i] != "unk":
        tienes_al_menos1 = True
        index_ = lista_valores[i].rfind("-")
        # if(i != 15):
        valor = lista_valores[i][index_+1:]
        lista_valores[i] = lista_valores[i] + str("_") + str(i)
        if (i >= 1 and i <= 3) or (i >= 6 and i <= 11):
          lista_filtros_ob.append(lista_valores[i])
        else:
          lista_filtros_normales.append(lista_valores[i])
        lista_val_new.append(lista_valores[i])
        # if(i != 15): # Evitar que el departamento no se appendee en la lista de orden
        lista_orden.append(valor)
      elif lista_valores[i] == "unk":
        lista_valores[i] = ""

    if(tienes_al_menos1):
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

      for i in range(0, len(lista_valores)):
        index_ = lista_valores[i].rfind("-")
        if index_ != -1:
          quitar = lista_valores[i][index_:]
          if int(valor) > 9:
            quitar = lista_valores[i][index_-2:]    
          aux = lista_valores[i].replace(quitar, "")
          lista_valores[i] = aux


      if len(lista_filtros_normales) == 0:
        # print("*********** Lista de filtros normales esta vacia")
        query_normal = ""
        query_total = function_filtros_ob(lista_filtros_ob_new, query_normal,False, SELECT_candidato, WHERE_candidato)
      
      elif len(lista_filtros_ob_new) == 0:
        if len(lista_filtros_normales) == 1:
          # print("query_total XXXX********",query_total)
          # print("********")
          # print("lista_valores********",lista_valores)
          # print("********")
          # print("SELECT_candidato********",SELECT_candidato)
          # print("********")
          # print("WHERE_candidato********",WHERE_candidato)
          # print("********")
          query_total = query_total + function_filtro_normal(lista_valores, False, SELECT_candidato, WHERE_candidato)
        elif len(lista_filtros_normales) > 1:
          query = ""
          query = query + function_filtro_normal(lista_valores, True, SELECT_candidato, WHERE_candidato)
          for i in range(1, len(lista_filtros_normales)):
            query = query +" INTERSECT "+ function_filtro_normal(lista_valores, True, SELECT_candidato, WHERE_candidato)
          query_total = "SELECT  DISTINCT DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,   " + SELECT_candidato+ "   FROM  ( "+query + " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) WHERE " + WHERE_candidato  

      elif len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)>1:
        query_total_filtros_normales = ""
        query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato, WHERE_candidato)
        for i in range(1, len(lista_filtros_normales)):
          query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores,True, SELECT_candidato, WHERE_candidato)
        filtro_ob = function_filtros_ob(lista_filtros_ob_new, "",True, SELECT_candidato, WHERE_candidato)

        for i in range(0, len(lista_filtros_ob_new)):
          index_ = lista_filtros_ob_new[i].find('_')
          valor = lista_filtros_ob_new[i][index_+1:]
          quitar = lista_filtros_ob_new[i][index_-1:]
          aux = lista_filtros_ob_new[i].replace("-"+quitar, "")
          lista_filtros_ob_new[i] = aux
        query_total = "SELECT  DP.id,  " + SELECT_candidato + ",  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE " + WHERE_candidato+ "  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +") ORDER BY conteo " + lista_filtros_ob_new[0]

      elif ((len(lista_filtros_normales)>1 and len(lista_filtros_ob_new) ==  1))  or  (len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)==1):
        query_total_filtros_normales = ""
        query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato, WHERE_candidato)
        if len(lista_filtros_normales) >1:  
          for i in range(1, len(lista_filtros_normales)):
            query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores,True, SELECT_candidato, WHERE_candidato)
        filtro_ob = function_filtros_ob(lista_filtros_ob_new, "",True, SELECT_candidato, WHERE_candidato)
        for i in range(0, len(lista_filtros_ob_new)):
          index_ = lista_filtros_ob_new[i].find('_')
          valor = lista_filtros_ob_new[i][index_+1:]
          quitar = lista_filtros_ob_new[i][index_-1:]
          aux = lista_filtros_ob_new[i].replace("-"+quitar, "")
          lista_filtros_ob_new[i] = aux
        query_total = "SELECT  DP.id,  " + SELECT_candidato + ",  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE "+ WHERE_candidato+"  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica,  "+SELECT_candidato +" ) ORDER BY conteo " + lista_filtros_ob_new[0]
      
      elif len(lista_filtros_normales)>1 and len(lista_filtros_ob_new)>1:
        query_total_filtros_normales = ""
        query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato, WHERE_candidato)
        for i in range(1, len(lista_filtros_normales)):
          query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores, True, SELECT_candidato, WHERE_candidato)
        
        query_total = function_filtros_ob(lista_filtros_ob_new, query_total_filtros_normales, False, SELECT_candidato, WHERE_candidato)

      #print("-----------------------------------------------------------------")
      #print("query_total", query_total)
      #print("-----------------------------------------------------------------")
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

    else:
      return render(request, 'elecciones/dashboard.html') 

  # Si son org políticas
  else:
    ###############################################
    # Variables
    ###############################################
    # Org Politica
    org_rango_edad = unkipify(request.GET.get("org_rango_edad"))
    org_edad_orden = unkipify(request.GET.get("org_edad_orden"))
    org_educacion_prim_ord = unkipify(request.GET.get("org_educacion_prim"))
    org_educacion_sec_ord = unkipify(request.GET.get("org_educacion_sec"))
    org_educacion_tec_ord = unkipify(request.GET.get("org_educacion_tec"))
    org_educacion_no_univ_ord = unkipify(request.GET.get("org_educacion_no_univ"))
    org_educacion_univ_ord = unkipify(request.GET.get("org_educacion_univ"))
    org_educacion_post_ord = unkipify(request.GET.get("org_educacion_post"))
    org_educacion_doc_ord = unkipify(request.GET.get("org_educacion_doc"))
    org_opc_sexo = unkipify(request.GET.get("org_opc_sexo"))
    org_sexo_orden = unkipify(request.GET.get("org_sexo_orden"))
    org_cant_sen_penal_obliga = unkipify(request.GET.get("cant_sen_penal_obliga"))
    org_cant_sen_penal = unkipify(request.GET.get("cant_sen_penal"))
    org_cant_sen_civil = unkipify(request.GET.get("cant_sen_civil"))
    org_oriundo = unkipify(request.GET.get("org_oriundo"))
    org_departamento_oriundo = unkipify(request.GET.get("org_departamento_oriundo"))
    org_distrito_electoral = unkipify(request.GET.get("org_distrito_electoral"))
    org_2019_finan_priv_presento = unkipify(request.GET.get("2019_est_present"))
    org_2019_finan_priv_orden_ingreso = unkipify(request.GET.get("2019_ingre_dec"))
    org_2018_finan_priv_presento = unkipify(request.GET.get("2018_est_present"))
    org_2018_finan_priv_orden_ingreso = unkipify(request.GET.get("2018_ingre_dec"))
    org_2017_finan_priv_presento = unkipify(request.GET.get("2017_est_present"))
    org_2017_finan_priv_orden_ingreso = unkipify(request.GET.get("2017_ingre_dec"))
    org_finan_pub_orden_monto_quinquenal = unkipify(request.GET.get("monto_quinque"))

    #- before column name mean descending order without - mean ascending. 
    query_total = "select * from datos_personales;"

    if org_rango_edad != "unk":
      rango = org_rango_edad.rfind("-")
      var1 = org_rango_edad[0:rango:+1] 
      var2 = org_rango_edad[rango+1:len(org_rango_edad)+1:+1]

      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM tabla_edad  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica)  WHERE edad BETWEEN " +var1+ " AND " +var2+"  GROUP BY (OP.organizacion_politica , OP.url)  ORDER BY (conteo) " + org_edad_orden
    
    elif org_educacion_prim_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM educacion_basica  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_primaria  = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_prim_ord
      
    elif org_educacion_sec_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM educacion_basica  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_secundaria  = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_sec_ord

    elif org_educacion_tec_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_tecnico  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_tecnico = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_tec_ord
    
    elif org_educacion_no_univ_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_no_universitario  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_no_universitario = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_no_univ_ord
    
    elif org_educacion_univ_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_universitario  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_universitario = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_univ_ord
    
    elif org_educacion_post_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_postgrado  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE concluyo_estudio_postgrado = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_post_ord

    elif org_educacion_doc_ord != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM estudio_postgrado  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE ( es_maestro  = 'SI' OR es_doctor = 'SI') GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_educacion_doc_ord

    elif org_opc_sexo != "unk":
      query_total = "SELECT OP.organizacion_politica , OP.url , COUNT (DP.dni_candidato) AS conteo FROM datos_personales AS DP JOIN organizaciones_politicas AS OP USING(organizacion_politica) WHERE sexo = '"+org_opc_sexo+"' GROUP BY (OP.organizacion_politica) ORDER BY (conteo)  " + org_sexo_orden

    elif org_cant_sen_penal_obliga != "unk":
      query_total= "SELECT SUM(conteo) AS total, organizacion_politica FROM (SELECT  COUNT(dni_candidato) AS conteo , organizacion_politica FROM sentencia_penal WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica) UNION ALL SELECT  COUNT(dni_candidato) AS conteo , organizacion_politica  FROM sentencia_obligacion WHERE  tiene_info_por_declarar   = 'SI' GROUP BY (organizacion_politica)) TABLA GROUP BY organizacion_politica ORDER BY total " + org_cant_sen_penal_obliga
    
    elif org_cant_sen_penal != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM sentencia_penal  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE tiene_info_por_declarar   = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_cant_sen_penal
    
    elif org_cant_sen_civil != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM sentencia_obligacion  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE tiene_info_por_declarar   = 'SI' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_cant_sen_civil
    
    elif org_oriundo != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM datos_personales  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE departamento_nacimiento = '"+ org_departamento_oriundo +"' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_oriundo
    
    elif org_distrito_electoral != "unk":
      query_total = "SELECT COUNT (dni_candidato) AS conteo, OP.organizacion_politica , OP.url FROM datos_personales  AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE departamento_nacimiento <> distrito_elec AND  distrito_elec <> 'PERUANOS RESIDENTES EN EL EXTRANJERO' AND distrito_elec <> 'LIMA PROVINCIAS' GROUP BY (OP.organizacion_politica , OP.url) ORDER BY (conteo) " + org_distrito_electoral

    elif org_2019_finan_priv_presento != "unk":
      query_total = "SELECT total_ingresos AS monto, OP.organizacion_politica FROM financiamiento_privado AS EB  JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE  estado   = '"+org_2019_finan_priv_presento+"' AND  anhio = '2019' GROUP BY (OP.organizacion_politica,monto,OP.url) ORDER BY (monto) " + org_2019_finan_priv_orden_ingreso

    elif org_2018_finan_priv_presento != "unk":
      query_total = "SELECT total_ingresos AS monto, OP.organizacion_politica FROM financiamiento_privado AS EB  JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE  estado   = '"+org_2018_finan_priv_presento+"' AND  anhio = '2018' GROUP BY (OP.organizacion_politica,monto,OP.url) ORDER BY (monto) " + org_2018_finan_priv_orden_ingreso

    elif org_2017_finan_priv_presento != "unk":
      query_total = "SELECT total_ingresos AS monto, OP.organizacion_politica FROM financiamiento_privado AS EB  JOIN organizaciones_politicas AS OP USING (organizacion_politica) WHERE  estado   = '"+org_2017_finan_priv_presento+"' AND  anhio = '2017' GROUP BY (OP.organizacion_politica,monto,OP.url) ORDER BY (monto) " + org_2017_finan_priv_orden_ingreso

    elif org_finan_pub_orden_monto_quinquenal != "unk":
      query_total = "SELECT monto_quinquenal AS monto, OP.organizacion_politica, EB.num_votos_congresales FROM financiamiento_publico AS EB JOIN organizaciones_politicas AS OP USING (organizacion_politica) GROUP BY (EB.num_votos_congresales,OP.organizacion_politica,monto,OP.url) ORDER BY (monto) " + org_finan_pub_orden_monto_quinquenal
    
    planes_gob = "SELECT PG.url1 FROM planes_gobierno AS PG INNER JOIN organizaciones_politicas as OP where PG.organizacion_politica = OP.organizacion_politica"
    
    org_politicas = OrganizacionesPoliticas.objects.raw(query_total)
    # Paginator 
    paginator = Paginator(org_politicas, 20)
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
                    'organizaciones': page_obj,
                    'planes_gobierno' : planes_gob
                  } )

def hojadevida_by_dni(request, dni_hoja_de_vida, cargo_postula_dato):
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
  
    
  renuncias_ = Renuncia.objects.raw("SELECT DISTINCT DP.id, EP.tiene_info_por_declarar, EP.organización_renuncia, EP.comentario FROM renuncia AS EP RIGHT JOIN datos_personales AS DP USING (dni_candidato) WHERE DP.cargo_eleccion ='"+cargo_postula_dato+"' AND DP.dni_candidato ='" +dni_hoja_de_vida+ "'")
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


# def planesdegobierno(request):
#   return render(request,'elecciones/planesgobierno.html')

def iaDisplay(request):
  if request.method == "GET":
    cargo_postula_list = request.GET.getlist('cargo_postula')    
    if len(cargo_postula_list) == 0:
      cargo_postula_ = "presidenciales" 
    else:
      cargo_postula_ = cargo_postula_list[0]
    organizacion_list = request.GET.getlist("organizacion")
    if len(organizacion_list) == 0:
      organizacion_ = "" 
    else:
      organizacion_ = organizacion_list[0]

    if cargo_postula_ == "presidenciales":
      WHERE_candidato = " (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion  ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
    elif cargo_postula_ == "congresales":
      WHERE_candidato = " (cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') "
    elif cargo_postula_ == "parlamento":
      WHERE_candidato = " (cargo_eleccion = 'REPRESENTANTE ANTE EL PARLAMENTO ANDINO') "
    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Alegría'"
    candidatos_alegria = AiTotal.objects.raw(query_)
    #print("query_: ",query_)
    
    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Molestia'"
    candidatos_molestia = AiTotal.objects.raw(query_)
    #print("query_: ",query_)
    
    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Miedo'"
    candidatos_miedo = AiTotal.objects.raw(query_)
    #print("query_: ",query_)

    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Seriedad'"
    candidatos_seriedad = AiTotal.objects.raw(query_)
    #print("query_: ",query_)

    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Sorpresa'"
    candidatos_sorpresa = AiTotal.objects.raw(query_)
    #print("query_: ",query_)
    
    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Disgusto'"
    candidatos_disgusto = AiTotal.objects.raw(query_)
    #print("query_: ",query_)

    query_ = "SELECT * FROM ai_total WHERE "+WHERE_candidato+" AND organizacion_politica='"+organizacion_+"' AND emocion='Tristeza'"
    candidatos_tristeza = AiTotal.objects.raw(query_)
    #print("query_: ",query_)

    if(candidatos_alegria or candidatos_molestia or candidatos_miedo or candidatos_seriedad or candidatos_sorpresa or candidatos_disgusto or candidatos_tristeza):
      have_results = True
    else:
      have_results = False

    return render(request,
    'elecciones/iaDisplay.html',
    {
      'candidatos_tristeza':candidatos_tristeza,
      'candidatos_alegria':candidatos_alegria,
      'candidatos_sorpresa':candidatos_sorpresa,
      'candidatos_disgusto':candidatos_disgusto,
      'candidatos_molestia':candidatos_molestia,
      'candidatos_miedo':candidatos_miedo,
      'candidatos_seriedad':candidatos_seriedad,
      'have_results': have_results
    })

def nosotros(request):
  return render(request,'elecciones/nosotros.html',{})

def error_404(request, exception):
  data = {}
  return render(request,'404.html', data)

def error_500(request):
  data = {}
  return render(request,'500.html', data)

def error_403(request, exception):
  data = {}
  return render(request,'403.html', data)

def error_400(request, exception):
  data = {}
  return render(request,'400.html', data)

def subir_data(request):
  # Leer el archivo 'datos.csv' con reader() y
  # mostrar todos los registros, uno a uno:
  from time import time
  inicio = time()
  import csv
  with open("datos/bien_inmueble.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = BienInmueble.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_inmueble = objeto[5],
            tipo_inmueble = objeto[6],
            direccion_inmueble = objeto[7],
            esta_inscrito_sunarp = objeto[8],
            partida_inmueble_sunarp = objeto[9],
            autovaluo = objeto[10],
            comentario_inmueble = objeto[11],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("bien_inmueble")
  with open("datos/bien_mueble.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = BienMueble.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_bien_mueble = objeto[5],
            vehiculo = objeto[6],
            placa = objeto[7],
            valor = objeto[8],
            caracteristicas_vehiculo = objeto[9],
            comentario_vehiculo = objeto[10],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("bien_mueble")
  with open("datos/cargo_eleccion.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = CargoEleccion.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_info_por_declarar = objeto[5],
            org_politica_cargo = objeto[6],
            desde_anhio = objeto[7],
            hasta_anhio = objeto[8],
            total_anhio_eleccion = objeto[9],
            cargo = objeto[10],
            comentario = objeto[11],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("cargo_eleccion")
  with open("datos/cargo_partidario.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = CargoPartidario.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_cargo_partidario = objeto[5],
            org_politica_cargo = objeto[6],
            cargo = objeto[7],
            desde_anhio = objeto[8],
            hasta_anhio = objeto[9],
            comentario = objeto[10],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("cargo_partidario")
  with open("datos/datos_personales.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = DatosPersonales.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            carnet_extranjeria = objeto[5],
            apellido_paterno = objeto[6],
            apellido_materno = objeto[7],
            nombres = objeto[8],
            sexo = objeto[9],
            fecha_nacimiento = objeto[10],
            pais_nacimiento = objeto[11],
            departamento_nacimiento = objeto[12],
            provincia_nacimiento = objeto[13],
            distrito_nacimiento = objeto[14],
            departamento_domicilio = objeto[15],
            provincia_domicilio = objeto[16],
            distrito_domicilio = objeto[17],
            direccion_domicilio = objeto[18],
            cargo_eleccion = objeto[19],
            url = objeto[20],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("datos_personales")
  with open("datos/edad.csv", encoding="utf8") as csvarchivo:
    from .models import TablaEdad
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = TablaEdad.objects.create(
            edad = int(objeto[0]),
            organizacion_politica = objeto[1],
            dni = objeto[2],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("edad")
  with open("datos/edu_basica.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = EducacionBasica.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_educacion_basica = objeto[5],
            tiene_estudio_primaria = objeto[6],
            concluyo_primaria = objeto[7],
            tiene_estudio_secundaria = objeto[8],
            concluyo_secundaria = objeto[9],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("edu_basica")
  with open("datos/estudio_no_univ.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = EstudioNoUniversitario.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_estudio_no_universitario = objeto[5],
            centro_estudio_no_universitario = objeto[6],
            carrera_no_universitaria = objeto[7],
            concluyo_estudio_no_universitario = objeto[8],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("estudio_no_univ")
  with open("datos/estudio_post.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = EstudioPostgrado.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_postgrado = objeto[5],
            centro_estudio_postgrado = objeto[6],
            especialidad = objeto[7],
            concluyo_estudio_postgrado = objeto[8],
            es_egresado_postgrado = objeto[9],
            es_maestro = objeto[10],
            es_doctor = objeto[11],
            anhio_obtencion_postgrado = objeto[12],
            comentario_estudio_postgrado = objeto[13],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("estudio_post")
  with open("datos/estudio_tec.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = EstudioTecnico.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_estudio_tecnico = objeto[5],
            centro_estudio_tecnico = objeto[6],
            carrera_tecnica = objeto[7],
            concluyo_estudio_tecnico = objeto[8],
            comentario_estudio_tecnico = objeto[9],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("estudio_tec")
  with open("datos/estudio_univers.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = EstudioUniversitario.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_estudio_universitario = objeto[5],
            universidad = objeto[6],
            carrera_universitaria = objeto[7],
            concluyo_estudio_universitario = objeto[8],
            es_egresado_universitario = objeto[9],
            anhio_obtencion_universitario = objeto[10],
            comentario_estudio_universitario = objeto[11],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("Estudios Universitarios")
  with open("datos/exp_lab.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = ExperienciaLaboral.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_experiencia_laboral = objeto[5],
            centro_laboral = objeto[6],
            ocupacion = objeto[7],
            ruc_empresa_laboral = objeto[8],
            direccion_laboral = objeto[9],
            desde_anhio = objeto[10],
            hasta_anhio = objeto[11],
            pais_laboral=objeto[12],
            departamento_laboral = objeto[13],
            provincia_laboral = objeto[14],
            distrito_laboral = objeto[15],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("exp_lab")
  with open("datos/finan_priv.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = FinanciamientoPrivado.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            ruc_org_politica = objeto[2],
            estado = objeto[3],
            fecha_presentacion = objeto[4],
            total_activo = objeto[5],
            total_pasivo = objeto[6],
            total_patrimonio = objeto[7],
            total_pasivo_patrimonio = objeto[8],
            total_ingresos = objeto[9],
            total_gastos = objeto[10],
            anhio = objeto[11],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass

  print("finan_priv")
  with open("datos/finan_pub.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = FinanciamientoPublico.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            num_votos_congresales = objeto[2],
            monto_quinquenal = objeto[3],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass

  print("finan_pub")
  with open("datos/info_adi.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = InformacionAdicional.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_info_adicional = objeto[5],
            info = objeto[6],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("info_adi")

  with open("datos/ingreso.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = Ingreso.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_ingresos = objeto[5],
            anhio_ingresos = objeto[6],
            total_ingresos = objeto[7],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("ingreso")

  with open("datos/org_poli.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = OrganizacionesPoliticas.objects.create(
            organizacion_politica = objeto[0],
            url = objeto[1],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("org_poli")

  with open("datos/renuncia.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = Renuncia.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_info_por_declarar = objeto[5],
            organización_renuncia = objeto[6],
            comentario = objeto[7],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass

  print("renuncia")
  with open("datos/sent_oblig.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = SentenciaObligacion.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_info_por_declarar = objeto[5],
            materia_sentencia = objeto[6],
            n_experiente_obliga = objeto[7],
            organo_judicial = objeto[8],
            fallo_obliga = objeto[9],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass

  print("sent_oblig")
  with open("datos/sent_penal.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = SentenciaPenal.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_info_por_declarar = objeto[5],
            n_experiente_penal = objeto[6],
            fecha_sentencia_penal = objeto[7],
            organo_judicial = objeto[8],
            delito_penal = objeto[9],
            fallo_penal = objeto[10],
            modalidad_penal = objeto[11],
            otra_modalidad = objeto[12],
            cumplimiento_del_fallo = objeto[13],
          )
          bien_inmueble_objeto.save()
        except:
          pass
    except:
      pass
  print("sent_penal")
  final = time() - inicio
  print("Tiempo Total : ", final)
  return HttpResponse("")

def eliminar(lista):
  for objeto in lista:
    objeto.delete()

def eliminar_data(request):
  from .models import TablaEdad
  eliminar(BienInmueble.objects.all())
  eliminar(BienMueble.objects.all())
  eliminar(CargoEleccion.objects.all())
  eliminar(CargoPartidario.objects.all())
  eliminar(DatosPersonales.objects.all())
  eliminar(TablaEdad.objects.all())
  eliminar(EducacionBasica.objects.all())
  eliminar(EstudioNoUniversitario.objects.all())
  eliminar(EstudioPostgrado.objects.all())
  eliminar(EstudioTecnico.objects.all())
  eliminar(ExperienciaLaboral.objects.all())
  eliminar(FinanciamientoPrivado.objects.all())
  eliminar(FinanciamientoPublico.objects.all())
  eliminar(InformacionAdicional.objects.all())
  eliminar(Ingreso.objects.all())
  eliminar(OrganizacionesPoliticas.objects.all())
  eliminar(Renuncia.objects.all())
  eliminar(SentenciaObligacion.objects.all())
  eliminar(SentenciaPenal.objects.all())
  return HttpResponse('')

def corregir_data(request):
  for o in BienInmueble.objects.all():
    o.delete()
  import csv, sys
  with open("datos/bien_inmueble.csv", encoding="utf8") as csvarchivo:
    entrada = csv.reader(csvarchivo)
    try:
      for objeto in entrada:
        try:
          bien_inmueble_objeto = BienInmueble.objects.create(
            id = objeto[0],
            organizacion_politica = objeto[1],
            distrito_elec = objeto[2],
            dni_candidato = objeto[3],
            candidato = objeto[4],
            tiene_inmueble = objeto[5],
            tipo_inmueble = objeto[6],
            direccion_inmueble = objeto[7],
            esta_inscrito_sunarp = objeto[8],
            partida_inmueble_sunarp = objeto[9],
            autovaluo = objeto[10],
            comentario_inmueble = objeto[11],
          )
          bien_inmueble_objeto.save()
        except:
          print('id : ', objeto[0])
          pass
    except:
      pass

  return HttpResponse('bien')
