let dni = 17903382

let win_href = window.location.hostname

let cant_filtros = 0

let filtro_academico = false
let filtro_cargo = false
let filtro_sentencia = false
let filtro_bienesraices = false
let filtro_renuncias = false
let filtro_edad = false
let filtro_oriundo = false
let filtro_cargo_postula = false
let filtro_organizacion = false
let filtro_distrito = false

/* Onclick Academico */

function onclick_cargo_popular(){
  if(filtro_cargo == false){
    filtro_cargo = true
    cant_filtros++
  }
}
function quitar_seleccion_cargo(){
  let button_asc = document.getElementById("anhio_servicio_asc")
  button_asc.checked = false
  let button_desc = document.getElementById("anhio_servicio_desc")
  button_desc.checked = false
  filtro_cargo = false
  cant_filtros--
}

function quitar_seleccion_b_r(){
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

//function onclick_

function onclick_sentencias(){
  filtro_sentencia = true
  cant_filtros++
}


function onclick_br() {
  filtro_bienesraices = true
  cant_filtros++
}

function onclick_renun(){
  filtro_renuncias = true
  cant_filtros++
}

function onclick_edad(){
  filtro_edad = true
}


function get_range_edad(){
  rango1 = document.getElementById("rango_edad1")
  rango2 = document.getElementById("rango_edad2")
  rango3 = document.getElementById("rango_edad3")
  if (rango1.checked != true && rango2.checked != true && rango3.checked != true ){        
    console.log("filtro de edad esta vacio")
    return ''
  }

  if(rango1.checked){
    console.log(rango1.value)
    filtro_edad = true
    return rango1
  }
  if(rango2.checked){
    console.log(rango2.value)
    filtro_edad = true
    return rango2
  }
  if(rango3.checked){
    console.log(rango3.value)
    filtro_edad = true
    return rango3
  }
} 

function get_nivel_academico(){
  console.log("get_nivel_academico")

  let nivel_academico = document.getElementById("nivel_academico")
  let nivel_academico_value = nivel_academico.options[nivel_academico.selectedIndex].value;

  console.log(nivel_academico_value)   
  
  return nivel_academico_value
}
function button_filter(){
  get_nivel_academico()
  let rango_edad = get_range_edad()
  let nivel_academico = get_nivel_academico()
  let cargos_previos_order = get_cargos_previos()

}


function get_cargos_previos(){
  //return anhio_servicio_asc.checked && anhio_servicio_desc.checked
  let button_asc = document.getElementById("anhio_servicio_asc")
  if (button_asc.checked != true){
      console.log("NULO CHECKED")
  }
}


  
function sentencias_(){
  tipo_sentencia.checked && cantidad_senticia.checked && penal_sentencia_asc.checked
  && penal_sentencia_desc.checked && civil_sentencia_asc.checked && civil_sentencia_desc.checked;
}

function bienes_rentas(){
  return cant_ingreso_asc.checked 
  && cant_ingreso_desc.checked && cant_inmueble_asc.checked && valor_inmueble_asc.checked && valor_inmueble_desc.checked
  && cant_muebles_asc.checked && cant_muebles_desc.checked && valor_mueble_asc.checked && valor_mueble_desc.checked 
}

function renuncias(){
  return cantidad_renuncia_asc.checked && cantidad_renuncia_desc.checked 

}
function get_nivel_academico() {
  let nivel_academico = document.getElementById("nivel_academico")
  let nivel_academico_value = nivel_academico.options[nivel_academico.selectedIndex].value;
  // location.replace('http://' + win_href + ':8000/elecciones/candidatos/estudios/' + nivel_academico_value)
  return nivel_academico_value
}

function cargos_previos() {
  let anhio_servicios = document.getElementsByName("anhio_servicio");
  for(let i = 0; i < anhio_servicios.length; i++) {
    if(anhio_servicios[i].checked == true) 
      return anhio_servicios[i].value
  }
}