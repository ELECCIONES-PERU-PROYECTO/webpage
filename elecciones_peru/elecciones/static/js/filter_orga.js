let filtro_id = ""
let filtro_info = ""
let orden = ""
let info_extra= ""

let data_org = {
  "edad" : "",
  "genero" : "",
  "genero_orden" : "",
  "niv_academico" : "",
  "niv_academico_orden" : "",
  "cantidad_sentencia_penal_obliga_orden" : "",
  "cantidad_sentencia_penal_orden" : "",
  "cantidad_sentencia_civil_orden" : "",
  "oriundo_orden" : "",
  "postulan_dif_distrito_orden" : "",
  "2019_estado_presento" : "",
  "2019_ingre_declar" : "",
  "2018_estado_presento" : "",
  "2018_ingre_declar" : "",
  "2017_estado_presento" : "",
  "2017_ingre_declar" : "",
  "monto_quinque_orden" : ""
}

function button_filter_org(){
  if(filtro_id==""){
    setTimeout(function(){
      UIkit.notification('Marque al menos un filtro');
    }, 1000);
    return "again"
  }

  let url = "http://127.0.0.1:8000/elecciones/candidatos"

  
}

function quitar_todas_selecciones(id_){
  let gen_or_cont = document.getElementById("orden_genero_container")
  let lista_inputs_all = document.getElementsByTagName("input")
  for(let i = 0 ; i<lista_inputs_all.length; i++){
    if(lista_inputs_all[i].id == id_){
      continue
    }
    lista_inputs_all[i].checked = false
  }
  let lista_selects = document.getElementsByTagName("select")
  for(let i = 0 ; i<lista_selects.length; i++){
    if(lista_selects[i].id == id_){
      continue
    }
    lista_selects[i].selectedIndex = 0
  }
  gen_or_cont.style.display = "none"
  filtro_id= ""
  filtro_info=""
}

