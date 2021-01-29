from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *

SELECT_candidato = ""
WHERE_candidato = ""

def function_filtros_ob(self, query_normal, normnob1):
    #print("function_filtros_ob##################")
    #print(len(self))
  
    query_total = ""
    subquery_list = list()
    for i in range(0, len(self)):
        index_ = self[i].find('_')
        valor = self[i][index_+1:]
        quitar = self[i][index_-1:]
        if int(valor) > 9:
          quitar = self[i][index_-2:]
        aux = self[i].replace("("+quitar, "")
        self[i] = aux
        if valor == "1":
            if len(self) > 1 or normnob1 == True: #cargos previos
                subquery = " SELECT CE.total_anhio_eleccion AS conteo, DP.dni_candidato FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY ( DP.dni_candidato,  conteo)  " 
                
                subquery_list.append(subquery)
            else:
                subquery = " SELECT DP.id, CE.total_anhio_eleccion AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM cargo_eleccion AS CE JOIN  datos_personales AS DP USING (dni_candidato) WHERE CE.tiene_info_por_declarar  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (  Dp.id, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion, CE.total_anhio_eleccion) ORDER BY conteo " +self[i]
                return subquery            
        elif valor == "2": # cant sentencia penal 
            if len(self) >1 or normnob1 == True :
                subquery =   " SELECT  COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato)  "
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT  COUNT(SP.dni_candidato) AS conteo, DP.dni_candidato,   DP.candidato, DP.organizacion_politica, DP.distrito_elec FROM sentencia_penal AS SP JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato,   DP.candidato, DP.organizacion_politica, DP.distrito_elec ) ORDER BY conteo  " +self[i] 
                return subquery                            
        elif valor == "3": #cantidad sentencia obligaciones
            if len(self) >1 or normnob1 == True :
                subquery = " SELECT  COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato) "
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT  COUNT(SO.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.distrito_elec FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato, total_ingresos,DP.candidato, DP.organizacion_politica, DP.distrito_elec) ORDER BY conteo  " +self[i]
                return subquery
        elif valor == "6":#cantidad ingresos
            subquery = " SELECT total_ingresos AS  conteo , DP.dni_candidato FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY ( DP.dni_candidato, conteo) "
            if len(self) >1 or normnob1 == True :
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT total_ingresos AS  conteo , DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.distrito_elec FROM ingreso AS I JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_ingresos  = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY ( DP.dni_candidato, total_ingresos, DP.candidato, DP.organizacion_politica, DP.distrito_elec) ORDER BY conteo "  + self[i]
                return subquery
        elif valor == "7":#cantidad inmueble
            subquery = " SELECT COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato) " 
            if len(self) >1 or ( normnob1 == True):
                subquery_list.append(subquery)
            else: 
                subquery = "SELECT COUNT(BI.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion) ORDER BY conteo " + self[i]             
                return subquery            
        elif valor == "8":  #valor inmuebles
            subquery = " SELECT SUM (BI.autovaluo) AS conteo, DP.dni_candidato FROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_inmueble = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato)  "
            if len(self) >1 or normnob1 == True :
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT SUM (BI.autovaluo) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccionFROM bien_inmueble AS BI JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_inmueble = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion) ORDER BY conteo " + self[i]
                return subquery 
        elif valor == "9" : # cantidad muebles
            subquery = " SELECT COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato) " 
            if len(self) >1 or normnob1 == True :
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT COUNT(BM.dni_candidato) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato)WHERE tiene_bien_mueble  = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion) ORDER BY conteo "+self [i]                
                return subquery
        elif valor == "10"  : #valor muebles
            subquery = " SELECT SUM (BM.valor ) AS conteo, DP.dni_candidato FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato)  " 
            if len(self) >1 or normnob1 == True :
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT SUM (BM.valor ) AS conteo, DP.dni_candidato,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM bien_mueble AS BM JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_bien_mueble = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato , DP.candidato, DP.organizacion_politica, DP.cargo_eleccion) ORDER BY conteo  " + self[i]
                return subquery
        elif valor == "11": #renuncias
            subquery = " SELECT COUNT(R.dni_candidato) AS conteo, DP.dni_candidato FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY (DP.dni_candidato)  "
            if len(self) >1 or normnob1 == True:
                subquery_list.append(subquery)
            else: 
                subquery = " SELECT  DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion, COUNT(R.dni_candidato) AS conteo FROM renuncia AS R JOIN  datos_personales AS DP USING (dni_candidato) WHERE tiene_info_por_declarar = 'SI' AND  (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') GROUP BY ( DP.dni_candidato, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion) ORDER BY conteo "+ self[i]                
                return subquery
    #return subquery_list
    if normnob1 == True:
        return subquery_list
    SELECT = " SELECT DP.id,  DP.candidato,DP.dni_candidato, DP.organizacion_politica, DP.cargo_eleccion  "
    WHERE = " WHERE (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA')"
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
    GROUP_BY_ = " GROUP BY (DP.id,DP.candidato,DP.dni_candidato, DP.organizacion_politica, DP.cargo_eleccion, "+ Qs+" ) "
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
def function_filtro_normal(self):
    # print("self",self)
    if self[0] != "":
        if(self[0] == 'maestro_doctor'):
            query_total = "SELECT DP.id , SELECT DP.dni_candidato , DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE (EP.es_maestro= 'SI' OR EP.es_doctor = 'SI') AND   (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR   DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA')   "
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
            retorno = "SELECT DP.id, DP.dni_candidato,DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM " + tabla + \
                " AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." +  self[0] + " = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
            self[0] = ""
            return retorno
    if self[4] != "":
        retorno = "SELECT DP.id, DP.dni_candidato   DP.candidato, DP.organizacion_politica,  DP.cargo_eleccion,  DP.dni_candidato FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[
            4]+"' ) AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion  ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
        self[4] = ""
        return retorno
    if self[5] == "NO":
        retorno = "SELECT DP.id, DP.dni_candidato, DP.candidato, DP.organizacion_politica,  DP.cargo_eleccion,  DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO' "
        self[5] = ""
        return retorno
    if self[12] != "":
        retorno = "SELECT DP.id,  DP.dni_candidato,DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM tabla_edad AS TE JOIN    datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN " + (self[12])[:2] + " AND " + ( self[12])[3:5] + " AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR   DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
        self[12] = ""
        return retorno
    if self[13] == "SI":
        retorno = "SELECT id, dni_candidato, candidato, organizacion_politica, cargo_eleccion FROM  datos_personales WHERE   departamento_nacimiento = '"+ self[15]+"' AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion   ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') " 
        self[13] = ""
        return retorno
    if self[14] != "":
        retorno = "SELECT id,  dni_candidato, candidato, organizacion_politica, cargo_eleccion FROM datos_personales WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
        self[14] = ""
        return retorno
    if self[16] != "":
        retorno = "SELECT id ,  dni_candidato, candidato, organizacion_politica, cargo_eleccion FROM  datos_personales  WHERE cargo_eleccion = '" + \
            self[16]+"' "
        self[16] = ""
        return retorno
    if self[17] != "":
        retorno = "SELECT id,  dni_candidato, candidato, organizacion_politica, cargo_eleccion FROM  datos_personales WHERE organizacion_politica  = '" +self[17]+"' AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
        self[17] = ""
        return retorno
    if self[18] != "":
        retorno = "SELECT id,   dni_candidato,candidato, organizacion_politica, distrito_elec FROM  datos_personales WHERE distrito_elec = '" + self[18] + "' AND  (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
        self[18] = ""
        return retorno
