// let btn_fil_org = document.getElementById("filtrar_org")
// btn_fil_org.disable = false

let filtro_id = ""
let filtro_info = ""
let orden = ""
let info_extra= ""

function mark_filters(){
  setTimeout(function(){
    UIkit.notification({
      message: 'Marque al menos un filtro', 
      status: 'danger'
  })
  }, 1000);
  return "again"
}

function button_filter_org(){
  // btn_fil_org.disable = true
  if(filtro_id==""){
    mark_filters();
  }
  let new_data = []
  sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify(new_data))
  
  let url = URL + "/" + VIEW
  if(filtro_id=="edad"){
    let rango=""
    inputs_edad = document.getElementsByName("opc_edad")
    orden_edad_ = document.getElementsByName("edad_orden")
    for(let i = 0 ; i < inputs_edad.length; i++){
      if(inputs_edad[i].checked){
        rango = inputs_edad[i].value
      }
    }
    for(let i = 0 ;i < orden_edad_.length; i++){
      filtro_info = orden_edad_[i].value
    }
    

    url = url+"/"+filtro_id+"/"+rango+"/"+filtro_info
    // console.log(url)
  } else if(filtro_id=="genero"){
    let inputs_genero = document.getElementsByName("opc_genero")
    let inputs_orden = document.getElementsByName("genero_orden")
    let genero = ""
    for(let i = 0 ; i < inputs_genero.length; i++){
      if(inputs_genero[i].checked){
        genero = inputs_genero[i].value
      }
    }
    for(let i = 0 ; i < inputs_orden.length; i++){
      if(inputs_orden[i].checked){
        orden = inputs_orden[i].value
      }
    }
    info_extra = genero
    //filtro_orden = orden
    if(orden==""){
      setTimeout(function(){
        UIkit.notification({
          message: 'Marque orden', 
          status: 'danger'
      });
      }, 1000);
      return;
    }
    url = url+"/"+ filtro_id+"/"+genero+"/"+orden
    // console.log(url)
  } else if(filtro_id=="primaria" || filtro_id == "secundaria" || 
            filtro_id == "tecnicos"  ||filtro_id == "nouni"|| 
            filtro_id == "uni" ||   filtro_id =="postgrado" || 
            filtro_id=="maestrodoctor"  
            ) {
      let orden = filtro_info

      url = url+"/"+filtro_id+"/unk"+"/"+orden
      // console.log(url)
  } else if(filtro_id=="cant_sen_penal_obliga"){
      url = url+"/"+filtro_id+"/unk/"+filtro_info
  } else if(filtro_id=="cant_sen_penal"){
      //url = url+"/"+filtro_id+"/"+filtro_info+"/unk"
      url = url+"/"+filtro_id+"/unk/" + filtro_info
    } else if(filtro_id=="cant_sen_civil"){
      //url = url+"/"+filtro_id+"/"+filtro_info+"/unk"
      url = url+"/"+filtro_id+"/unk/" + filtro_info

    } else if(filtro_id=="org_oriundo"){
    url = url+"/"+filtro_id+"/"+info_extra+"/"+filtro_info
    // console.log(url)
  }else if(filtro_id=="elecvsnacimiento_name"){
    url = url+"/"+filtro_id+"/unk/"+filtro_info
    // console.log(url)
  }else if(filtro_id=="2019priv" ){
    // console.log("2019_priv: --> filtro_info : ",filtro_info)
    //let orden_=""
    
    let inputs = document.getElementsByName("2019_ingre_dec")
    for(let i = 0 ; i < inputs.length; i++){
      if(inputs[i].checked == true)
        orden = inputs[i].value  
    }
    if(orden == "") orden = "ASC";
    
    url = url+"/"+filtro_id+"/"+filtro_info+"/"+orden
    // console.log(url)
  } else if(filtro_id=="2018priv" ){
    // console.log("2018_priv: --> filtro_info : ",filtro_info)
    if(orden == "") orden = "ASC";
    let inputs = document.getElementsByName("2018_ingre_dec")
    for(let i = 0 ; i < inputs.length; i++){
      if(inputs[i].checked == true)
      orden = inputs[i].value  
    }


    url = url+"/"+filtro_id+"/"+filtro_info+"/"+orden
    // console.log(url)
  } else if(filtro_id=="2017priv" ){
      let inputs = document.getElementsByName("2017_ingre_dec")
      for(let i = 0 ; i < inputs.length; i++){
        if(inputs[i].checked == true)
          orden = inputs[i].value  
      }

      if(orden == "") orden = "ASC";
      url = url+"/"+filtro_id+"/"+filtro_info+"/"+orden
      // console.log(url)
  } else if(filtro_id=="monto_quinque"){

    orden = filtro_info;

    url = url+"/"+filtro_id+"/unk/"+orden
    // console.log(url)
  }
  // console.log(url)
  window.location = url   
}