function set_valor(element){
  if(element.name == "opc_edad"){
    let edad = document.getElementsByName("opc_edad")
    for(let i = 0; i < edad.length; i++) 
      if(edad[i].checked)
        data_org["edad"] = edad[i].value
        
    console.log(data_org)

  } else if(element.name == "opc_genero"){
    /* Debe seleccionarse al menos 1 género*/ 
    let gen_or_cont = document.getElementById("orden_genero_container")
    let gen = document.getElementsByName("opc_genero")
    
    // agg p
    if(gen[0].checked || gen[1].checked) 
    gen_or_cont.style.display = "block"
    else 
    gen_or_cont.style.display = "none"

    for(let i = 0; i < gen.length; i++) 
    if(gen[i].checked)
        data_org["genero"] = gen[i].value
        
    console.log("object ", data_org)

  } else if(element.name == "genero_orden") {
    let gen_ord = document.getElementsByName("genero_orden")
    for(let i=0; i<gen_ord.length; i++) 
      if(gen_ord[i].checked)
        data_org["genero_orden"] = gen_ord[i].value

    console.log("object", data_org)

  } else if(element.name == "opc_educacion"){
    let inputs_educacion = document.getElementsByName("opc_educacion")
    for(let i = 0 ; i < inputs_educacion.length; i++){
      if(inputs_educacion[i].checked){
        if(i == 0 || i == 1){
          data_org["niv_academico"] = "primaria"
          data_org["niv_academico_orden"] = inputs_educacion[i].value
        }
        else if(i == 2 || i == 3){
          data_org["niv_academico"] = "secundaria"
          data_org["niv_academico_orden"] = inputs_educacion[i].value
        }
        else if(i == 4 || i == 5){
          data_org["niv_academico"] = "tecnicos" 
          data_org["niv_academico_orden"] = inputs_educacion[i].value 
        }
        else if(i == 6 || i == 7){
          data_org["niv_academico"] = "nouni"
          data_org["niv_academico_orden"] = inputs_educacion[i].value  
        }
        else if(i == 8 || i == 9){
          data_org["niv_academico"] = "uni"
          data_org["niv_academico_orden"] = inputs_educacion[i].value  
        }
        else if(i == 10 || i == 11){
          data_org["niv_academico"] = "postgrado"
          data_org["niv_academico_orden"] = inputs_educacion[i].value  
        }
        else if(i == 12 || i == 13){
          data_org["niv_academico"] = "maestrodoctor"
          data_org["niv_academico_orden"] = inputs_educacion[i].value  
        }
      }
    }
    
    console.log(data_org)

  } else if(element.name == "cant_sen_penal_obliga"){
    let cant_sen_penal_oblig = document.getElementsByName("cant_sen_penal_obliga")
    
    for(let i = 0; i < cant_sen_penal_oblig.length; i++)
      if(cant_sen_penal_oblig[i].checked)
      data_org["cantidad_sentencia_penal_obliga_orden"] = cant_sen_penal_oblig[i].value

      console.log(data_org)
  } else if(element.name == "cant_sen_penal"){
    let cant_sen_penal = document.getElementsByName("cant_sen_penal")
    
    for(let i = 0; i < cant_sen_penal.length; i++)
    if(cant_sen_penal[i].checked)
      data_org["cantidad_sentencia_penal_orden"] = cant_sen_penal[i].value

      console.log(data_org)
  } else if(element.name == "cant_sen_civil"){
    let cant_sen_civil = document.getElementsByName("cant_sen_civil")

    for(let i = 0; i < cant_sen_civil.length; i++)
      if(cant_sen_civil[i].checked)
      data_org["cantidad_sentencia_civil_orden"] = cant_sen_civil[i].value

    console.log(data_org)
  } else if(element.name == "org_oriundo"){
    let org_oriundo = document.getElementsByName("org_oriundo")

    for(let i = 0; i < org_oriundo.length; i++)
      if(org_oriundo[i].checked)
      data_org["oriundo_orden"] = org_oriundo[i].value

    console.log(data_org)
  } else if(element.name == "postulan_dif_distrito_orden"){
    let postulan_dif_distrito_orden = document.getElementsByName("postulan_dif_distrito_orden")

    for(let i = 0; i < postulan_dif_distrito_orden.length; i++)
      if(postulan_dif_distrito_orden[i].checked)
      data_org["postulan_dif_distrito_orden"] = postulan_dif_distrito_orden[i].value

    console.log(data_org)
  } else if(element.name == "2019_est_present"){
    let est_present = document.getElementsByName("2019_est_present")

    for(let i = 0; i < est_present.length; i++)
      if(est_present[i].checked)
      data_org["2019_estado_presento"] = est_present[i].value

      console.log(data_org)
  } else if(element.name == "2019_ingre_dec"){
    let ingre_dec = document.getElementsByName("2019_ingre_dec")

    for(let i = 0; i < ingre_dec.length; i++)
    if(ingre_dec[i].checked)
      data_org["2019_ingre_declar"] = ingre_dec[i].value

      console.log(data_org)
  } else if(element.name == "2018_est_present"){
    let est_present = document.getElementsByName("2018_est_present")
    
    for(let i = 0; i < est_present.length; i++)
    if(est_present[i].checked)
      data_org["2018_estado_presento"] = est_present[i].value

    console.log(data_org)
  } else if(element.name == "2018_ingre_dec"){
    let ingre_dec = document.getElementsByName("2018_ingre_dec")

    for(let i = 0; i < ingre_dec.length; i++)
      if(ingre_dec[i].checked)
      data_org["2018_ingre_declar"] = ingre_dec[i].value
      
    console.log(data_org)
  } else if(element.name == "2017_est_present"){
    let est_present = document.getElementsByName("2017_est_present")

    for(let i = 0; i < est_present.length; i++)
      if(est_present[i].checked)
      data_org["2017_estado_presento"] = est_present[i].value

    console.log(data_org)
  } else if(element.name == "2017_ingre_dec"){
    let ingre_dec = document.getElementsByName("2017_ingre_dec")

    for(let i = 0; i < ingre_dec.length; i++)
      if(ingre_dec[i].checked)
      data_org["2017_ingre_declar"] = ingre_dec[i].value

    console.log(data_org)
  } else if(element.name == "monto_quinque"){
    let monto_quinque = document.getElementsByName("monto_quinque")

    for(let i = 0; i < monto_quinque.length; i++)
    if(monto_quinque[i].checked)
      data_org["monto_quinque_orden"] = monto_quinque[i].value

      console.log(data_org)
  } 
}