def function_filtro_normal(self):
  print("self",self)
  if self[0] != "":
    if(self[0] == 'maestro_doctor'):
      query_total = "SELECT DP.id  , DP.candidato, DP.organizacion_politica, DP.cargo_eleccion FROM  estudio_postgrado AS EP   JOIN  datos_personales AS DP USING   (dni_candidato) WHERE (EP.es_maestro= 'SI' OR EP.es_doctor = 'SI') AND   (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR   DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA')   " 
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
      retorno = "SELECT DP.id, DP.candidato, DP.organizacion_politica, DP.cargo_eleccion, DP.dni_candidato FROM " + tabla + " AS EB JOIN    datos_personales AS DP USING (dni_candidato)  WHERE EB." + self[0] + " = 'SI' AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
      self[0]=""
      return retorno
  if self[4] != "":
    retorno = "SELECT DP.id,   DP.candidato, DP.organizacion_politica, DP.cargo_eleccion,  DP.dni_candidato FROM   sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'SI' AND  (SO.materia_sentencia = '"+self[4]+"' ) AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion  ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') " 
    self[4]=""
    return retorno
  if self[5] == "NO":
    retorno = "SELECT DP.id,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion,  DP.dni_candidato FROM sentencia_obligacion AS SO JOIN  datos_personales AS DP USING (dni_candidato) WHERE SO.tiene_info_por_declarar = 'NO' "
    self[5]=""
    return retorno
  if self[12] != "":
    retorno = "SELECT DP.id,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion ,  DP.dni_candidato FROM tabla_edad AS TE JOIN    datos_personales AS DP USING (dni_candidato) WHERE TE.edad BETWEEN "+ (self[12])[:2]+ " AND " +(self[12])[3:5]    + " AND (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR   DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') " 
    self[12]=""
    return retorno    
  if self[13] == "SI":
    retorno ="SELECT id, candidato, organizacion_politica, cargo_eleccion,  dni_candidato FROM  datos_personales WHERE   departamento_nacimiento = '"+ self[15]+"' AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion   ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
    self[13]=""
    return retorno  
  if self[14]!="":
    retorno = "SELECT id,  candidato, organizacion_politica, cargo_eleccion,  dni_candidato FROM datos_personales WHERE pais_nacimiento   <>'PERÚ' and pais_nacimiento <>'PERU'AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
    self[14]=""
    return retorno   
  if self[16]!="":
    retorno = "SELECT id ,  candidato, organizacion_politica, cargo_eleccion ,  dni_candidato FROM  datos_personales  WHERE cargo_eleccion = '"+  self[16]+"' "
    self[16]=""
    return retorno
  if self[17]!= "":
    retorno = "SELECT id,  candidato, organizacion_politica, cargo_eleccion,  dni_candidato FROM  datos_personales WHERE organizacion_politica  = '"+self[17]+"' AND (cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR  cargo_eleccion ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA') "
    self[17]=""
    return retorno
  if self[18]!="":
    retorno = "SELECT id, candidato, organizacion_politica, distrito_elec ,  dni_candidato FROM  datos_personales WHERE distrito_elec = '" +self[18]+"' AND  (cargo_eleccion = 'CONGRESISTA DE LA REPÚBLICA') "
    self[18]=""
    return retorno



