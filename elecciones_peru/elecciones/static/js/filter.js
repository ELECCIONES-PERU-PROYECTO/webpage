/* ---------------Globlal Variables-----------*/
let dni = 17903382

let cantidad_wrapper = document.getElementById("cantidad_senticia_opcion")
let tipos_wrapper = document.getElementById("tipo_senticia_opcion")

let win_href = window.location.hostname

let cant_filtros = 0

let filtro_academico = false
let filtro_cargo = false
let filtro_sentencia_penal_tipos = false
let filtro_sentencia_penal_cantidad = false
let filtro_sentencia_civil_tipos = false
let filtro_sentencia_civil_cantidad = false
let filtro_bienesraices = false
let filtro_renuncias = false
let filtro_edad = false
let filtro_oriundo = false
let filtro_cargo_postula = false
let filtro_organizacion = false
let filtro_distrito = false

/* Variables de filtros*/
 //Nivel Academico
  let nivel_academico = ""
 //Cargos previos
  let cargos_previos_order = ""
 //Sentencias
  let s = ""
   




 //Bienes y Rentas
  //let cant_ingresos = ""
  //let cant_inmuebles = ""
  let valor_inmueble = ""
  let cant_muebles = ""
  let valor_mueble = ""
  
  //Renuncias
   

/*                      */
/* Contadores de tipo de queries */
//let cant_filtros_normales = 0
//let cant_filtros_ob = 0
let cant_filtro_especial = 0
/*-------------------------------*/

/*     QUERY  -> PRODUCTO FINAL    */
let query = ""
/* ---------------Globlal Variables-----------*/

/* Onclick Academico */



function onclick_cargo_popular(){
  if(filtro_cargo == false){
    filtro_cargo = true
    cant_filtros++
    cant_filtros_normales++
    console.log("cant_filtros_normales: " ,cant_filtros_normales)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " ,cant_filtros)
  }
}
function quitar_seleccion_cargo(){
  if(filtro_cargo == true)
  {
    let button_asc = document.getElementById("anhio_servicio_asc")
    button_asc.checked = false
    let button_desc = document.getElementById("anhio_servicio_desc")
    button_desc.checked = false
    filtro_cargo = false
    cant_filtros--
    cant_filtros_normales--
    console.log("cant_filtros_normales: " ,cant_filtros_normales)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " ,cant_filtros)
  }
}

