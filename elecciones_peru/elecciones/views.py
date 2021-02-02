from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *



def function_filtros_ob(self, query_normal, normnob1, SELECT_candidato,WHERE_candidato ):
    #print("function_filtros_ob##################")
    #print(len(self))
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
          subquery = " SELECT CE.total_anhio_eleccion AS conteo, DP.dni_candidato FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND "+ WHERE_candidato+ " GROUP BY ( DP.dni_candidato,  conteo)  "       
          subquery_list.append(subquery)
        else:
          subquery = " SELECT DP.id, CE.total_anhio_eleccion AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "  +  SELECT_candidato + " FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND "  + WHERE_candidato + "  GROUP BY (  Dp.id, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+ ", CE.total_anhio_eleccion) ORDER BY conteo " +self[i]
          return subquery            
      elif valor == "2": # cant sentencia penal 
          if len(self) >1 or normnob1 == True :
              subquery =   " SELECT  COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND " + WHERE_candidato+" GROUP BY (DP.dni_candidato)  "
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT DP.id, COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica , "+ SELECT_candidato  +"  FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  " +  WHERE_candidato  +" GROUP BY (Dp.id, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo  " +self[i] 
              return subquery                            
      elif valor == "3": #cantidad sentencia obligaciones
          if len(self) >1 or normnob1 == True :
              subquery = " SELECT  COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  " +   WHERE_candidato +    " GROUP BY (DP.dni_candidato) "
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT  DP.id , COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica , " + SELECT_candidato +  " FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND " +  WHERE_candidato +"   GROUP BY (" + SELECT_candidato + " , DP.dni_candidato,DP.candidato, DP.organizacion_politica, DP.id) ORDER BY conteo  " +self[i]
              return subquery
      elif valor == "6":#cantidad ingresos
          subquery = " SELECT  total_ingresos AS  conteo , DP.dni_candidato FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND "+ WHERE_candidato +"  GROUP BY (DP.id,  DP.dni_candidato, conteo) "
          if len(self) >1 or normnob1 == True :
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT DP.id, total_ingresos AS  conteo , DP.dni_candidato,  DP.candidato, DP.organizacion_politica," + SELECT_candidato  +   " FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND "+ WHERE_candidato +" GROUP BY ( DP.id,DP.dni_candidato, total_ingresos, DP.candidato, DP.organizacion_politica, "  +  SELECT_candidato +") ORDER BY conteo "  + self[i]
              return subquery
      elif valor == "7":#cantidad inmueble
          subquery = " SELECT  COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND "+ WHERE_candidato+"  GROUP BY (DP.dni_candidato) " 
          if len(self) >1 or ( normnob1 == True):
              subquery_list.append(subquery)
          else:
              subquery = "SELECT DP.id, COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+" FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND " + WHERE_candidato+"  GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica," + SELECT_candidato+ ") ORDER BY conteo " + self[i]             
              return subquery            
      elif valor == "8":  #valor inmuebles
          subquery = " SELECT SUM (BI.autovaluo) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND  "+   WHERE_candidato +"  GROUP BY (DP.dni_candidato)  "
          if len(self) >1 or normnob1 == True :
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT SUM (BI.autovaluo) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +"  FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND " + WHERE_candidato+ " GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo " + self[i]
              return subquery 
      elif valor == "9" : # cantidad muebles
          subquery = " SELECT COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  "+  WHERE_candidato +  " GROUP BY (DP.dni_candidato) " 
          if len(self) >1 or normnob1 == True :
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+ " FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  " +  WHERE_candidato+ " GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+SELECT_candidato+"  ) ORDER BY conteo "+self [i]                
              return subquery
      elif valor == "10"  : #valor muebles
          subquery = " SELECT SUM (BM.valor ) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND " + WHERE_candidato+ " GROUP BY (DP.dni_candidato)  " 
          if len(self) >1 or normnob1 == True :
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT SUM (BM.valor ) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato+" FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND "  + WHERE_candidato+ " GROUP BY (DP.dni_candidato , DP.candidato, DP.organizacion_politica, "+ SELECT_candidato+" ) ORDER BY conteo  " + self[i]
              return subquery
      elif valor == "11": #renuncias
          subquery = " SELECT COUNT(R.dni_candidato) AS conteo, DP.dni_candidato FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  "+WHERE_candidato+" GROUP BY (DP.dni_candidato)  "
          if len(self) >1 or normnob1 == True:
              subquery_list.append(subquery)
          else: 
              subquery = " SELECT  DP.id , DP.dni_candidato, DP.candidato, DP.organizacion_politica, " + SELECT_candidato+", COUNT(R.dni_candidato) AS conteo FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND "+ WHERE_candidato+" GROUP BY ( DP.id , DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +" ) ORDER BY conteo "+ self[i]                
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
    GROUP_BY_ = " GROUP BY (DP.id,DP.candidato,DP.dni_candidato, DP.organizacion_politica,  "+  SELECT_candidato+"  , "+ Qs+" ) "
    #print("query_normal: ",query_normal)
    for i in range(0, len(subquery_list)):          
        if i == 0 and query_normal != "":
            FROM = " FROM ( " + query_normal+ " ) AS  QN JOIN datos_personales AS DP USING (dni_candidato) "  
        if i == 0 and query_normal == "":
            FROM = " FROM ("+ subquery_list[i] +" ) AS "+" Q"+str(i+1)+ " JOIN datos_personales AS DP USING (dni_candidato) "     
            continue
        FROM = FROM + " JOIN ("+subquery_list[i]   +" ) AS Q" +str(i+1)+ " USING (dni_candidato) "    
    ORDER_BY = " ORDER BY "+Qs_
    query_total = SELECT + " , " + Qs + FROM + WHERE + GROUP_BY_ + ORDER_BY
     
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
              query_total = "SELECT DP.id ,  DP.dni_candidato , DP.candidato, DP.organizacion_politica, "+  SELECT_candidato+ "  FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE ((EP.es_maestro= 'SI' ) OR (EP.es_doctor = 'SI')) AND  "+ WHERE_candidato
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
              retorno = "SELECT DP.id, DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+ SELECT_candidato +"  FROM " + tabla + \
                  " AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." +  self[0] + " = 'SI' AND "+ WHERE_candidato
              self[0] = ""
              return retorno
      if self[4] != "":
          retorno = "SELECT DP.id, DP.dni_candidato ,  DP.candidato, DP.organizacion_politica,  "+ SELECT_candidato +" ,  DP.dni_candidato FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[
              4]+"' ) AND  " + WHERE_candidato
          self[4] = ""
          return retorno
      if self[5] == "NO":
          retorno = "SELECT DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica,  "+SELECT_candidato+" ,  DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO' "
          self[5] = ""
          return retorno
      if self[12] != "":
          retorno = "SELECT DP.id,  DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+ SELECT_candidato+"  FROM tabla_edad AS TE JOIN    datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + ( self[12])[3:5] + " AND  "+WHERE_candidato
          self[12] = ""
          return retorno
      if self[13] == "SI":
          retorno = "SELECT DP.id, DP.dni_candidato, DP.candidato, Dp.organizacion_politica, " + SELECT_candidato+"   FROM datos_personales AS DP  WHERE    departamento_nacimiento = '"+ self[15]+"' AND "+WHERE_candidato 
          self[13] = ""
          return retorno
      if self[14] != "":
          retorno = "SELECT DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,  "+ SELECT_candidato +"  FROM datos_personales AS DP  WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND  "+ WHERE_candidato
          self[14] = ""
          return retorno
      if self[16] != "":
          retorno = "SELECT DP.id ,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,  "+ SELECT_candidato +"  FROM  datos_personales AS DP  WHERE cargo_eleccion = '"+ self[16]+"' "
          self[16] = ""
          return retorno
      if self[17] != "":
          retorno = "SELECT DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica, "+SELECT_candidato+" FROM  datos_personales AS DP WHERE organizacion_politica  = '" +self[17]+"' AND  "+ WHERE_candidato
          self[17] = ""
          return retorno
      if self[18] != "":
          retorno = "SELECT DP.id,   DP.dni_candidato,DP.candidato, DP.organizacion_politica, "+SELECT_candidato+" FROM  datos_personales AS DP WHERE distrito_elec = '" + self[18] + "' AND  "+ WHERE_candidato
          self[18] = ""
          return retorno
    elif stack_ == True:
      if self[0] != "":
          print("self[0]: ",self[0])
          if(self[0] == 'maestro_doctor'):
              query_total = "SELECT DP.dni_candidato FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE (EP.es_maestro= 'SI' OR EP.es_doctor = 'SI') AND " + WHERE_candidato
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
              retorno = "SELECT  DP.dni_candidato FROM " + tabla +" AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." +  self[0] + " = 'SI' AND  " + WHERE_candidato
              self[0] = ""
              return retorno
      if self[4] != "":
          retorno = "SELECT DP.dni_candidato  FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[4]+"' ) AND  "+WHERE_candidato
          self[4] = ""
          return retorno
      if self[5] == "NO":
          retorno = "SELECT DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO' "
          self[5] = ""
          return retorno
      if self[12] != "":
          retorno = "SELECT  DP.dni_candidato FROM tabla_edad AS TE JOIN    datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + ( self[12])[3:5] + " AND "+ WHERE_candidato
          self[12] = ""
          return retorno
      if self[13] == "SI":
          retorno = "SELECT DP.dni_candidato FROM  datos_personales AS DP WHERE   departamento_nacimiento = '"+ self[15]+"' AND  "+WHERE_candidato 
          self[13] = ""
          return retorno
      if self[14] != "":
          retorno = "SELECT   DP.dni_candidato FROM datos_personales AS DP WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND  "+WHERE_candidato
          self[14] = ""
          return retorno
      if self[16] != "":
          retorno = "SELECT   DP.dni_candidato FROM  datos_personales AS DP WHERE cargo_eleccion = '" + self[16]+"' "
          self[16] = ""
          return retorno
      if self[17] != "":
          retorno = "SELECT   DP.dni_candidato FROM  datos_personales AS DP WHERE organizacion_politica  = '" +self[17]+"' AND  "+WHERE_candidato
          self[17] = ""
          return retorno
      if self[18] != "":
          retorno = "SELECT   DP.dni_candidato FROM  datos_personales AS DP WHERE distrito_elec = '" + self[18] + "' AND  (cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA' ) "
          self[18] = ""
          return retorno


