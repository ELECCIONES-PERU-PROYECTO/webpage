// let btn_fil_cand = document.getElementById("filtrar_cand")
// btn_fil_cand.disable = false
let cant_filtros = 0
let lista_orden_filtros = []

// Filtro Académico
let filtro_academico = false         //1 

// Filtro Cargo
let filtro_cargo = false             //2 OB

// Filtro Sentencias Penales
let filtro_penal_cant = false        //3 OB         
// Filtro Sentencias por Obligaciones - Cantidad
let filtro_oblig_cant = false        //4 OB
// Filtro Sentencias por Obligaciones - Material de Demanda
let filtro_oblig_mat = false         //5 
// WARNING : donde está el de familia? 
// Filtro Sentencias No Tiene
let filtro_senten_no_tiene = false   //6  

// Filtro Bienes y Rentas  - Cantidad Ingresos
let filtro_ingres_cant = false      //7     
// Filtro Bienes y Rentas  - Cantidad Inmuebles        
let filtro_inmu_cant = false        //8
// Filtro Bienes y Rentas  - Valor Inmuebles
let filtro_inmu_valor = false       //9
// Filtro Bienes y Rentas  - Cantidad Muebles
let filtro_mueb_cant = false        //10
// Filtro Bienes y Rentas  - Valor Muebles
let filtro_mueb_valor = false       //11

// Filtro Renuncias
let filtro_renuncias = false         //12

// Filtro Edad
let filtro_edad = false              //13

// Filtro Oriundo
let filtro_oriundo = false           //14

// Filtro Cargo al que Postula
let filtro_cargo_postula = false     //15

// Filtro Org Política
let filtro_organizacion = false      //16

// Filtro Distrito
let filtro_distrito = false          //17   


/* Variables de filtros*/
 // Nivel Academico
  let nivel_academico = ""      
 // Cargos previos
  let cargos_previos_order = ""   // ob1
 // Sentencias
  let orden_cant_sentencia = ""    // ob2
  let orden_cant_sentencia_oblig = ""  // ob3
  let mat_demanda = ""
  let no_tiene_val = ""         
  // Bienes y rentas
  let orden_cant_ingreso = ""    // ob 6
  let orden_cant_inmueble = ""  // ob 7
  let orden_valor_inmueble = "" // ob 8
  let orden_cant_mueble = ""  // ob 9
  let orden_valor_mueble = "" // ob 10
  // Renuncias
  let orden_renuncias = ""   // ob 11
  // Edad
  let rango_edad_val = ""
  // Oriundo
  let nac_per_si = ""
  let nac_per_no = ""
  let departamento_nacimiento = ""
  // Cargo al que Postula
  let cargo_postula = ""
  // Organizacion Politica
  let org_politica = ""
  // Distrito electoral
  let dist_electoral = ""
  let tipo_candidato_ = ""
  
/* Contadores de tipo de queries */
let cant_filtros_normales = 0
let cant_filtros_ob = 0

/* ELEMENTO DE LISTA DE FILTRO SELECCIONADOS */
let ul_filt_selec = document.getElementById("filtros_seleccionados")

function SendJSON() {
  console.log("Empacando datos")
  let data = {
    "nivel_academico" : "concluyo_secundaria",
    "cargos_previos_order" : "DESC",
    "orden_cant_sentencia" : "",
    "orden_cant_sentencia_oblig" : "",
    "mat_demanda" : "",
    "no_tiene_val" : "",
    "orden_cant_ingreso" : "",
    "orden_cant_inmueble" : "",
    "orden_valor_inmueble" : "",
    "orden_cant_mueble" : "",
    "orden_valor_mueble" : "",
    "orden_renuncias" : "",
    "rango_edad_val" : "",
    "nac_per_si" : "",
    "nac_per_no" : "",
    "departamento_nacimiento" : "",
    "cargo_postula" : "",
    "org_politica" : "",
    "dist_electoral" : "",
    "tipo_candidato_" : ""
  }
  window.location = URL + VIEW + "/test"
}