function quitar_seleccion_b_r(){
  if(filtro_bienesraices == true){
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
    cant_filtros--
    cant_filtros_ob--
    console.log("cant_filtros_ob: " ,cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " ,cant_filtros)
    filtro_bienesraices = false
  }
}


function quitar_seleccion_sentencias(){

}
function quitar_seleccion_distrito(){

}

function quitar_seleccion_postula(){

}

function quitar_seleccion_edad(){
  if(filtro_edad == true){
    cant_filtros--
    cant_filtros_ob--
    console.log("cant_filtros_ob: ", cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " ,cant_filtros)
    filtro_edad = false
    let inputs = document.getElementsByName("rango_edad")
    for(let i = 0; i < inputs.length; i++){
      inputs[i].checked = false
    }
    
  }
}
function quitar_seleccion_org_politica(){
  if(filtro_organizacion == true){
    cant_filtros--
    console.log("cant_filtros: " ,cant_filtros)
    cant_filtros_normales--
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros_normales: " ,cant_filtros_normales) 
    filtro_organizacion = false
    let select_ = document.getElementById("select_org_politica")
    select_.selectedIndex = 0
  }
}

function quitar_seleccion_oriundo(){
  if(filtro_oriundo == true)
    {
      cant_filtros_normales--
      console.log("cant_filtros_normales: " ,cant_filtros_normales)
      cant_filtros--
      console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
      console.log("cant_filtros: " ,cant_filtros)
      filtro_oriundo = false
      oriundo = document.getElementById("desplegable_oriundo")
      oriundo.style = "display:none"
      oriundo_inputs = document.getElementsByName("oriundo_input")
      oriundo_inputs[0].checked = false
      oriundo_inputs[1].checked = false
    }
}

function quitar_seleccion_sentencias(){
  document.getElementById("por_obligaciones").checked = false
  document.getElementById("penal_cbx").checked = false
  document.getElementById("no_tiene").checked = false
  let inputs1 = document.getElementsByName("cant_senten")
  for (let i= 0 ; i < inputs1.length; i++){
    inputs1[i].checked = false
  }
  let inputs2 = document.getElementsByName("cant_senten_oblig")
  for (let i= 0 ; i < inputs2.length; i++){
    inputs2[i].checked = false
  }
  
  let inputs3 = document.getElementsByName("opc_mat_demanda")
  for (let i= 0 ; i < inputs3.length; i++){
    inputs3[i].checked = false
  }

  
}


//function onclick_
function togglePenal_opciones(element){
  if(element.checked == true){
    if (document.getElementById("no_tiene").checked == true){
      document.getElementById("no_tiene").checked = false
    }
    mostrar = document.getElementById("div_opc_cant_sentencias")
    mostrar.style = ""
  } 
  else if (element.checked == false){
    let mostrar = document.getElementById("div_opc_cant_sentencias")
    mostrar.style = "display:none"
    let inputs1 = document.getElementsByName("cant_senten")
    for (let i= 0 ; i < inputs1.length; i++){
      inputs1[i].checked = false
    }
  }
}
function toggleObligacion_opciones(element){
  if(element.checked == true){
    if (document.getElementById("no_tiene").checked == true){
      document.getElementById("no_tiene").checked = false
    }
    let mostrar = document.getElementById("div_opc_obligaciones")
    mostrar.style = ""
  } 
  else if (element.checked == false){
    let mostrar = document.getElementById("div_opc_obligaciones")
    mostrar.style = "display:none"
    let inputs2 = document.getElementsByName("cant_senten_oblig")
    for (let i= 0 ; i < inputs2.length; i++){
      inputs2[i].checked = false
    }
    
    let inputs3 = document.getElementsByName("opc_mat_demanda")
    for (let i= 0 ; i < inputs3.length; i++){
      inputs3[i].checked = false
    }
  }
}

function noTiene_opcion(element){
  if (element.checked == true){
    let  mostrar1 = document.getElementById("div_opc_cant_sentencias")
    let mostrar2 = document.getElementById("div_opc_obligaciones")
    mostrar1.style = "display:none"
    mostrar2.style = "display:none"
    document.getElementById("por_obligaciones").checked = false
    document.getElementById("penal_cbx").checked = false
  }
}


function onclick_sentencias(){
  filtro_sentencia = true
  cant_filtros++
  

  console.log("cant_filtros: " ,cant_filtros)
}
function onchange_org_politica(){
  if(filtro_organizacion == false){
    cant_filtros++
    filtro_organizacion = true
    cant_filtros_normales++
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " , cant_filtros)
  }
}
function onclick_br() {
  if(filtro_bienesraices == false )
  {
    filtro_bienesraices = true
    cant_filtros++
    cant_filtros_ob++
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " ,cant_filtros)
  }
}
/*
function quitar_seleccion_renuncia(){
  if(filtro_renuncias == true){
    let inputs = document.getElementsByName("cantidad_renuncia")
    cant_filtros--
    cant_filtros_ob--
    console.log("cant_filtros_ob: ", cant_filtros_ob)
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    console.log("cant_filtros: " ,cant_filtros)
    filtro_renuncias = false
    for(let i = 0 ; i < inputs.length; i++){
      inputs[i].checked = false
let counter_filtro_contador = 0

// Esconde todos los inputs que no se deben mostrar si no se marca una opción de los filtros
cantidad_wrapper.style.display = 'none'
tipos_wrapper.style.display = 'none'

}
}
*/


/* Onclick Nivel Academico */
function get_nivel_academico(){
  let nivel_academico = document.getElementById("nivel_academico")
  let nivel_academico_value = nivel_academico.options[nivel_academico.selectedIndex].value

  if(!filtro_academico) cant_filtros++
  
  filtro_academico = true
  
  console.log(nivel_academico_value)
  console.log(cant_filtros)

  return nivel_academico_value
}


/* Onclick Deseleccionar Cargos Previos */
function quitar_seleccion_cargos_pervios(){
  let cargos_previos = document.getElementsByName("anhio_servicio")

  for(let i = 0; i < cargos_previos.length; i++) 
    cargos_previos[i].checked = false

  filtro_cargo = false
  cant_filtros--

  console.log(cant_filtros)
}


/* Onclick Cargos Previos */
function get_cargos_previos(){
  let anhio_servicio_list = document.getElementsByName("anhio_servicio")

  if(!filtro_cargo) cant_filtros++

  filtro_cargo = true

  console.log(cant_filtros)

  for(let i = 0; i < anhio_servicio_list.length; i++) {
    if(anhio_servicio_list[i].checked) {
      console.log("si " + anhio_servicio_list[i].value)
      return anhio_servicio_list[i].value
    }
  }
}


/* Onclick Sentencias (solo hace que se muestren las opciones) */
function get_sentencias(){
  let sentencias_options = document.getElementsByName("opcion_sentencia")
  let sentencia_option
}
function onclick_edad(){
  if(filtro_edad == false){
    filtro_edad = true
    cant_filtros_ob++
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    cant_filtros++
    console.log("cant_filtros: " ,cant_filtros)
    


  for(let i = 0; i < sentencias_options.length; i++)
    if(sentencias_options[i].checked)
      sentencia_option = sentencias_options[i].value

  // Muestra los contenedores de cada opción
  if(sentencia_option == "tipo_sentencia") {
    tipos_wrapper.style.display = "block"
    cantidad_wrapper.style.display = "none"
  } else if (sentencia_option == "cantidad_senticia") {
    cantidad_wrapper.style.display = "block"
    tipos_wrapper.style.display = "none"
  }
}
}


/*Onclick oriundo*/
function onclick_oriundo(){
  let oriundo_inputs = document.getElementsByName("oriundo_input")

  if(filtro_oriundo == false){
    filtro_oriundo = true
    cant_filtros_normales++
    console.log("cant_filtros_normales: ", cant_filtros_normales)
    console.log("cant_filtros_new: ",cant_filtros_ob+cant_filtros_normales)    
    cant_filtros++
    console.log("cant_filtros: " ,cant_filtros)
  }
}
/* Onclick Deseleccionar Cargos Previos */
function quitar_seleccion_sentecias(){
  let sentencias_options = document.getElementsByName("opcion_sentencia")
  let delito_tipo = document.getElementById("delito_tipo")
  let demanda_tipo = document.getElementById("demanda_tipo")
  let sentencias_civiles = document.getElementsByName("civil_sentencia")
  let sentencias_penales = document.getElementsByName("penal_sentencia")

  // Pongo los radio buttons en false (sin marcar)
  for(let i = 0; i < sentencias_options.length; i++) 
    sentencias_options[i].checked = false

  for(let i = 0, j = 0; i < sentencias_civiles.length, i < sentencias_penales.length; i++, j++) {
    sentencias_civiles[i].checked = false
    sentencias_penales[i].checked = false
  }

  // Escondo los otros contenedores
  cantidad_wrapper.style.display = "none"
  tipos_wrapper.style.display = "none"

  // Hago que los selects sean default
  delito_tipo.selectedIndex = 0
  demanda_tipo.selectedIndex = 0

  if(filtro_sentencia_civil_tipos) 
    cant_filtros--
  if(filtro_sentencia_penal_tipos) 
    cant_filtros--
  if(filtro_sentencia_civil_cantidad) 
    cant_filtros--
  if(filtro_sentencia_penal_cantidad) 
    cant_filtros--

  filtro_sentencia_civil_tipos = false
  filtro_sentencia_penal_tipos = false
  filtro_sentencia_civil_cantidad = false
  filtro_sentencia_penal_cantidad = false

  console.log(delito_tipo.options[delito_tipo.selectedIndex].value)
  console.log(demanda_tipo.options[demanda_tipo.selectedIndex].value)
  console.log(cant_filtros)
}


function button_filter(){
  get_nivel_academico()
  let rango_edad = get_range_edad()
  let nivel_academico = get_nivel_academico()
  let cargos_previos_order = get_cargos_previos()
  let desplegable_oriundo = get_oriundo()
}
/* Onchange Delito - Tipo */
function get_delito() {
  let delito_tipo = document.getElementById("delito_tipo")
  let delito_tipo_value = delito_tipo.options[delito_tipo.selectedIndex].value

  if(!filtro_sentencia_penal) cant_filtros++
  
  filtro_sentencia_penal = true
  
  console.log(delito_tipo_value)
  console.log(cant_filtros)

  return delito_tipo_value
}


/* Onchange Demanda - Tipo */
function get_demanda() {
  let demanda_tipo = document.getElementById("demanda_tipo")
  let demanda_tipo_value = demanda_tipo.options[demanda_tipo.selectedIndex].value

  if(!filtro_sentencia_civil_tipos) cant_filtros++
  
  filtro_sentencia_civil_tipos = true
  
  console.log(demanda_tipo_value)
  console.log(cant_filtros)

  return demanda_tipo_value
}
function get_oriundo(){

}


/* Onchange Penal - Cantidad */
function penal_cantidad() {
  let penal_sentencia_list = document.getElementsByName("penal_sentencia")

  if(!filtro_sentencia_penal_cantidad) cant_filtros++

  filtro_sentencia_penal_cantidad = true

  console.log(cant_filtros)

  for(let i = 0; i < penal_sentencia_list.length; i++) {
    if(penal_sentencia_list[i].checked) {
      console.log("si " + penal_sentencia_list[i].value)
      return penal_sentencia_list[i].value
    }
  }
}


/* Onchange Civil - Cantidad */
function civil_cantidad() {
  let civil_sentencia_list = document.getElementsByName("civil_sentencia")

  if(!filtro_sentencia_civil_cantidad) cant_filtros++

  filtro_sentencia_civil_cantidad = true



  console.log(cant_filtros)

  for(let i = 0; i < civil_sentencia_list.length; i++) {
    if(civil_sentencia_list[i].checked) {
      console.log("si " + civil_sentencia_list[i].value)
      return civil_sentencia_list[i].value
    }
  }
}


/* Quitar Bienes y Rentas */
function quitar_seleccion_b_r(){
  if(filtro_bienesraices == true){
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
    cant_filtros--
    console.log("cant_filtros: " ,cant_filtros)
    filtro_bienesraices = false
  }
}
