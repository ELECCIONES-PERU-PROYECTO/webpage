//let organizacion_politica = ""
//let info_extra = ""
//let tipo_candidato = ""
let json_info_extra = {}
let json_organizacion = {}
let json_tipo_candidato = {}
function selects_index_0(dataset_grupo)
{
    
    let select_organizacion = document.getElementsByClassName("select_organizacion")
    let select_tipo_candidato = document.getElementsByClassName("select_tipo_candidato")
    for(let i = 0 ; i < select_organizacion.length;i++)
    {
      if(dataset_grupo == select_organizacion[i].dataset.grupo)
      {
        continue
      }
      select_organizacion[i].selectedIndex = 0
    }
    for(let i = 0 ; i < select_tipo_candidato.length;i++)
    {
        if(dataset_grupo == select_tipo_candidato[i].dataset.grupo)
        {
            continue
        }
      select_tipo_candidato[i].selectedIndex = 0
    }
    let select_edad_rango = document.getElementById("academico_select_nivel")
    if (select_edad_rango.dataset.grupo != dataset_grupo)
    {
        select_edad_rango.selectedIndex = 0
    }
    let select_nivel_academico = document.getElementById("edad_select_edades")
    if (select_nivel_academico.dataset.grupo != dataset_grupo)
    {
        select_nivel_academico.selectedIndex = 0
    }
    if(dataset_grupo == "none")
    {
        json_organizacion = {"organizacion": "","grupo":""}
        json_info_extra= {"info":"", "grupo":""}
        json_tipo_candidato = {"tipo_candidato":""}
    }
}

window.onload = function()
{     
    selects_index_0("none")
}

function cambiar_organizacion(select_)
{  
    selects_index_0(select_.dataset.grupo)
    organizacion_politica = select_.options[select_.selectedIndex].value
    if(json_tipo_candidato["grupo"] != select_.dataset.grupo)
    {
        json_tipo_candidato = {"tipo_candidato": "","grupo":""}
    }
    json_organizacion = {"organizacion": organizacion_politica,"grupo": select_.dataset.grupo}
}

function tipo_candidato_select(select_)
{
    selects_index_0(select_.dataset.grupo)
    tipo_candidato = select_.options[select_.selectedIndex].value
    if(json_organizacion["grupo"]!= select_.dataset.grupo)
    {
        json_organizacion = {"organizacion":"","grupo":""}
    }
    json_tipo_candidato = {"tipo_candidato": tipo_candidato,"grupo": select_.dataset.grupo}

}
function info_extra_info(select_)
{
    selects_index_0(select_.dataset.grupo)
    if (select_.id == "academico_select_nivel" || select_.id == "edad_select_edades")
    {
        info_extra = select_.options[select_.selectedIndex].value
        json_info_extra = {"info":info_extra, "grupo":select_.dataset.grupo}
    }
}
function sessionStorage_tipo_candidato(tipo_candidato_)
{
    if(tipo_candidato_ == "presidenciales")
    {
        let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Presidenciales' }
        sessionStorage.setItem('data_filtro',JSON.stringify(data))
    }
    else if(tipo_candidato_ == "congresales")
    {
        let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Congresales' }
        sessionStorage.setItem('data_filtro',JSON.stringify(data))
    
    }
    else if(tipo_candidato_ == "parlamento")
    {
        let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Parlamento Andino' }
        sessionStorage.setItem('data_filtro',JSON.stringify(data))
    }
}



function busqueda_url(id_)
{
    let tipo_candidato = json_tipo_candidato["tipo_candidato"]
    let organizacion_politica = json_organizacion["organizacion"]
    let info_extra = json_info_extra["info"]

    if(((id_=="edad_busqueda" || id_=="academico_busqueda") && info_extra == "") || organizacion_politica=="" || tipo_candidato==""){
        setTimeout(function(){
            UIkit.notification({
              message: 'Especifique la Organización Política, el tipo de candidato y el nivel acádemico o rango de edades',
              status: 'danger'
            })
          }, 1000)
          return 
    }
    else if(organizacion_politica=="" || tipo_candidato=="") {
          setTimeout(function(){
            UIkit.notification({
              message: 'Especifique la Organización Política y el tipo de candidato',
              status: 'danger'
            })
          }, 1000)
          return 
    }
    selects_index_0("none")

    sessionStorage_tipo_candidato(tipo_candidato)
    
    if(id_=="edad_busqueda")
    {
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([13,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&rango_edad="+info_extra+"-1&org_politica="+organizacion_politica+"-2"
    }
    else if(id_=="cargo_previos_busqueda")
    {
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([2,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&anhio_servicio=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="renuncia_busqueda"){
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([12,16]))
        window.location ="/busqueda?tipo_filter="+tipo_candidato+"&cantidad_renuncia=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="sentencias_busqueda"){
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([3, 4,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&ifsentencias=si&cant_senten=DESC-1&cant_senten_oblig=DESC-2&org_politica="+organizacion_politica+"-3"
    }
    else if (id_=="ingreso_busqueda"){
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([7,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&cant_ingreso=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="inmueble_busqueda"){
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([8,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&cant_inmuebles=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="mueble_busqueda"){
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([10,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&cant_muebles=DESC-1&org_politica="+organizacion_politica+"-2"
    }
    else if (id_=="academico_busqueda"){
        sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify([1,16]))
        window.location = "/busqueda?tipo_filter="+tipo_candidato+"&nivel_academico="+info_extra+"-1&org_politica="+organizacion_politica+"-2"
    }
}
