/*igual al inicio un enter (ver linea 212)*/
let Json_urls_orga = {
  "ALIANZA PARA EL PROGRESO"                       :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/1257.JPG",
  "JUNTOS POR EL PERU"                             :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/1264.JPG",
  "FUERZA POPULAR"                                 :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/1366.JPG",
  "PARTIDO DEMOCRATICO SOMOS PERU"                 :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/14.JPG",
  "PARTIDO POPULAR CRISTIANO - PPC"                :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/15.JPG",
  "PARTIDO NACIONALISTA PERUANO"                   :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/179.JPG",
  "VICTORIA NACIONAL"                              :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/21.JPG",
  "EL FRENTE AMPLIO POR JUSTICIA, VIDA Y LIBERTAD" :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2160.JPG",
  "AVANZA PAIS - PARTIDO DE INTEGRACION SOCIAL"    :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2173.JPG",
  "DEMOCRACIA DIRECTA"                             :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2191.JPG",
  "RENOVACION POPULAR"                             :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/22.JPG",
  "PARTIDO POLITICO NACIONAL PERU LIBRE"           :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2218.JPG",
  "FRENTE POPULAR AGRICOLA FIA DEL PERU - FREPAP"  :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2646.JPG",
  "PODEMOS PERU"                                   :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2731.JPG",
  "PARTIDO MORADO"                                 :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/2840.JPG",
  "PARTIDO APRISTA PERUANO"                        :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/32.JPG",
  "ACCION POPULAR"                                 :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/4.JPG",
  "UNION POR EL PERU"                              :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/47.JPG",
  "RENACIMIENTO UNIDO NACIONAL"                    :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/5.JPG",
  "PERU PATRIA SEGURA"                             :  "https://votoinformado.jne.gob.pe/voto/Resources/imgs/logoop/55.JPG"
}

let Json_plan_gob = {
  "ACCION POPULAR"                                 :  "https://pdfhost.io/v/rEIM3lEcH_Accin_PopularPDF.pdf",
  "VICTORIA NACIONAL"                              :  "https://pdfhost.io/v/khjAx3mPQ_Victoria_NacionalPDF.pdf",
  "AVANZA PAIS - PARTIDO DE INTEGRACION SOCIAL"    :  "https://pdfhost.io/v/~dtWUFRJf_Microsoft_Word_Anexo_5_Resumen_PDG_Avanza_Pais_221220docx.pdf",
  "PARTIDO DEMOCRATICO SOMOS PERU"                 :  "https://pdfhost.io/v/or0LK3O~2_Partido_Democrtico.pdf",
  "RENOVACION POPULAR"                             :  "https://pdfhost.io/v/AdNM57Nip_Renovacin_PopularPDF.pdf",
  "PODEMOS PERU"                                   :  "https://pdfhost.io/v/Jw4HUlLvR_PodemosPDF.pdf",
  "PARTIDO POLITICO NACIONAL PERU LIBRE"           :  "https://pdfhost.io/v/gHfVcdteX_Per_Libre_1PDF.pdf",
  "UNION POR EL PERU"                              :  "https://pdfhost.io/v/iGf~SLhhy_Unin_por_el_PerPDF.pdf",
  "PARTIDO POPULAR CRISTIANO - PPC"                :  "https://pdfhost.io/v/3nyJiYx.N_PPCPDF.pdf",
  "RENACIMIENTO UNIDO NACIONAL"                    :  "https://pdfhost.io/v/WkYdaugpF_RUNAPDF.pdf",
  "PERU PATRIA SEGURA"                             :  "https://pdfhost.io/v/KfrkVttzI_Per_Patria_SeguraPDF.pdf",
  "PARTIDO NACIONALISTA PERUANO"                   :  "https://pdfhost.io/v/TDjeDnFZN_Partido_NacionalistaPDF.pdf",
  "JUNTOS POR EL PERU"                             :  "https://pdfhost.io/v/0CzONkyG9_Juntos_por_el_PerPDF.pdf",
  "EL FRENTE AMPLIO POR JUSTICIA, VIDA Y LIBERTAD" :  "https://pdfhost.io/v/cKMvQv3dU_Frente_AmplioPDF.pdf",
  "PARTIDO MORADO"                                 :  "https://pdfhost.io/v/gfXzmadFC_Partido_MoradoPDF.pdf",
  "FUERZA POPULAR"                                 :  "https://pdfhost.io/v/JeNXHhIs2_Fuerza_PopularPDF.pdf",
  "ALIANZA PARA EL PROGRESO"                       :  "https://pdfhost.io/v/~tojb6ED7_Microsoft_Word_2020_12_21_PLAN_INTEGRAL_DE_GOBIERNO_APPdocx.pdf",
  "DEMOCRACIA DIRECTA"                             :  "https://pdfhost.io/v/Na~QKu~5h_Democracia_DirectaPDF.pdf"
  // "FRENTE POPULAR AGRICOLA FIA DEL PERU - FREPAP"  :  ""
}


function agregar_imagen_organizacion(){
  let divs_candidatos = document.getElementsByName("images-candidato")
  let div_name_orga = document.getElementsByName("orga_candidato_name")
  for(let i = 0; i < div_name_orga.length; i++){
    let url = Json_urls_orga[div_name_orga[i].textContent]
    let img = document.createElement("img");
    img.src = url
    img.width = "125"
    divs_candidatos[i].appendChild(img);
  }
}