function button_filter(){
  // btn_fil_cand.disable = true
  tipo_candidato_ = document.getElementsByName("tipo_candidato_filter")[0].id

  let lista_valores = [
    nivel_academico, cargos_previos_order, orden_cant_sentencia,
    orden_cant_sentencia_oblig, mat_demanda, no_tiene_val, 
    orden_cant_ingreso, orden_cant_inmueble, orden_valor_inmueble,
    orden_cant_mueble, orden_valor_mueble, orden_renuncias, 
    rango_edad_val, nac_per_si, nac_per_no, 
    departamento_nacimiento, cargo_postula, org_politica, 
    dist_electoral, tipo_candidato_
  ]

  if(lista_orden_filtros.length == 0){
		setTimeout(function(){
			UIkit.notification({
        message: 'Escoja al menos un filtro', 
        status: 'warning'
    })
    }, 1000)
    return 
  }
  else if(lista_valores[13] != "" && lista_valores[15] == ""){
		setTimeout(function(){
			UIkit.notification({
        message: 'Especifique el distrito de nacimiento del filtro "Oriundo"',
        status: 'warning'
      })
    }, 1000)
    return 
  }
  let url = URL + "/" + VIEW

  console.log("URL XDDDDDDDDDDDDDD",url)

  let x = 1
  
  sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify(lista_orden_filtros))

  for(let i = 0; i < lista_orden_filtros.length; i++){
    if(lista_orden_filtros[i] == 1){
      lista_valores[0] = lista_valores[0] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 2){
      lista_valores[1] = lista_valores[1] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 3){
      lista_valores[2] = lista_valores[2] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 4){
      lista_valores[3] = lista_valores[3] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 5){
      lista_valores[4] = lista_valores[4] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 6){
      lista_valores[5] = lista_valores[5] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 7){
      lista_valores[6] = lista_valores[6] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 8){
      lista_valores[7] = lista_valores[7] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 9){
      lista_valores[8] = lista_valores[8] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 10){
      lista_valores[9] = lista_valores[9] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 11){
      lista_valores[10] = lista_valores[10] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 12){
      lista_valores[11] = lista_valores[11] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 13){
      lista_valores[12] = lista_valores[12] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 14){
      console.log("i ",i)
      if (lista_valores[13] == ""){
        lista_valores[14] = lista_valores[14] + "(" + x
        console.log("lista_valores[13] ",lista_valores[13])
        x++
      } else {
        lista_valores[13] = lista_valores[13] + "(" + x
        console.log("lista_valores[13] ",lista_valores[13])
        x++
      }
    }
    else if(lista_orden_filtros[i] == 15){
      lista_valores[16] = lista_valores[16] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 16){
      lista_valores[17] = lista_valores[17] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 17){
      lista_valores[18] = lista_valores[18] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 18){
      lista_valores[19] = lista_valores[19] + "(" + x
      x++
    }
    else if(lista_orden_filtros[i] == 19){
      lista_valores[20] = lista_valores[20] + "(" + x
      x++
    }
  }
  
  console.log("LISTA FINAL DE VALORES ", lista_valores)

  // Apendea los valores de la lista de valores a la url
  for (let i = 0; i < lista_valores.length; i++){
    if( lista_valores[i] != ""){
      url = url + "/"+ lista_valores[i]
    }
    else{
      url = url + "/unk"
    }
  }

  console.log(url)

  window.location = url 

  return
}
function quitar_badges(){
  let badges = document.getElementsByName("badges-filtros-selec")
  for(let i =0 ;i < badges.length ; i++){
    ul_filt_selec.removeChild(badges[i])
  }
}