def filter_function(request, nivel_academico,cargos_previos_order , orden_cant_sentencia, orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,cargo_postula, org_politica, dist_electoral, tipo_candidato_):
  lista_valores = [nivel_academico,cargos_previos_order , orden_cant_sentencia,
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

  print("SELECT_candidato: ", SELECT_candidato)
  print("WHERE_candidato: ", WHERE_candidato)
  lista_filtros_normales = list()
  lista_filtros_ob = list()
  lista_val_new = list()
  lista_orden = list()
  lista_ids_new = list()
  lista_ids = list()
  lista_ob_dict = list()
  tienes_al_menos1 = False
  for i in range(0, len(lista_valores)-1):
      print("lista_valores[",i,"]: " , lista_valores[i])
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
        query_total = query_total + function_filtro_normal(lista_valores, False, SELECT_candidato,WHERE_candidato )

      
      elif len(lista_filtros_normales) > 1: 
        query = ""
        print("len(lista_filtros_normales)  > 1")
        query = query + function_filtro_normal(lista_valores, True, SELECT_candidato,WHERE_candidato )
        for i in range(1, len(lista_filtros_normales)):
            query = query +" INTERSECT "+ function_filtro_normal(lista_valores, True, SELECT_candidato,WHERE_candidato )
        query_total = "SELECT  DP.id,  DP.dni_candidato, DP.candidato, DP.organizacion_politica,   " + SELECT_candidato+ "   FROM  ( "+query + " ) AS QN JOIN datos_personales AS DP USING (dni_candidato)"   

  elif len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)>1:
      query_total_filtros_normales = ""
      query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
      for i in range(1, len(lista_filtros_normales)):
          query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
      filtro_ob = function_filtros_ob(lista_filtros_ob_new , "",True, SELECT_candidato,WHERE_candidato )

      for i in range(0, len(lista_filtros_ob_new)):
          index_ = lista_filtros_ob_new[i].find('_')
          valor = lista_filtros_ob_new[i][index_+1:]
          quitar = lista_filtros_ob_new[i][index_-1:]
          if int(valor) > 9:
            quitar = lista_filtros_ob_new[i][index_-2:]
          aux = lista_filtros_ob_new[i].replace("("+quitar, "")
          lista_filtros_ob_new[i] = aux
      query_total = " SELECT DP.id,  " + SELECT_candidato + ",  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE " + WHERE_candidato+ "  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica, " + SELECT_candidato +") ORDER BY conteo " + lista_filtros_ob_new[0]
     
  
  
  elif ((len(lista_filtros_normales)>1 and len(lista_filtros_ob_new) ==  1))  or  (len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)==1):
      query_total_filtros_normales = ""
      query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
      if len(lista_filtros_normales) >1:  
        for i in range(1, len(lista_filtros_normales)):
            query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
      filtro_ob = function_filtros_ob(lista_filtros_ob_new , "",True, SELECT_candidato,WHERE_candidato )
      for i in range(0, len(lista_filtros_ob_new)):
          index_ = lista_filtros_ob_new[i].find('_')
          valor = lista_filtros_ob_new[i][index_+1:]
          quitar = lista_filtros_ob_new[i][index_-1:]
          aux = lista_filtros_ob_new[i].replace("("+quitar, "")
          lista_filtros_ob_new[i] = aux
      query_total = " SELECT DP.id,  " + SELECT_candidato + " ,  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE "+ WHERE_candidato+"  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica,  "+SELECT_candidato +" ) ORDER BY conteo " + lista_filtros_ob_new[0]

  
  elif len(lista_filtros_normales)>1 and len(lista_filtros_ob_new)>1:
      query_total_filtros_normales = ""
      query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores,True, SELECT_candidato,WHERE_candidato )
      for i in range(1, len(lista_filtros_normales)):
          query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores, True, SELECT_candidato,WHERE_candidato )
      
      print("query_total_filtros_normales: ",query_total_filtros_normales)



      query_total = function_filtros_ob(lista_filtros_ob_new, query_total_filtros_normales, False)

  print("-----------------------------------------------------------------")
  print("query_total", query_total)
  print("-----------------------------------------------------------------")
  candidatos = DatosPersonales.objects.raw(query_total)
  
  return render(request,
                'elecciones/dashboard.html',
                {'candidatos': candidatos}) 