def filter_function(request, nivel_academico,cargos_previos_order , orden_cant_sentencia, orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,cargo_postula, org_politica, dist_electoral, tipo_candidato_):
  lista_valores = [nivel_academico,cargos_previos_order , orden_cant_sentencia,
    orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, orden_cant_ingreso,orden_cant_inmueble,orden_valor_inmueble,
    orden_cant_mueble, orden_valor_mueble,orden_renuncias, rango_edad_val,nac_per_si, nac_per_no, departamento_nacimiento,
    cargo_postula, org_politica, dist_electoral, tipo_candidato_
  ]
  print("tipo_candidato_: ", tipo_candidato_)
  
  if tipo_candidato_ == "presidenciales":
    SELECT_candidato =  "cargo_eleccion"
    WHERE_candidato = " XD"
  elif tipo_candidato_ == "congreso":
    print('todo')

  lista_filtros_normales = list()
  lista_filtros_ob = list()
  # for i in range(0,len(lista_valores)):
  #  print(i, lista_valores[i])
  lista_val_new = list()
  lista_orden = list()
  lista_ids_new = list()
  # for item in lista_valores:
  lista_ids = list()
  lista_ob_dict = list()
  almenos1 = False
  for i in range(0, len(lista_valores)-1):
      print("lista_valores[i]: ", lista_valores[i])
      if lista_valores[13] != "unk" and i == 15:
          continue
      if lista_valores[i] != "unk":
          tienes_al_menos1 = True
          index_ = lista_valores[i].find('(')
          valor = lista_valores[i][index_+1:]
          lista_valores[i] = lista_valores[i] + str("_") + str(i)
          # lista_valores[i] = lista_valores[i].replace("("+valor, "")
          if (i >= 1 and i <= 3) or (i >= 6 and i <= 11):
              #print(lista_valores[i])
              lista_filtros_ob.append(lista_valores[i])
          else:
              lista_filtros_normales.append(lista_valores[i])
          lista_val_new.append(lista_valores[i])
          lista_orden.append(valor)
      elif lista_valores[i] == "unk":
          lista_valores[i] = ""
  #print("")
  # print(lista_val_new)
  #print("lista_orden: ",lista_orden)
  lista_index = list()
  if (tienes_al_menos1 == True):
      j = 1
      for i in range(0, len(lista_orden)):
          val = lista_orden.index(str(j))
          lista_index.append(val)
          j += 1
      #print(lista_index)
      LN = list()
      for i in lista_index:
          LN.append(lista_val_new[i])
      #print("LN: ", LN)
      #print("lista_ids ", lista_ids)
      diccionarios_ordenados = list()
      # print("------------------------------")
      #print(lista_filtros_ob)
      lista_filtros_ob_new = list()
      for i in range(0, len(LN)):
          if(LN[i] in lista_filtros_ob):
              lista_filtros_ob_new.append(LN[i])
              # index_ = lista_filtros_ob.index(LN[i])
              # lista_ids_new.append(lista_ids[index_])
      # print(lista_filtros_ob_new)
  # print("lista_valores: ",lista_valores)