// if(filtro_id=="opc_edad"){
//   let rango=""
//   inputs_edad = document.getElementsByName("opc_edad")
//   for(let i = 0 ; i < inputs_edad.length; i++){
//     if(inputs_edad[i].checked){
//       rango = inputs_edad[i].value
//     }
//   }
//   console.log("rango: ",rango)
//   url = url+"/"+filtro_id+"/"+rango+"/"+"unk"
//   console.log("url xd", url)
//   } else if(filtro_id=="genero"){
//     let inputs_genero = document.getElementsByName("opc_genero")
//     let inputs_orden = document.getElementsByName("genero_orden")
//     let genero = ""
//     for(let i = 0 ; i < inputs_genero.length; i++){
//       if(inputs_genero[i].checked){
//         genero = inputs_genero[i].value
//       }
//     }
//     for(let i = 0 ; i < inputs_orden.length; i++){
//       if(inputs_orden[i].checked){
//         orden = inputs_orden[i].value
//       }
//     }
//     info_extra = genero
//     //filtro_orden = orden
//     url = url+"/"+ filtro_id+"/"+genero+"/"+orden
//     console.log(url)
//   } else if(filtro_id=="primaria" || filtro_id == "secundaria" || 
//             filtro_id == "tecnicos"  ||filtro_id == "nouni"|| 
//             filtro_id == "uni" ||   filtro_id =="postgrado" || 
//             filtro_id=="maestrodoctor"  
//             ) {
//       let orden = filtro_info

//       url = url+"/"+filtro_id+"/unk"+"/"+orden
//       console.log(url)
//   } else if(filtro_id=="penal_obligaciones_in"){
//       url = url+"/"+filtro_id+"/"+filtro_info+"/unk"
//   } else if(filtro_id=="penal_cant"){
//       //url = url+"/"+filtro_id+"/"+filtro_info+"/unk"
//       url = url+"/"+filtro_id+"/unk/" + filtro_info
//     } else if(filtro_id=="civil_cant"){
//       //url = url+"/"+filtro_id+"/"+filtro_info+"/unk"
//       url = url+"/"+filtro_id+"/unk/" + filtro_info

//     } else if(filtro_id=="opc_si"){
//     url = url+"/"+filtro_id+"/"+filtro_info
//     console.log(url)
//   }else if(filtro_id=="opc_no"){
//     url = url+"/"+filtro_id+"/unk/"+filtro_info
//     console.log(url)
//   }else if(filtro_id=="elecvsnacimiento_name"){
//     url = url+"/"+filtro_id+"/unk/"+filtro_info
//     console.log(url)
//   }else if(filtro_id=="2019priv" ){
//     console.log("2019_priv: --> filtro_info : ",filtro_info)
//     let bool_presento=""
//     let orden_=""
//     let bool_presento_inputs = document.getElementsByName("2019_presente")
//     let orden_inputs = document.getElementsByName("2019_ingre")
//     for(let i = 0 ; i < bool_presento_inputs.length; i++){
//       if(bool_presento_inputs[i].checked == true)
//         bool_presento = bool_presento_inputs[i].value  
//     }
//     for(let i = 0 ; i < orden_inputs.length; i++){
//       if(orden_inputs[i].checked == true)
//         orden_ = orden_inputs[i].value  
//     }

//     url = url+"/"+filtro_id+"/"+bool_presento+"/"+orden_
//     console.log(url)
//   } else if(filtro_id=="2018priv" ){
//     console.log("2018_priv: --> filtro_info : ",filtro_info)
//     let bool_presento=""
//     let orden_=""
//     let bool_presento_inputs = document.getElementsByName("2018_presente")
//     let orden_inputs = document.getElementsByName("2018_ingre")
//     for(let i = 0 ; i < bool_presento_inputs.length; i++){
//       if(bool_presento_inputs[i].checked == true)
//         bool_presento = bool_presento_inputs[i].value  
//     }
//     for(let i = 0 ; i < orden_inputs.length; i++){
//       if(orden_inputs[i].checked == true)
//         orden_ = orden_inputs[i].value  
//     }

//     url = url+"/"+filtro_id+"/"+bool_presento+"/"+orden_
//     console.log(url)
//   } else if(filtro_id=="2017priv" ){
//       console.log("2018_priv: --> filtro_info : ",filtro_info)
//       let bool_presento=""
//       let orden_=""
//       let bool_presento_inputs = document.getElementsByName("2017_presente")
//       let orden_inputs = document.getElementsByName("2017_ingre")
//       for(let i = 0 ; i < bool_presento_inputs.length; i++){
//         if(bool_presento_inputs[i].checked == true)
//           bool_presento = bool_presento_inputs[i].value  
//       }
//       for(let i = 0 ; i < orden_inputs.length; i++){
//         if(orden_inputs[i].checked == true)
//           orden_ = orden_inputs[i].value  
//       }

//       url = url+"/"+filtro_id+"/"+bool_presento+"/"+orden_
//       console.log(url)
//   } else if(filtro_id=="publico_orden"){
//     url = url+"/"+filtro_id+"/"+filtro_info
//     console.log(url)
//   }
//   console.log(url)
//   window.location = url 