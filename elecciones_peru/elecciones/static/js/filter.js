/* ---------------Globlal Variables-----------*/
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
    }
  }
}


function onclick_renun(){
if(filtro_renuncias == false)
  {
    filtro_renuncias = true
  cant_filtros++
  console.log("cant_filtros: " ,cant_filtros)
  }
}

function onclick_edad(){
  if(filtro_edad == false){
    filtro_edad = true
    cant_filtros_ob++
    console.log("cant_filtros_new",cant_filtros_ob+cant_filtros_normales)    
    cant_filtros++
    console.log("cant_filtros: " ,cant_filtros)
    



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
  

  if(oriundo_inputs[0].checked == true){
      oriundo = document.getElementById("desplegable_oriundo")
      oriundo.style = ""
  }

  if(oriundo_inputs[1].checked == true){
        oriundo = document.getElementById("desplegable_oriundo")
        oriundo.style = "display:none"
  }    

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


function button_filter(){
  get_nivel_academico()
  let rango_edad = get_range_edad()
  let nivel_academico = get_nivel_academico()
  let cargos_previos_order = get_cargos_previos()
  let desplegable_oriundo = get_oriundo()
}
function get_oriundo(){

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


function cargos_previos() {
  let anhio_servicios = document.getElementsByName("anhio_servicio");
  for(let i = 0; i < anhio_servicios.length; i++) {
    if(anhio_servicios[i].checked == true) 
      return anhio_servicios[i].value
  }
}