# i lista_valores[] != "":
  # print(lista_orden)

  # print(lista_ids)
  # print(LN)
  #print(lista_ids_new)
  query_total = ""
  #print("lista_filtros_ob_new: ",lista_filtros_ob_new, "  size: ", len(lista_filtros_ob_new))
  #print("lista_filtro_normales: ",lista_filtros_normales,"  size:  ", len(lista_filtros_normales))
  for i  in range(0, len(lista_valores)):
      index_ = lista_valores[i].find('(')
      if index_ != -1:  
          quitar = lista_valores[i][index_:]    
          aux = lista_valores[i].replace(quitar, "")
          lista_valores[i] = aux


  #print("lista_filtros_ob: ",lista_filtros_ob)
  #print("lista_filtros_normales: ", lista_filtros_normales)

  if len(lista_filtros_normales) == 0:
      #print("Lista de filtros normales esta vacia")
      query_normal = ""
      query_total = function_filtros_ob(lista_filtros_ob_new,query_normal,False)
      #print("query_total: ", query_total)
  
  
  elif len(lista_filtros_ob_new) == 0:
      #print("Lista de filtros ob esta vacio")
      query_total = query_total + function_filtro_normal(lista_valores)
      for i in range(1, len(lista_filtros_normales)):
          query_total = query_total +" INTERSECT "+ function_filtro_normal(lista_valores)
      #print("query_total: ",query_total)
      #print("lista_filtros_normales: ",lista_filtros_normales )
     
  elif len(lista_filtros_normales)==1 and len(lista_filtros_ob_new)>1:
      #print("normales 1 ob n")
      query_total_filtro_normal = ""
      #print("lista_valores: ",lista_valores)
      query_total_filtro_normal = query_total_filtro_normal + function_filtro_normal(lista_valores)
      #print("query_total_filtro_normal: ",query_total_filtro_normal)
      query_total = function_filtros_ob(lista_filtros_ob_new,query_total_filtro_normal , False)
      #print("query_total: ",query_total)
  elif (len(lista_filtros_normales)>1 and len(lista_filtros_ob_new) ==  1):
      query_total_filtros_normales = ""
      #print("len(lista_filtros_normales)>1 and len(lista_filtros_ob_new) ==  1")
      query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores)
      for i in range(1, len(lista_filtros_normales)):
          query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores)
      #print("lista_filtros_ob_new: ", lista_filtros_ob_new)
      filtro_ob = function_filtros_ob(lista_filtros_ob_new , "",True)
      #print("filtro_ob: ",filtro_ob[0])
      #print("---------------------------------------------------")
      #print("query_total_filtros_normales: ",query_total_filtros_normales)
      for i in range(0, len(lista_filtros_ob_new)):
          index_ = lista_filtros_ob_new[i].find('_')
          valor = lista_filtros_ob_new[i][index_+1:]
          quitar = lista_filtros_ob_new[i][index_-1:]
          aux = lista_filtros_ob_new[i].replace("("+quitar, "")
          lista_filtros_ob_new[i] = aux
      query_total = " SELECT DP.id,  DP.cargo_eleccion,  DP.candidato, DP.organizacion_politica FROM ( "+ query_total_filtros_normales+ " ) AS QN JOIN datos_personales AS DP USING (dni_candidato) join ( " + filtro_ob[0] +" ) AS Q1 USING (dni_candidato) WHERE (DP.cargo_eleccion = 'PRESIDENTE DE LA REPÚBLICA' OR DP.cargo_eleccion  ='PRIMER VICEPRESIDENTE DE LA REPÚBLICA' OR  DP.cargo_eleccion = 'SEGUNDO VICEPRESIDENTE DE LA REPÚBLICA')  GROUP BY (conteo,DP.id,  DP.candidato, DP.organizacion_politica, DP.cargo_eleccion) ORDER BY conteo " + lista_filtros_ob_new[0]
      #query_total = (list,query_total_filtros_normales)
      #print("query_total: ", query_total)
  elif len(lista_filtros_normales)>1 and len(lista_filtros_ob_new)>1:
      query_total_filtros_normales = ""
      #print("len(lista_filtros_normales)>1 and len(lista_filtros_ob_new) >  1")
      query_total_filtros_normales = query_total_filtros_normales + function_filtro_normal(lista_valores)
      for i in range(1, len(lista_filtros_normales)):
          query_total_filtros_normales = query_total_filtros_normales +" INTERSECT "+ function_filtro_normal(lista_valores)
      
      #print("query_total_filtros_normales: ", query_total_filtros_normales )
      query_total = function_filtros_ob(lista_filtros_ob_new, query_total_filtros_normales, False)
      #print("--------------------------------------------------------------------")


  print("query_total", query_total)
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