/* Funciones de filtros (gets y quitar seleccion) algunos filtros tienen una funcion extra*/
/* FILTRO ACADEMICO */
function get_nivel_academico(){
  if (filtro_academico == false){
    filtro_academico = true
    cant_filtros++
    cant_filtros_normales++
    console.log(lista_orden_filtros)
    lista_orden_filtros.push(1)

    ///*Agregar <li> al a la lista de filtros seleccionados */
    //var data = JSON.parse(sessionStorage.getItem('data_filtros_seleccionados'))
    //const index = data.indexOf(1)
    //if(index == -1 || data.length == 0){
    //  console.log("El badge academico no esta")
    //  agregar_badge_academico("badge-academico","Nivel Académico")
//
    //}else{
    //  console.log("el badge academico esta")
    //}
    ///*          */

    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
  let nivel_academico_ = document.getElementById("nivel_academico")
  let nivel_academico_value = nivel_academico_.options[nivel_academico_.selectedIndex].value
  nivel_academico = nivel_academico_value
  console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
  console.log("cant_filtros: ",cant_filtros)
  console.log("nivel_academico: ", nivel_academico)
}

function agregar_badge(badge_text){
  var node = document.createElement("LI");     
  node.className= "uk-badge"
  node.name = "badges-filtros-selec"
  node.textContent = badge_text
  ul_filt_selec.appendChild(node)
}

function quitar_seleccion_academico(){
  if(filtro_academico == true){
    filtro_academico = false
    cant_filtros_normales--
    cant_filtros--
    
    //let remove = document.getElementById("badge-academico")
    //ul_filt_selec.removeChild(remove)

    const index = lista_orden_filtros.indexOf(1)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
    document.getElementById("nivel_academico").selectedIndex = 0
    nivel_academico = ""
  }
}

/* FILTRO CARGOS PREVIOS */
function get_cargos_previos(){
  let anhio_servicio_list = document.getElementsByName("anhio_servicio")

if(filtro_cargo == false) {  
  cant_filtros++
  cant_filtros_ob++
  filtro_cargo = true
  lista_orden_filtros.push(2)
  
  ///*Agregar <li> al a la lista de filtros seleccionados */
  //var data = JSON.parse(sessionStorage.getItem('data_filtros_seleccionados'))
  //const index = data.indexOf(2)
  //if(index == -1 || data.length == 0){
  //  console.log("El badge academico no esta")
  //  agregar_badge_academico("badge-elecciones-pasadas","Cargos por Elecciones pasadas")
  //}else{
  //  console.log("El badge elecc pasadas esta")
  //}
  /*          */  
  
  console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )

    console.log(cant_filtros)

    for(let i = 0; i < anhio_servicio_list.length; i++) {
      if(anhio_servicio_list[i].checked) {
        cargos_previos_order = anhio_servicio_list[i].value
        console.log("cargos_previos_order: ", cargos_previos_order)
        return
      }
    }
  }

  for(let i = 0; i < anhio_servicio_list.length; i++) {
    if(anhio_servicio_list[i].checked) {
      cargos_previos_order =  anhio_servicio_list[i].value
      console.log("cargos_previos_order: ", cargos_previos_order)
    }
  }
}

