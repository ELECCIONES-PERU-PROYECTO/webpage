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

let counter_filtro_contador = 0

// Esconde todos los inputs que no se deben mostrar si no se marca una opción de los filtros
cantidad_wrapper.style.display = 'none'
tipos_wrapper.style.display = 'none'


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

/* Onchange Bienes y Rentas */

// Porfa aumenta las funciones que faltan :(
// No me alcanzó tiempo uu
// Me avisas cualquier cosa uwu