function ver_plan_gobierno() {
  let div_plan_gob = document.getElementsByName("plan_gob")
  let org_name = document.getElementsByName("org_name")
  for(let i = 0; i < org_name.length; i++){
    let url = Json_plan_gob[org_name[i].innerText]
    let btn = document.createElement("a");
    btn.text = "Plan de Gobierno"
    btn.href = url
    btn.target = "blank"
    btn.className = "view_details_btn uk-text-center"
    if(url)
      div_plan_gob[i].appendChild(btn);
  }
}

window.onload = function(){
  var data1 = JSON.parse(sessionStorage.getItem('data_filtros_seleccionados'))
  let ul_filt_selec_ = document.getElementById("filtros_seleccionados")
  if (data1 != null){
    if(ul_filt_selec_!=null)
      agregar_filtros_selecs(data1)
  }
  if (sessionStorage.getItem("hasCodeRunBefore") === null) {
    let data = []
    sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify(data))
    sessionStorage.setItem("hasCodeRunBefore", true);
  }
  var data_ = JSON.parse(sessionStorage.getItem('data_filtro'))
  if (data_ != null){
    if(data_ ['tipo_filtro'] == "candidatos")
    activar_candidatos(data_ ['tipo_candiato_s'])
    else
    activar_organizaciones()
  }
  agregar_imagen_organizacion();
  ver_plan_gobierno();
}

function agregar_filtros_selecs(data){
  if(typeof badges !== "undefined")
    quitar_badges()
    for(let i = 0;i < data.length; i++){
      if (data[i] == "1"){
        agregar_badge("Nivel Académico")
      }
      else if( data[i]=="2"){
        agregar_badge("Cargos por Elecciones pasadas")
      }
      else if( data[i]=="3"){
        agregar_badge("Cantidad de Sentencias Penales")
      }
      else if( data[i]=="4"){
        agregar_badge("Cantidad de Sentencias por Obligaciones")
      }
      else if( data[i]=="5"){
        agregar_badge("Cantidad de Sentencias Materia")
      }
      else if( data[i]=="6"){
        agregar_badge("No tiene sentencias")
      }
      else if( data[i]=="7"){
        agregar_badge("Cantidad de Ingresos")
      }
      else if( data[i]=="8"){
        agregar_badge("Cantidad de Inmuebles")
      }
      else if( data[i]=="9"){
        agregar_badge("Valor de Inmuebles")
      }    
      else if( data[i]=="10"){
        agregar_badge("Cantidad de Muebles")
      }
      else if( data[i]=="11"){
        agregar_badge("Valor de Muebles")
      }
      else if( data[i]=="12"){
        agregar_badge("Renuncias de Otros Partidos")
      }
      else if( data[i]=="13"){
        agregar_badge("Rango de Edad")
      }
      else if( data[i]=="14"){
        //arreglar text
        agregar_badge("Oriundo de Cierto Departamento")
      }
      else if( data[i]=="15"){
        agregar_badge("Cargo al que Postula")
      }
      else if( data[i]=="16"){
        agregar_badge("Organización Política")
      }
      else if( data[i]=="17"){
        agregar_badge("Distrito Electoral")
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
  a_visited_mob = document.getElementsByClassName("orga_opt mob_opt")
  for(let i=0; i<a_visited.length; i++) 
    a_visited[i].style.background = "#8e0707"

  for(let i=0; i<a_visited_mob.length; i++)
    a_visited_mob[i].style.background = "#222"

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
    a_visited_mob = document.getElementsByClassName("cong_opt mob_opt")
    for(let i=0; i<a_visited.length; i++) 
      a_visited[i].style.background = "#8e0707"

    for(let i=0; i<a_visited_mob.length; i++)
      a_visited_mob[i].style.background = "#222"

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
    let tip_cand = document.getElementsByName("tipo_filter")[0]
    if(tip_cand_filter) {
      tip_cand_filter.id = "congresales"      
      tip_cand.value = "congresales"
    }
  }

  if(text == "Candidatos Presidenciales" || text == "Presidencial"){
    if(text == "Presidencial") 
      window.location = URL + "/" + VIEW

    clearNavOptions()
    a_visited = document.getElementsByClassName("pres_opt")
    a_visited_mob = document.getElementsByClassName("pres_opt mob_opt")
    for(let i=0; i<a_visited.length; i++)
      a_visited[i].style.background = "#8e0707"
    
    for(let i=0; i<a_visited_mob.length; i++)
      a_visited_mob[i].style.background = "#222"
    
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
    let tip_cand = document.getElementsByName("tipo_filter")[0]
    if(tip_cand_filter) {
      tip_cand_filter.id = "presidenciales"
      tip_cand.value = "presidenciales"
    }
  }

  if(text == "Candidatos Parlamento Andino" || text == "Parlamento Andino"){
    if(text == "Parlamento Andino")
      window.location = URL + "/" + VIEW

    clearNavOptions()
    a_visited = document.getElementsByClassName("parl_opt")
    a_visited_mob = document.getElementsByClassName("parl_opt mob_opt")
    for(let i=0; i<a_visited.length; i++)
      a_visited[i].style.background = "#8e0707"
    
    for(let i=0; i<a_visited_mob.length; i++)
      a_visited_mob[i].style.background = "#222"
    
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
    let tip_cand = document.getElementsByName("tipo_filter")[0]
    if(tip_cand_filter) {
      tip_cand_filter.id = "parlamento"
      tip_cand.value = "parlamento"
    }
  }
  if (text == "Organización Política"){
    activar_organizaciones(text);
  }
}
/*siempre deja un enter sobrando porque algunos browsers esperan que exista un enter al final*/