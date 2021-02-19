
window.onload = function () {
  if (sessionStorage.getItem("hasCodeRunBefore") === null) {
    let data = []
    sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify(data))
    sessionStorage.setItem("hasCodeRunBefore", true);
  }
}

window.onload =  function(){
  var data = JSON.parse(sessionStorage.getItem('data_filtro'))
  if (data != null){
    if(data['tipo_filtro'] == "candidatos")
    activar_candidatos(data['tipo_candiato_s'])
    else
    activar_organizaciones()
  }
}

window.onload =  function(){
  console.log("agregar_filtros_selecs")

  var data = JSON.parse(sessionStorage.getItem('data_filtros_seleccionados'))
  console.log(data)
  if (data != null){
    console.log("agregar_filtros_selecs")
    agregar_filtros_selecs(data)
  }
}

function agregar_filtros_selecs(data){
  console.log("agregar_filtros_selecs")
  for(let i = 0 ;i < data.length ; i++){
    if (data[i] == "1"){
      agregar_badge_academico()
      console.log("uww")
    } 
  }
}



let a_visited

function clearNavOptions() {
  let all_nav_opt = document.getElementsByClassName("nav-options")
  for (let i=0; i<all_nav_opt.length; i++)
    all_nav_opt[i].style.background = "none"
}

function activar_organizaciones(text){
  if(text == "Partidos Políticos" || text == "Organización Política")
    if(text == "Organización Política")
      window.location = URL + "/" + VIEW

  clearNavOptions()
  a_visited = document.getElementsByClassName("orga_opt")
  for(let i=0; i<a_visited.length; i++)
    a_visited[i].style.background = "#8e0707"

  let new_data = {data_filtro:'organizaciones', tipo_candiato_s : ''}
  sessionStorage.setItem('data_filtro',JSON.stringify(new_data))
  let data = JSON.parse(sessionStorage.getItem('data_filtro')) 
  let div1 = document.getElementById("filtros_candidatos")
  if(div1)
    div1.style.display ="none"
  let div2 = document.getElementById("filtros_organizaciones")
  if(div2)
    div2.style.display ="block"
}

function activar_candidatos(text){
  let div3 = document.getElementById("filtros_organizaciones")
  if(div3)
    div3.style.display ="none"	
  let div4 = document.getElementById("filtros_candidatos")
  if(div4)
    div4.style.display ="block"
  let opc_candidatos = document.getElementById("opciones_candidatos")
  if(opc_candidatos)
  opc_candidatos.style.display = ""

  if(text == "Candidatos Congresales" || text == "Congresales"){
    if(text == "Congresales")
      window.location = URL + "/" + VIEW
    
    clearNavOptions()
    a_visited = document.getElementsByClassName("cong_opt")
    for(let i=0; i<a_visited.length; i++)
      a_visited[i].style.background = "#8e0707"

    let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Congresales' }
    sessionStorage.setItem('data_filtro',JSON.stringify(data))
    let div3 = document.getElementById("filtros_organizaciones")
    if(div3)
      div3.style.display ="none"	
    let div4 = document.getElementById("filtros_candidatos")
    if(div4)
      div4.style.display ="block"
    let dist = document.getElementById("distrito_congreso")
    if(dist)
      dist.style = ""
    let post_presis = document.getElementById("postula_presidentes")
    if(post_presis)
      post_presis.style = "display : none"
    let tip_cand_filter = document.getElementsByName("tipo_candidato_filter")[0]
    if(tip_cand_filter)
      tip_cand_filter.id = "congresales"      
  }

  if(text == "Candidatos Presidenciales" || text == "Presidencial"){
    if(text == "Presidencial") 
      window.location = URL + "/" + VIEW

    clearNavOptions()
    a_visited = document.getElementsByClassName("pres_opt")
    for(let i=0; i<a_visited.length; i++)
      a_visited[i].style.background = "#8e0707"
    
    let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Presidenciales' }
    sessionStorage.setItem('data_filtro',JSON.stringify(data))
    let div3 = document.getElementById("filtros_organizaciones")
    if(div3)
      div3.style.display ="none"	  
    let div4 = document.getElementById("filtros_candidatos")
    if(div4)
      div4.style.display ="block"
    let dist = document.getElementById("distrito_congreso")
    if(dist)
      dist.style = "display : none"
    let post_presis = document.getElementById("postula_presidentes")
    if(post_presis)
      post_presis.style = ""
    let tip_cand_filter = document.getElementsByName("tipo_candidato_filter")[0]
    if(tip_cand_filter)
      tip_cand_filter.id = "presidenciales"
  }

  if(text == "Candidatos Parlamento Andino" || text == "Parlamento Andino"){
    if(text == "Parlamento Andino")
      window.location = URL + "/" + VIEW

    clearNavOptions()
    a_visited = document.getElementsByClassName("parl_opt")
    for(let i=0; i<a_visited.length; i++)
      a_visited[i].style.background = "#8e0707"
    
    let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Parlamento Andino' }
    sessionStorage.setItem('data_filtro',JSON.stringify(data))
    let div3 = document.getElementById("filtros_organizaciones")
    if(div3)
      div3.style.display ="none"	
    let div4 = document.getElementById("filtros_candidatos")
    if(div4)
      div4.style.display ="block"
    let dist = document.getElementById("distrito_congreso")
    if(dist)
      dist.style = "display : none"
    let post_presis = document.getElementById("postula_presidentes")
    if(post_presis)
      post_presis.style = "display : none"
    let tip_cand_filter = document.getElementsByName("tipo_candidato_filter")[0]
    if(tip_cand_filter)
      tip_cand_filter.id = "parlamento"
  }
}