function quitar_seleccion_cargos_pervios(){
  if(filtro_cargo == true) {
    let button_asc = document.getElementById("anhio_servicio_asc")
    button_asc.checked = false
    let button_desc = document.getElementById("anhio_servicio_desc")
    button_desc.checked = false
    filtro_cargo = false
    cant_filtros--
    cant_filtros_ob--
    const index = lista_orden_filtros.indexOf(2)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    cargos_previos_order = ""
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
}


/* FILTRO SENTENCIAS */
function togglePenal_opciones(element){
  if(element.checked == true){
  mostrar = document.getElementById("div_opc_cant_sentencias")
  mostrar.style = ""
  } else if (element.checked == false){
    mostrar = document.getElementById("div_opc_cant_sentencias")
    mostrar.style.display = "none"
  }
}

function toggleObligacion_opciones(element){
  mostrar = document.getElementById("div_opc_obligaciones")
  if(element.checked == true){
    mostrar.style = ""
  } else if (element.checked == false){
    mostrar.style.display = "none"
  }
}

function get_sentencias_penal_cant(){
  if(filtro_penal_cant == false){
    filtro_penal_cant = true
    cant_filtros_ob++
    cant_filtros++
    lista_orden_filtros.push(3)
    //var data = JSON.parse(sessionStorage.getItem('data_filtros_seleccionados'))
    //const index = data.indexOf(3)
    //if(index == -1 || data.length == 0){
    //  console.log("El badge academico no esta")
    //  agregar_badge_academico(lista_orden_filtros)
    //}else{
    //  console.log("El badge elecc pasadas esta")
    //}

    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
  mostrar_tiposentencias()
  let cant_senten_list = document.getElementsByName("cant_senten")
  for(let i = 0; i < cant_senten_list.length; i++) {
    if(cant_senten_list[i].checked) {
      orden_cant_sentencia = cant_senten_list[i].value
      console.log("orden_cant_sentencia: ", orden_cant_sentencia)
    }
  }
}

function get_sentencias_oblig_cant(){
  mostrar_tiposentencias()
  if( filtro_oblig_cant == false){
    filtro_oblig_cant = true
    cant_filtros_ob++
    cant_filtros++
    lista_orden_filtros.push(4)
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
    let cant_senten_oblig_list = document.getElementsByName("cant_senten_oblig")
    for(let i = 0; i < cant_senten_oblig_list.length; i++) {
      if(cant_senten_oblig_list[i].checked) {
        orden_cant_sentencia_oblig = cant_senten_oblig_list[i].value
        console.log("orden_cant_sentencia_oblig: ", orden_cant_sentencia_oblig)
      }
    }
  }
  let cant_senten_oblig_list = document.getElementsByName("cant_senten_oblig")
  for(let i = 0; i < cant_senten_oblig_list.length; i++) {
    if(cant_senten_oblig_list[i].checked) {
      orden_cant_sentencia_oblig = cant_senten_oblig_list[i].value
      console.log("orden_cant_sentencia_oblig: ", orden_cant_sentencia_oblig)
    }
  }
}

function get_sentencias_oblig_mat(){
  mostrar_tiposentencias()
  if(filtro_oblig_mat == false){
    filtro_oblig_mat = true
    cant_filtros_normales++
    cant_filtros++
    lista_orden_filtros.push(5)
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }

  let cant_mat_list = document.getElementsByName("opc_mat_demanda")

  for(let i = 0; i < cant_mat_list.length; i++) {
    if(cant_mat_list[i].checked) {
      mat_demanda = cant_mat_list[i].value
      console.log("mat_demanda: ", mat_demanda)
    }
  }
}

function quitar_seleccion_sentencias_menosno_tiene(){
  //document.getElementById("no_tiene").checked = false
  document.getElementById("si-sentencia").checked = false

  if(filtro_penal_cant  == true){
    document.getElementById("penal_cbx").checked = false
    orden_cant_sentencia = ""
    filtro_penal_cant = false
    cant_filtros_ob--
    cant_filtros--
    const index = lista_orden_filtros.indexOf(3)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    let inputs = document.getElementsByName("cant_senten")
    for(let i = 0; i < inputs.length; i++){
      if(inputs[i].checked){
        inputs[i].checked = false
      }
    document.getElementById("div_opc_cant_sentencias").style.display="none"
    }
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
  if(filtro_oblig_cant  == true){
    document.getElementById("por_obligaciones").checked = false
    orden_cant_sentencia_oblig = ""
    filtro_oblig_cant = false
    cant_filtros_ob--
    cant_filtros--
    const index = lista_orden_filtros.indexOf(4)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("cant_senten_oblig")

    for(let i = 0; i < inputs.length; i++){
      if(inputs[i].checked){
        inputs[i].checked = false
      }
    document.getElementById("div_opc_obligaciones").style.display="none"
    }
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }

  if(filtro_oblig_mat  == true){
    document.getElementById("por_obligaciones").checked = false
    mat_demanda = ""
    filtro_oblig_mat = false
    cant_filtros_normales--
    cant_filtros--
    const index = lista_orden_filtros.indexOf(5)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("opc_mat_demanda")

    for(let i = 0; i < inputs.length; i++){
      if(inputs[i].checked){
        inputs[i].checked = false
      }
    }
    
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
  document.getElementById("por_obligaciones").checked = false
  document.getElementById("penal_cbx").checked = false
  /*if(no_tiene_val == "NO") {
    no_tiene_val = ""
    cant_filtros--
    cant_filtros_normales--
    console.log("Procedo a quitar el 6")
    const index = lista_orden_filtros.indexOf(6)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }*/
  document.getElementById("mostrar_sentencias").style.paddingLeft="10px"
  document.getElementById("mostrar_sentencias").style.display="none" 
}

function quitar_seleccion_sentencias(){
  document.getElementById("por_obligaciones").checked = false
  document.getElementById("penal_cbx").checked = false
  document.getElementById("no_tiene").checked = false
  document.getElementById("no_tiene").checked = false
  document.getElementById("si-sentencia").checked = false

  if(filtro_penal_cant  == true){
    document.getElementById("penal_cbx").checked = false
    orden_cant_sentencia = ""
    filtro_penal_cant = false
    cant_filtros_ob--
    cant_filtros--
    const index = lista_orden_filtros.indexOf(3)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    let inputs = document.getElementsByName("cant_senten")
    for(let i = 0; i < inputs.length; i++){
      if(inputs[i].checked){
        inputs[i].checked = false
      }
    }
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
  if(filtro_oblig_cant  == true){
    document.getElementById("por_obligaciones").checked = false
    orden_cant_sentencia_oblig = ""
    filtro_oblig_cant = false
    cant_filtros_ob--
    cant_filtros--
    const index = lista_orden_filtros.indexOf(4)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("cant_senten_oblig")

    for(let i = 0; i < inputs.length; i++){
      if(inputs[i].checked){
        inputs[i].checked = false
      }
    }
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }

  if(filtro_oblig_mat  == true){
    document.getElementById("por_obligaciones").checked = false
    mat_demanda = ""
    filtro_oblig_mat = false
    cant_filtros_normales--
    cant_filtros--
    const index = lista_orden_filtros.indexOf(5)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("opc_mat_demanda")

    for(let i = 0; i < inputs.length; i++){
      if(inputs[i].checked){
        inputs[i].checked = false
      }
    }
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }

  if(filtro_senten_no_tiene == true) {
    filtro_senten_no_tiene = false
    no_tiene_val = ""
    cant_filtros--
    cant_filtros_normales--
    console.log("Procedo a quitar el 6")
    const index = lista_orden_filtros.indexOf(6)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }

  document.getElementById("mostrar_sentencias").style="" 
}

function noTiene_opcion(){

    quitar_seleccion_sentencias_menosno_tiene();
    
    if(filtro_senten_no_tiene == false){
      filtro_senten_no_tiene = true
      no_tiene_val = "NO"
      lista_orden_filtros.push(6)
      cant_filtros++
      cant_filtros_normales++
      
    }

}


/* FILTRO BIENES Y RENTAS */
function get_bienes_rentas(element){
  console.log("element.name: ",element.name)
  switch(element.name) {
    case "cant_ingreso":
      if(filtro_ingres_cant == false){
        filtro_ingres_cant = true
        cant_filtros++
        cant_filtros_ob++
        lista_orden_filtros.push(7)
        console.log("push 7")
        
      }
      orden_cant_ingreso = element.value
      break;
    case "cant_inmuebles":
      if(filtro_inmu_cant == false){
        filtro_inmu_cant = true
        cant_filtros++
        cant_filtros_ob++
        lista_orden_filtros.push(8)
        console.log("push 8")
        
      }
      orden_cant_inmueble = element.value
      break;
    case "valor_inmuebles":
      if(filtro_inmu_valor == false){
        filtro_inmu_valor = true
        cant_filtros++
        cant_filtros_ob++
        lista_orden_filtros.push(9)
        console.log("push 9")
        
      }
      orden_valor_inmueble = element.value
      break;
      case "cant_muebles":
        if(filtro_mueb_cant == false){
          filtro_mueb_cant = true
          cant_filtros++
          cant_filtros_ob++
          lista_orden_filtros.push(10)
          console.log("push 10")
          
        }
        orden_cant_mueble = element.value
        break;
    case "valor_muebles":
      if(filtro_mueb_valor == false){
        filtro_mueb_valor = true
        cant_filtros++
        cant_filtros_ob++
        lista_orden_filtros.push(11)
        console.log("push 11")
        
      }
      orden_valor_mueble = element.value
      break;
  }
}

function quitar_seleccion_b_r(){
    if(filtro_ingres_cant){
      filtro_ingres_cant = false
      cant_filtros--
      cant_filtros_ob--
      const index = lista_orden_filtros.indexOf(7)
      if(index > -1) {
        lista_orden_filtros.splice(index, 1)
      }
      orden_cant_ingreso = ""
    }

    if(filtro_inmu_cant){
      filtro_inmu_cant = false
      cant_filtros--
      cant_filtros_ob--
      const index = lista_orden_filtros.indexOf(8)

      if(index > -1) {
        lista_orden_filtros.splice(index, 1)
      }
      orden_cant_inmueble = ""
    }

    if(filtro_inmu_valor){
      filtro_inmu_valor = false
      cant_filtros--
      cant_filtros_ob--
      const index = lista_orden_filtros.indexOf(9)

      if(index > -1) {
        lista_orden_filtros.splice(index, 1)
      }
      orden_valor_inmueble = ""
    }

    if(filtro_mueb_cant){
      filtro_mueb_cant = false
      cant_filtros--
      cant_filtros_ob--
      const index = lista_orden_filtros.indexOf(10)

      if(index > -1) {
        lista_orden_filtros.splice(index, 1)
      }
      orden_cant_mueble = ""
    }

    if(filtro_mueb_valor){
      filtro_mueb_valor = false
      cant_filtros--
      cant_filtros_ob--
      const index = lista_orden_filtros.indexOf(11)

      if(index > -1) {
        lista_orden_filtros.splice(index, 1)
      }
      orden_valor_mueble = ""
    }

    document.getElementById("cant_ingreso_asc").checked = false
    document.getElementById("cant_ingreso_desc").checked = false
    document.getElementById("cant_inmueble_asc").checked = false
    document.getElementById("cant_inmueble_desc").checked = false
    document.getElementById("valor_inmueble_asc").checked = false
    document.getElementById("valor_inmueble_desc").checked = false
    document.getElementById("cant_mueble_asc").checked = false
    document.getElementById("cant_mueble_desc").checked = false
    document.getElementById("valor_mueble_asc").checked = false
    document.getElementById("valor_mueble_desc").checked = false
}

/* FILTRO RENUNCIAS */
function get_renuncia(){
  if(filtro_renuncias == false){
    filtro_renuncias = true
    cant_filtros++
    cant_filtros_ob++
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
    lista_orden_filtros.push(12)
  }
  let inputs = document.getElementsByName("cantidad_renuncia")
  for(let i  = 0; i < inputs.length; i++){
    if(inputs[i].checked){
      orden_renuncias = inputs[i].value
      console.log("orden_renuncias, ", orden_renuncias)
    }
  }
}

function quitar_seleccion_renuncia(){
  if(filtro_renuncias == true){
    filtro_renuncias = false
    let inputs = document.getElementsByName("cantidad_renuncia")
    cant_filtros--
    cant_filtros_ob--
    console.log("cant_filtros_ob: ", cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)

    for(let i = 0; i < inputs.length; i++){
      inputs[i].checked = false
    }
    const index = lista_orden_filtros.indexOf(12)

    if(index > -1) {
      lista_orden_filtros.splice(index, 1)
    }    
    orden_renuncias = ""
  }
}


/* FILTRO EDAD */
function get_edad(){
  if(filtro_edad == false){
    filtro_edad = true
    cant_filtros_normales++
    lista_orden_filtros.push(13)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    cant_filtros++
    console.log("cant_filtros: ",cant_filtros)
  }
  let inputs = document.getElementsByName("rango_edad")
  for(let i = 0; i < inputs.length; i++){
    if(inputs[i].checked){
      rango_edad_val = inputs[i].value
      console.log("rango_edad_val: ",rango_edad_val)
    }
  }
}

function quitar_seleccion_edad(){
  if(filtro_edad == true){
    cant_filtros--
    cant_filtros_normales--
    console.log("cant_filtros_ob: ", cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
    filtro_edad = false
    
    const index = lista_orden_filtros.indexOf(13)
    if(index > -1) {
      lista_orden_filtros.splice(index, 1)
    }    

    let inputs = document.getElementsByName("rango_edad")
    for(let i = 0; i < inputs.length; i++){
      inputs[i].checked = false
    }
    rango_edad_val = ""
  }
}


/* FILTRO ORIUNDO  */
function get_oriundo(){
  if(filtro_oriundo == false){
    filtro_oriundo = true
    cant_filtros_normales++
    console.log("cant_filtros_normales: ", cant_filtros_normales)
    console.log("cant_filtros_new: ",cant_filtros_ob+cant_filtros_normales)    
    cant_filtros++
    console.log("cant_filtros: ",cant_filtros)
    lista_orden_filtros.push(14)
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length)
  }

  let oriundo_inputs = document.getElementsByName("oriundo_input")

  if(oriundo_inputs[1].checked == true){
    document.getElementById("desplegable_oriundo").style = "display:none"
    nac_per_no = "NO"
    nac_per_si = ""
    console.log("nac_per_no: ",nac_per_no)
    document.getElementById("nivel_academico").selectedIndex = 0
    return   
  } else if(oriundo_inputs[0].checked == true){
    document.getElementById("desplegable_oriundo").style = ""
    if(nac_per_si == ""){
      nac_per_si = "SI"
      console.log("nac_per_si: ",nac_per_si)
      nac_per_no = ""
    }
  }
}

function onchange_desple_oriundo(){
  if(nac_per_si =="SI"){
    let dpt_desplegable = document.getElementById("desplegable_oriundo_")
    let dpt_ = dpt_desplegable.options[dpt_desplegable.selectedIndex].value
    departamento_nacimiento = dpt_
    console.log("departamento_nacimiento: ",departamento_nacimiento)
    if( departamento_nacimiento ==  "default"){
      quitar_seleccion_oriundo()
    }
  }
}

function quitar_seleccion_oriundo(){
  if(filtro_oriundo == true) {
    filtro_oriundo = false
    cant_filtros_normales--
    console.log("cant_filtros_normales: ",cant_filtros_normales)
    cant_filtros--
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
    oriundo = document.getElementById("desplegable_oriundo")
    oriundo.style = "display:none"
    const index = lista_orden_filtros.indexOf(14)
    
    if(index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    oriundo_inputs = document.getElementsByName("oriundo_input")

    for(let i = 0; i < oriundo_inputs.length; i++){
      if(oriundo_inputs[i].checked){
        oriundo_inputs[i].checked = false
      }
    }
    departamento_nacimiento = ""
    nac_per_no = ""
    nac_per_si = ""
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
  }
}


/* FILTRO CARGO POSTULA */
function get_cargo_postula(){
  if(filtro_cargo_postula == false){
    filtro_cargo_postula = true
    cant_filtros_normales++
    cant_filtros++
    lista_orden_filtros.push(15)
    console.log("lista_orden_filtros.length: ",lista_orden_filtros.length )
    console.log("cant_filtros_ob: ",cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ",cant_filtros)
  }
  let postula_desplegable = document.getElementById("cargo_postula")
  let postula_value = postula_desplegable.options[postula_desplegable.selectedIndex].value

  cargo_postula = postula_value 

  if(cargo_postula == "cargo_postula"){
    quitar_seleccion_postula()
  }

  console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
  console.log("cant_filtros: ",cant_filtros)
  console.log("cargo_postula: ", cargo_postula)
}

function quitar_seleccion_postula(){
  if(filtro_cargo_postula == true){
    filtro_cargo_postula = false
    cargo_postula=""
    cant_filtros_normales--
    cant_filtros--
    document.getElementById("cargo_postula").selectedIndex = 0

    const index = lista_orden_filtros.indexOf(15)
    if(index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }
}


/* FILTRO  ORGANIZACION POLITICA */
function get_org_politica(){
  if(filtro_organizacion == false){
    cant_filtros++
    filtro_organizacion = true
    cant_filtros_normales++
    lista_orden_filtros.push(16)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ", cant_filtros)
  }

  let org_politica_ = document.getElementById("select_org_politica")
  let org_politica_value = org_politica_.options[org_politica_.selectedIndex].value

  org_politica = org_politica_value

  if(org_politica == "default"){
    quitar_seleccion_org_politica()
  }

  console.log("org_politica: ", org_politica)
}

function quitar_seleccion_org_politica(){
  if(filtro_organizacion == true){
    cant_filtros--
    console.log("cant_filtros: ",cant_filtros)
    cant_filtros_normales--
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros_normales: ",cant_filtros_normales) 
    filtro_organizacion = false
    let select_ = document.getElementById("select_org_politica")
    select_.selectedIndex = 0
    org_politica = ""
    const index = lista_orden_filtros.indexOf(16)

    if(index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }
}


/* FILTRO DISTRITO ELECTORAL */
function get_distrito_electoral(){
  if(filtro_distrito == false){
    filtro_distrito = true
    cant_filtros_normales++
    cant_filtros++
    lista_orden_filtros.push(17)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: ", cant_filtros)
  }

  let distrito_ = document.getElementById("dist_electo")
  let distrito_value = distrito_.options[distrito_.selectedIndex].value

  console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
  console.log("cant_filtros: ",cant_filtros)

  //get del valor
  dist_electoral = distrito_value

  if(dist_electoral == "default"){
    quitar_seleccion_distrito()
  }
  console.log("dist_electoral: ", dist_electoral) 
}

function quitar_seleccion_distrito(){
  if(filtro_distrito  == true){
    filtro_distrito = false
    cant_filtros_normales--
    cant_filtros--
    let select_ = document.getElementById("dist_electo")
    select_.selectedIndex = 0
    const index = lista_orden_filtros.indexOf(17)
    
    if(index > -1){
      lista_orden_filtros.splice(index, 1)
    }
  }
}