let organizacion_politica = ""
let info_extra = ""
let tipo_candidato = ""

function cambiar_organizacion(select_)
{  
    if (select_.id == "academico_select" || select_.id == "edad_select")
    {
        info_extra = select_.options[select_.selectedIndex].value
        return;
    }
    if(organizacion_politica!="")
    {
        organizacion_politica = ""
        info_extra = ""
        tipo_candidato = ""
    }
    organizacion_politica = select_.options[select_.selectedIndex].value
    document.getElementById("academico_select").selectedIndex = 0
    document.getElementById("edad_select").selectedIndex = 0
    info_extra = ""
}

function tipo_candidato_select(select_)
{
    tipo_candidato = select_.options[select_.selectedIndex].value
    console.log("tipo_candidato",tipo_candidato)
}


function busqueda_url(id_)
{   

    if(organizacion_politica=="" || tipo_candidato=="") {
          setTimeout(function(){
            UIkit.notification({
              message: 'Especifique la Organización Política y el tipo de candidato',
              status: 'danger'
            })
          }, 1000)
          return 
      }
    if(id_=="edad_busqueda")
    {
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&rango_edad="+info_extra+"-1&org_politica="+organizacion_politica+"-2"
    }
    else if(id_=="cargo_previos_busqueda")
    {
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&anhio_servicio=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="renuncia_busqueda"){
        window.location ="/busqueda?tipo_filter="+tipo_candidato+"&cantidad_renuncia=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="sentencias_busqueda"){
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&ifsentencias=si&cant_senten=DESC-1&cant_senten_oblig=DESC-2&org_politica="+organizacion_politica+"-3"
    }
    else if (id_=="ingreso_busqueda"){
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&cant_ingreso=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="inmueble_busqueda"){
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&cant_inmuebles=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="mueble_busqueda"){
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&cant_muebles=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="academico_busqueda"){
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&nivel_academico="+info_extra+"-1&org_politica="+organizacion_politica+"-2"
    }

}
