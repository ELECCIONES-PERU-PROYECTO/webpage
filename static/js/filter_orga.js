// let btn_fil_org = document.getElementById("filtrar_org")
// btn_fil_org.disable = false

let filtro_id = ""
let filtro_info = ""
let orden = ""
let info_extra= ""
let have_filter = false

function mark_filters(){
  setTimeout(function(){
    UIkit.notification({
      message: 'Marque al menos un filtro', 
      status: 'danger'
  })
  }, 1000);
  return "again"
}


/*******************************/
// Filter Button
/*******************************/
function button_filter_org() {
  if(!have_filter) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque al menos un filtro', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  let form = document.getElementById("filtro_org_form")

  let sexo = document.getElementsByName("org_opc_sexo")
  let sexo_ord = document.getElementsByName("org_sexo_orden")
  let sexo_marked = false
  let sexo_ord_marked = false

  let edad = document.getElementsByName("org_rango_edad")
  let edad_ord = document.getElementsByName("org_edad_orden")
  let edad_marked = false
  let edad_ord_marked = false

  let oriundo = document.getElementsByName("org_oriundo")
  let oriundo_dep = document.getElementsByName("org_departamento_oriundo")[0]
  let oriundo_dep_value = oriundo_dep.options[oriundo_dep.selectedIndex].value
  let oriundo_marked = false

  let finan_2017 = document.getElementsByName("2017_est_present")
  let finan_2017_ord = document.getElementsByName("2017_ingre_dec")
  let finan_2017_marked = false
  let finan_2017_ord_marked = false

  let finan_2018 = document.getElementsByName("2018_est_present")
  let finan_2018_ord = document.getElementsByName("2018_ingre_dec")
  let finan_2018_marked = false
  let finan_2018_ord_marked = false

  let finan_2019 = document.getElementsByName("2019_est_present")
  let finan_2019_ord = document.getElementsByName("2019_ingre_dec")
  let finan_2019_marked = false
  let finan_2019_ord_marked = false

  ////////// Validators [No pude ponerlo en una func :( ] //////////
  // Sexo
  for(let i = 0; i < sexo.length; i++)
    if(sexo[i].checked)
      sexo_marked = true

  for(let i = 0; i < sexo_ord.length; i++)
    if(sexo_ord[i].checked)
      sexo_ord_marked = true
  

  // Edad
  for(let i = 0; i < edad.length; i++)
    if(edad[i].checked)
      edad_marked = true

  for(let i = 0; i < edad_ord.length; i++)
    if(edad_ord[i].checked)
      edad_ord_marked = true

    
  // Oriundo
  for(let i = 0; i < oriundo.length; i++)
    if(oriundo[i].checked)
      oriundo_marked = true
  
  
  // Financiamiento Privado
  for(let i = 0; i < finan_2017.length; i++) 
    if(finan_2017[i].checked)
      finan_2017_marked = true

  for(let i = 0; i < finan_2017_ord.length; i++)
    if(finan_2017_ord[i].checked)
      finan_2017_ord_marked = true

  for(let i = 0; i < finan_2018.length; i++) 
    if(finan_2018[i].checked)
      finan_2018_marked = true
  
  for(let i = 0; i < finan_2018_ord.length; i++)
    if(finan_2018_ord[i].checked)
      finan_2018_ord_marked = true

  for(let i = 0; i < finan_2019.length; i++) 
    if(finan_2019[i].checked)
      finan_2019_marked = true

  for(let i = 0; i < finan_2019_ord.length; i++)
    if(finan_2019_ord[i].checked)
      finan_2019_ord_marked = true


  // Alerts
  if(sexo_marked && !sexo_ord_marked) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque el tipo de orden en el filtro de Sexo', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  if(edad_marked && !edad_ord_marked) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque el tipo de orden en el filtro de Edad', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  if(oriundo_dep_value !== "default" && !oriundo_marked) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque el tipo de orden en el filtro de Oriundo', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  if(finan_2017_marked && !finan_2017_ord_marked) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque el tipo de orden según ingresos en el filtro de Financiamiento Privado del 2017', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  if(finan_2018_marked && !finan_2018_ord_marked) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque el tipo de orden según ingresos en el filtro de Financiamiento Privado del 2018', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  if(finan_2019_marked && !finan_2019_ord_marked) {
    setTimeout(function(){
      UIkit.notification({
        message: 'Marque el tipo de orden según ingresos en el filtro de Financiamiento Privado del 2019', 
        status: 'danger'
    });
    }, 1000);
    return
  }

  // Send the form
  form.submit()
}