function quitar_todas_selecciones(id_){
  let gen_or_cont = document.getElementById("orden_genero_container")
  let edad_or_cont = document.getElementById("orden_edad_container")
  // console.log("id_: ",id_)
  let lista_inputs_all = document.getElementsByTagName("input")
  for(let i = 0 ; i<lista_inputs_all.length; i++){
    if(id_ == "org_desplegable_oriundo_" && lista_inputs_all[i].name =="org_oriundo"){
      continue
    }
     if (id_== lista_inputs_all[i].id  ){
        // console.log("------------------------------------")
       // console.log("lista_inputs_all[i].id: ", lista_inputs_all[i].id)
       // console.log("------------------------------------")

      continue
    }
    lista_inputs_all[i].checked = false
  }
  let litsta_selects = document.getElementsByTagName("select")
  for(let i = 0 ; i<litsta_selects.length; i++){
    //if(litsta_selects[i].id == id_){
    //  continue
    //}
    // console.log("dentro de funcion id_: ",id_ )
    if(id_ == "org_oriundo" || id_ =="org_desplegable_oriundo_"){
      return;
    }
    // console.log("elimina")
    litsta_selects[i].selectedIndex = 0
  }
  gen_or_cont.style.display = "none"
  edad_or_cont.style.display="none"
  document.getElementById("2019_est_present").style.display="block"
  document.getElementById("2018_est_present").style.display="block"
  document.getElementById("2017_est_present").style.display="block"

  filtro_id= ""
  filtro_info=""
  orden = ""
  info_extra= ""
}

//list.length = 0
//EDAD
function set_valor(element){
  // console.log("element.id : ",element.id)
  if(element.id == "org_desplegable_oriundo_" ){
    let select = document.getElementById("org_desplegable_oriundo_")
    info_extra = select.options[select.selectedIndex].value
    return
  }
  if(element.name != "genero_orden" && element.name != "edad_orden" && element.name !="2019_ingre_dec" && element.name !="2018_ingre_dec" && element.name !="2017_ingre_dec"){
    quitar_todas_selecciones(element.id)

  }

    filtro_id = element.name
    filtro_info = element.value
  
  if(element.name == "opc_educacion"){
    inputs_educacion = document.getElementsByName("opc_educacion")
    for(let i = 0 ; i < inputs_educacion.length; i++){
      if(inputs_educacion[i].checked == true){
        if(i ==0 || i==1){
          filtro_id = "primaria"
          filtro_info = inputs_educacion[i].value
        }
        else if(i ==2 || i==3){
          filtro_id = "secundaria"
          filtro_info = inputs_educacion[i].value
        }
        else if(i ==4 || i==5){
          filtro_id = "tecnicos" 
          filtro_info = inputs_educacion[i].value 
        }
        else if(i ==6 || i==7){
          filtro_id = "nouni"
          filtro_info = inputs_educacion[i].value  
        }
        else if(i ==8 || i==9){
          filtro_id = "uni"
          filtro_info = inputs_educacion[i].value  
        }
        else if(i ==10 || i==11){
          filtro_id = "postgrado"
          filtro_info = inputs_educacion[i].value  
        }
        else if(i ==12 || i==13){
          filtro_id = "maestrodoctor"
          filtro_info = inputs_educacion[i].value  
        }
      }
    }
  } 
  else if (element.name=="opc_edad" || element.name == "edad_orden"){
    filtro_id = "edad"
    let gen_or_cont = document.getElementById("orden_edad_container")
    let gen = document.getElementsByName("opc_edad")
    
    if(gen[0].checked || gen[1].checked|| gen[2].checked) 
    gen_or_cont.style.display = "block"
    else 
    gen_or_cont.style.display = "none"
  }
  else if(element.name == "opc_genero" || element.name == "genero_orden"){
    filtro_id = "genero"
    let gen_or_cont = document.getElementById("orden_genero_container")
    let gen = document.getElementsByName("opc_genero")
    
    if(gen[0].checked || gen[1].checked ) 
    gen_or_cont.style.display = "block"
    else 
    gen_or_cont.style.display = "none"
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

  // console.log("filtro_id: ",filtro_id)
  // console.log("filtro_info: ",filtro_info)
  // console.log("info_extra: ",info_extra)

}