def filter_function_orga(request, filtro_id, info_extra, orden):
    query_total = "select * from datos_personales;"
    print("filtro_id: ",filtro_id)
    print("info_extra: ",info_extra)
    print("orden: ",orden)
    if filtro_id =="opc_edad":
        rango = info_extra.find("-")
        var1 = info_extra[0:rango:+1] 
        var2 = info_extra[rango+1:len(filtro_id):+1]
        print("var1: ", var1)
        print("var2: ", var2)
        query_total = "SELECT id, COUNT (*),partido FROM tabla_edad WHERE edad BETWEEN " +var1+ " AND " +var2+" GROUP BY (id,partido)"    
        #query_total = "SELECT  dni_candidato, candidato, organizacion_politica, cargo_eleccion FROM datos_personales "
    

    #if filtro_id == "primaria" or filtro_id == "secundaria"or filtro_id == "tecnicos"or filtro_id == "nouni"or filtro_id == "uni"or filtro_id == "postgrado"or filtro_id == "maestrodoctor":
    elif filtro_id == "primaria":
        query_total = "SELECT id , COUNT (dni_candidato) AS conteo, organizacion_politica FROM educacion_basica WHERE concluyo_primaria  = 'SI' GROUP BY (organizacion_politica ,id) ORDER BY (conteo) " + orden

    elif filtro_id == "secundaria":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM educacion_basica WHERE concluyo_secundaria  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden

    elif filtro_id == "tecnicos":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_tecnico WHERE concluyo_estudio_tecnico  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    
    elif filtro_id == "nouni":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_no_universitario WHERE concluyo_estudio_no_universitario  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    
    elif filtro_id == "uni":
        query_total = "SELECT id , COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_universitario WHERE concluyo_estudio_universitario  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    
    elif filtro_id == "postgrado":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_postgrado WHERE concluyo_estudio_postgrado  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden

    elif filtro_id == "maestrodoctor":
        query_total = "SELECT id , COUNT (dni_candidato) AS conteo, organizacion_politica FROM estudio_postgrado WHERE ( es_maestro  = 'SI' OR es_doctor = 'SI') GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden

    elif filtro_id == "genero":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM datos_personales  WHERE  sexo = '" + info_extra+ "' GROUP BY (organizacion_politica,id ) ORDER BY (conteo) " + orden
    elif filtro_id == "penal_obligaciones_in":
        query_total = "SELECT id ,SUM(conteo) AS total, organizacion_politica FROM (SELECT  COUNT(dni_candidato) AS conteo , organizacion_politica  FROM sentencia_penal   WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica) UNION ALL SELECT  COUNT(dni_candidato) AS conteo , organizacion_politica  FROM sentencia_obligacion   WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica)) TABLA GROUP BY partido ORDER BY total " +orden 

    elif filtro_id =="penal_cant":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM sentencia_penal WHERE  tiene_info_por_declarar   = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) "+orden
    
    elif filtro_id =="civil_cant":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM sentencia_obligacion  WHERE  tiene_info_por_declarar  = 'SI' GROUP BY (organizacion_politica) ORDER BY (conteo) "+orden
    
    elif filtro_id =="opc_si":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica FROM datos_personales  WHERE departamento_nacimiento = '"+ info_extra+"' GROUP BY (organizacion_politica) ORDER BY (conteo) " + orden
    
    #elif filtro_id =="opc_no":
    #    query_total = "S"

    elif filtro_id =="elecvsnacimiento_name":
        query_total = "SELECT id ,COUNT (dni_candidato) AS conteo, organizacion_politica  FROM datos_personales  WHERE departamento_nacimiento <> distrito_elec AND  distrito_elec <> 'PERUANOS RESIDENTES EN EL EXTRANJERO' AND distrito_elec <> 'LIMA PROVINCIAS' GROUP BY (organizacion_politica) ORDER BY (conteo) "+orden

    elif filtro_id =="2019priv":
        query_total =  "SELECT id ,total_ingresos, organizacion_politica FROM financiamiento_privado  WHERE  estado   = '"+info_extra+"' AND  anhio = '2019' GROUP BY (organizacion_politica,total_ingresos) ORDER BY total_ingresos "+orden
    elif filtro_id =="2018priv":
        query_total =  "SELECT id ,total_ingresos, organizacion_politica FROM financiamiento_privado  WHERE  estado   = '"+info_extra+"' AND  anhio = '2018' GROUP BY (organizacion_politica,total_ingresos) ORDER BY total_ingresos "+orden

    elif filtro_id =="2017priv":
        query_total =  "SELECT id ,total_ingresos, organizacion_politica FROM financiamiento_privado  WHERE  estado   = '"+info_extra+"' AND  anhio = '2017' GROUP BY (organizacion_politica,total_ingresos) ORDER BY total_ingresos "+orden
    elif filtro_id =="publico_orden":
        query_total =  "SELECT id , monto_quinquenal, organizacion_politica, numero_votos_congresales FROM financiamiento_publico  GROUP BY (organizacion_politica) ORDER BY monto_quinquenal "+orden


    print("-------LLEGA A FINAL CASI DE LA FUNCION------------")
    print("query_total: ",query_total)
    #candidatos = DatosPersonales.objects.raw("SELECT * FROM datos_personales")
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