function quitar_todas_selecciones(id_){
  let gen_or_cont = document.getElementById("orden_sexo_container")
  let edad_or_cont = document.getElementById("orden_edad_container")
  let drp_cnt = document.getElementById("dep_order_ctn")
  let lista_inputs_all = document.getElementsByTagName("input")
  let litsta_selects = document.getElementsByTagName("select")

  for(let i = 0 ; i<lista_inputs_all.length; i++){
    if(id_ == "org_desplegable_oriundo_" && lista_inputs_all[i].name =="org_oriundo")
      continue
    if(id_== lista_inputs_all[i].id)
      continue
    lista_inputs_all[i].checked = false
  }

  for(let i = 0 ; i<litsta_selects.length; i++){
    //if(litsta_selects[i].id == id_){
    //  continue
    //}
    // console.log("dentro de funcion id_: ",id_ )
    if(id_ == "org_oriundo" || id_ =="org_desplegable_oriundo_")
      return
    litsta_selects[i].selectedIndex = 0
  }

  gen_or_cont.style.display = "none"
  edad_or_cont.style.display="none"
  drp_cnt.style.display = "none"
  
  document.getElementById("2019_est_present").style.display="block"
  document.getElementById("2018_est_present").style.display="block"
  document.getElementById("2017_est_present").style.display="block"

  filtro_id= ""
  filtro_info=""
  orden = ""
  info_extra= ""
}

function set_valor(element){
  have_filter = true
  
  if(element.name != "org_sexo_orden" && element.name != "org_edad_orden" && element.name !="2019_ingre_dec" && element.name !="2018_ingre_dec" && element.name !="2017_ingre_dec" && element.name !="2019_est_present" && element.name !="2018_est_present" && element.name !="2017_est_present" && element.name != "org_departamento_oriundo" && element.name != "org_oriundo") {
    quitar_todas_selecciones(element.id)
  }

  if(element.name == "org_rango_edad" || element.name == "org_edad_orden"){ // Edad
    let gen_or_cont = document.getElementById("orden_edad_container")
    let gen = document.getElementsByName("org_rango_edad")
    
    if(gen[0].checked || gen[1].checked|| gen[2].checked) 
      gen_or_cont.style.display = "block"
    else 
      gen_or_cont.style.display = "none"
  } else if(element.name == "org_opc_sexo" || element.name == "org_sexo_orden"){ // Sexo
    let gen_or_cont = document.getElementById("orden_sexo_container")
    let gen = document.getElementsByName("org_opc_sexo")
    
    if(gen[0].checked || gen[1].checked ) 
      gen_or_cont.style.display = "block"
    else 
      gen_or_cont.style.display = "none"
  } else if(element.name == "org_departamento_oriundo" || element.name == "org_oriundo") {
    let drp_cnt = document.getElementById("dep_order_ctn")
    drp_cnt.style.display = "block"
  } else if(element.name =="2019_est_present" || element.name =="2019_ingre_dec"){
    filtro_id = "2019priv"
    document.getElementById("2018_est_present").style.display="none"
    document.getElementById("2017_est_present").style.display="none"
  } else if(element.name =="2018_est_present" || element.name =="2018_ingre_dec"){
    filtro_id = "2018priv"
    document.getElementById("2019_est_present").style.display="none"
    document.getElementById("2017_est_present").style.display="none"
  } else if(element.name =="2017_est_present" || element.name =="2017_ingre_dec"){
    filtro_id = "2017priv"
    document.getElementById("2019_est_present").style.display="none"
    document.getElementById("2018_est_present").style.display="none"
  }
}