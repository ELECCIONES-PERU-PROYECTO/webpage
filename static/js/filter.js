/*******************************/
// Variables
/*******************************/
let cant_filtros = 0
let lista_orden_filtros = []

let filtro_academico = false         //1 
let filtro_cargo = false             //2 OB
let filtro_penal_cant = false        //3 OB         
let filtro_oblig_cant = false        //4 OB
let filtro_oblig_mat = false         //5 
let filtro_senten_no_tiene = false   //6  
let filtro_ingres_cant = false      //7     
let filtro_inmu_cant = false        //8
let filtro_inmu_valor = false       //9
let filtro_mueb_cant = false        //10
let filtro_mueb_valor = false       //11
let filtro_renuncias = false         //12
let filtro_edad = false              //13
let filtro_oriundo = false           //14
let filtro_cargo_postula = false     //15
let filtro_organizacion = false      //16
let filtro_distrito = false          //17

let separer_order = '-'


/*******************************/
// Badges
/*******************************/
/* ELEMENTO DE LISTA DE FILTRO SELECCIONADOS */
let ul_filt_selec = document.getElementById("filtros_seleccionados")

function agregar_badge(badge_text) {
  var node = document.createElement("li")
  node.className = "option_badge"
  node.name = "badges-filtros-selec"
  node.textContent = badge_text
  console.log("agregar_badge")
  if (ul_filt_selec)
    ul_filt_selec.appendChild(node)
}

function quitar_badges() {
  let badges = document.getElementsByName("badges-filtros-selec")
  for (let i = 0; i < badges.length; i++) {
    ul_filt_selec.removeChild(badges[i])
  }
}

function notification(message) {
  setTimeout(function () {
    UIkit.notification({
      message: message,
      status: 'danger'
    })
  }, 1000)
}

/*******************************/
// Filter Button
/*******************************/
function filter_candidatos() {
  let form = document.getElementById("form_candidatos")

  let x = 1
  let tiene_sent = document.getElementById("si-sentencia")
  let sent_penal = document.getElementById("penal_cbx")
  let sent_por_oblig = document.getElementById("por_obligaciones")
  let tiene_ingresos = document.getElementById("tiene_ingresos")
  let tiene_bienes_inmuebles = document.getElementById("tiene_bienes_inmuebles")
  let tiene_bienes_muebles = document.getElementById("tiene_bienes_muebles")

  let n_academic = document.getElementsByName("nivel_academico")[0]
  let anhio_servicio_list = document.getElementsByName("anhio_servicio")
  let cant_senten_list = document.getElementsByName("cant_senten")
  let cant_senten_oblig_list = document.getElementsByName("cant_senten_oblig")
  let cant_mat_list = document.getElementsByName("opc_mat_demanda")
  let no_tiene_sentencia = document.getElementById("no_tiene")
  let orden_cant_ingreso = document.getElementsByName("cant_ingreso")
  let orden_cant_inmuebles = document.getElementsByName("cant_inmuebles")
  let orden_valor_inmuebles = document.getElementsByName("valor_inmuebles")
  let orden_cant_muebles = document.getElementsByName("cant_muebles")
  let orden_valor_muebles = document.getElementsByName("valor_muebles")
  let cantidad_renuncia = document.getElementsByName("cantidad_renuncia")
  let rango_edad = document.getElementsByName("rango_edad")
  let oriundo_de_peru = document.getElementsByName("oriundo_input")
  let departamento_nacimiento = document.getElementsByName("departamento_nacimiento")[0]
  let cargo_al_que_postula = document.getElementsByName("cargo_al_que_postula")[0]
  let org_politica = document.getElementsByName("org_politica")[0]
  let dist_electoral = document.getElementsByName("dist_electoral")[0]

  // Validators
  if (oriundo_de_peru[0].checked) {
    if (departamento_nacimiento.options[departamento_nacimiento.selectedIndex].value === "default") {
      notification('Especifique el distrito de nacimiento del filtro "Oriundo"');
      return
    }
  }

  if (tiene_sent.checked) {
    if (sent_penal.checked) {
      if (!filtro_penal_cant) {
        notification('Especifique el el tipo de sentencia')
        return
      }
    }
    if (sent_por_oblig.checked) {
      if (!filtro_oblig_cant && !filtro_oblig_mat) {
        notification('Especifique el el tipo de sentencia por obligación')
        return
      }
    }
  }

  if (tiene_ingresos.checked) {
    if (!filtro_ingres_cant) {
      notification('Especifique el orden según el monto de ingreso')
      return
    }
  }

  if (tiene_bienes_inmuebles.checked) {
    if (!filtro_inmu_cant && !filtro_inmu_valor) {
      notification('Marque al menos una sección de bienes inmuebles')
      return
    }
  }

  if (tiene_bienes_muebles.checked) {
    if (!filtro_mueb_cant && !filtro_mueb_valor) {
      notification('Especifique al menos una sección de bienes muebles')
      return
    }
  }

  if (lista_orden_filtros.length == 0) {
    notification('Escoja al menos un filtro')
    return
  }


  sessionStorage.setItem('data_filtros_seleccionados', JSON.stringify(lista_orden_filtros))
  // Apend the order to values in the form
  for (let i = 0; i < lista_orden_filtros.length; i++) {
    // console.log("Entro al form")
    switch (lista_orden_filtros[i]) {
      case 1:
        n_academic.options[n_academic.selectedIndex].value = n_academic.options[n_academic.selectedIndex].value + separer_order + x
        x++
        break;
      case 2:
        for (let i = 0; i < anhio_servicio_list.length; i++)
          if (anhio_servicio_list[i].checked)
            anhio_servicio_list[i].value = anhio_servicio_list[i].value + separer_order + x
        x++
        break;
      case 3:
        for (let i = 0; i < cant_senten_list.length; i++)
          if (cant_senten_list[i].checked)
            cant_senten_list[i].value = cant_senten_list[i].value + separer_order + x
        x++
        break;
      case 4:
        for (let i = 0; i < cant_senten_oblig_list.length; i++)
          if (cant_senten_oblig_list[i].checked)
            cant_senten_oblig_list[i].value = cant_senten_oblig_list[i].value + separer_order + x
        x++
        break;
      case 5:
        for (let i = 0; i < cant_mat_list.length; i++)
          if (cant_mat_list[i].checked)
            cant_mat_list[i].value = cant_mat_list[i].value + separer_order + x
        x++
        break;
      case 6:
        no_tiene_sentencia.value = no_tiene_sentencia.value + separer_order + x
        x++
        break;
      case 7:
        for (let i = 0; i < orden_cant_ingreso.length; i++)
          if (orden_cant_ingreso[i].checked)
            orden_cant_ingreso[i].value = orden_cant_ingreso[i].value + separer_order + x
        x++
        break;
      case 8:
        for (let i = 0; i < orden_cant_inmuebles.length; i++)
          if (orden_cant_inmuebles[i].checked)
            orden_cant_inmuebles[i].value = orden_cant_inmuebles[i].value + separer_order + x
        x++
        break;
      case 9:
        for (let i = 0; i < orden_valor_inmuebles.length; i++)
          if (orden_valor_inmuebles[i].checked)
            orden_valor_inmuebles[i].value = orden_valor_inmuebles[i].value + separer_order + x
        x++
        break;
      case 10:
        for (let i = 0; i < orden_cant_muebles.length; i++)
          if (orden_cant_muebles[i].checked)
            orden_cant_muebles[i].value = orden_cant_muebles[i].value + separer_order + x
        x++
        break;
      case 11:
        for (let i = 0; i < orden_valor_muebles.length; i++)
          if (orden_valor_muebles[i].checked)
            orden_valor_muebles[i].value = orden_valor_muebles[i].value + separer_order + x
        x++
        break;
      case 12:
        for (let i = 0; i < cantidad_renuncia.length; i++)
          if (cantidad_renuncia[i].checked)
            cantidad_renuncia[i].value = cantidad_renuncia[i].value + separer_order + x
        x++
        break;
      case 13:
        for (let i = 0; i < rango_edad.length; i++)
          if (rango_edad[i].checked)
            rango_edad[i].value = rango_edad[i].value + separer_order + x
        x++
        break;
      case 14:
        for (let i = 0; i < oriundo_de_peru.length; i++)
          if (oriundo_de_peru[i].checked)
            oriundo_de_peru[i].value = oriundo_de_peru[i].value + separer_order + x
        x++
        break;
      case 15:
        cargo_al_que_postula.options[cargo_al_que_postula.selectedIndex].value = cargo_al_que_postula.options[cargo_al_que_postula.selectedIndex].value + separer_order + x
        x++
        break;
      case 16:
        org_politica.options[org_politica.selectedIndex].value = org_politica.options[org_politica.selectedIndex].value + separer_order + x
        x++
        break;
      default:
        dist_electoral.options[dist_electoral.selectedIndex].value = dist_electoral.options[dist_electoral.selectedIndex].value + separer_order + x
        x++
        break;
    }
  }
  // Send the form
  form.submit()
}


/*******************************/
// Getters and Deletions
/*******************************/
/* Funciones de filtros (gets y quitar seleccion) algunos filtros tienen una funcion extra*/
/* FILTRO ACADEMICO */
function get_nivel_academico() {
  if (filtro_academico == false) {
    filtro_academico = true
    cant_filtros++
    lista_orden_filtros.push(1)
  }
}

function quitar_seleccion_academico() {
  if (filtro_academico == true) {
    filtro_academico = false
    cant_filtros--

    const index = lista_orden_filtros.indexOf(1)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    document.getElementById("nivel_academico").selectedIndex = 0
    nivel_academico = ""
  }
}


/* FILTRO CARGOS PREVIOS */
function get_cargos_previos() {
  if (filtro_cargo == false) {
    cant_filtros++
    filtro_cargo = true
    lista_orden_filtros.push(2)
  }
}

function quitar_seleccion_cargos_pervios() {
  if (filtro_cargo == true) {
    let button_asc = document.getElementById("anhio_servicio_asc")
    button_asc.checked = false
    let button_desc = document.getElementById("anhio_servicio_desc")
    button_desc.checked = false
    filtro_cargo = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(2)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    cargos_previos_order = ""
  }
}


/* FILTRO SENTENCIAS */
function togglePenal_opciones(element) {
  if (element.checked == true) {
    mostrar = document.getElementById("div_opc_cant_sentencias")
    mostrar.style.display = "block"
  } else if (element.checked == false) {
    mostrar = document.getElementById("div_opc_cant_sentencias")
    mostrar.style.display = "none"
  }
}

function toggleObligacion_opciones(element) {
  mostrar = document.getElementById("div_opc_obligaciones")
  if (element.checked == true) {
    mostrar.style.display = "block"
  } else if (element.checked == false) {
    mostrar.style.display = "none"
  }
}


function get_sentencias_penal_cant() {
  if (filtro_penal_cant == false) {
    filtro_penal_cant = true
    cant_filtros++
    lista_orden_filtros.push(3)
  }
  mostrar_tiposentencias()
  let cant_senten_list = document.getElementsByName("cant_senten")
  for (let i = 0; i < cant_senten_list.length; i++) {
    if (cant_senten_list[i].checked) {
      orden_cant_sentencia = cant_senten_list[i].value
    }
  }

  // console.log("lista orden filtros", lista_orden_filtros)
}

function get_sentencias_oblig_cant() {
  mostrar_tiposentencias()
  if (filtro_oblig_cant == false) {
    filtro_oblig_cant = true
    cant_filtros++
    lista_orden_filtros.push(4)

    let cant_senten_oblig_list = document.getElementsByName("cant_senten_oblig")
    for (let i = 0; i < cant_senten_oblig_list.length; i++) {
      if (cant_senten_oblig_list[i].checked) {
        orden_cant_sentencia_oblig = cant_senten_oblig_list[i].value
      }
    }
  }
  let cant_senten_oblig_list = document.getElementsByName("cant_senten_oblig")
  for (let i = 0; i < cant_senten_oblig_list.length; i++) {
    if (cant_senten_oblig_list[i].checked) {
      orden_cant_sentencia_oblig = cant_senten_oblig_list[i].value
    }
  }

  // console.log("lista orden filtros", lista_orden_filtros)
}

function get_sentencias_oblig_mat() {
  mostrar_tiposentencias()
  if (filtro_oblig_mat == false) {
    filtro_oblig_mat = true
    cant_filtros++
    lista_orden_filtros.push(5)
  }

  let cant_mat_list = document.getElementsByName("opc_mat_demanda")

  for (let i = 0; i < cant_mat_list.length; i++) {
    if (cant_mat_list[i].checked) {
      mat_demanda = cant_mat_list[i].value
    }
  }

  // console.log("lista orden filtros", lista_orden_filtros)
}

function quitar_seleccion_sentencias_menosno_tiene() {
  document.getElementById("si-sentencia").checked = false

  if (filtro_penal_cant == true) {
    document.getElementById("penal_cbx").checked = false
    orden_cant_sentencia = ""
    filtro_penal_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(3)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    let inputs = document.getElementsByName("cant_senten")
    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i].checked) {
        inputs[i].checked = false
      }
      document.getElementById("div_opc_cant_sentencias").style.display = "none"
    }
    // console.log("lista orden filtros", lista_orden_filtros)
  }

  if (filtro_oblig_cant == true) {
    document.getElementById("por_obligaciones").checked = false
    orden_cant_sentencia_oblig = ""
    filtro_oblig_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(4)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("cant_senten_oblig")

    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i].checked) {
        inputs[i].checked = false
      }
      document.getElementById("div_opc_obligaciones").style.display = "none"
    }
  }

  if (filtro_oblig_mat == true) {
    document.getElementById("por_obligaciones").checked = false
    mat_demanda = ""
    filtro_oblig_mat = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(5)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("opc_mat_demanda")

    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i].checked) {
        inputs[i].checked = false
      }
    }
  }
  document.getElementById("por_obligaciones").checked = false
  let element_ = document.getElementById("div_opc_obligaciones")
  toggleObligacion_opciones(element_)
  document.getElementById("penal_cbx").checked = false
  let element = document.getElementById("penal_cbx");
  togglePenal_opciones(element);

  document.getElementById("mostrar_sentencias").style.paddingLeft = "10px"
  document.getElementById("mostrar_sentencias").style.display = "none"
}

function quitar_seleccion_sentencias() {
  document.getElementById("por_obligaciones").checked = false
  document.getElementById("penal_cbx").checked = false
  document.getElementById("no_tiene").checked = false
  document.getElementById("si-sentencia").checked = false

  if (filtro_penal_cant == true) {
    document.getElementById("penal_cbx").checked = false
    orden_cant_sentencia = ""
    filtro_penal_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(3)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    let inputs = document.getElementsByName("cant_senten")
    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i].checked) {
        inputs[i].checked = false
      }
    }
  }

  if (filtro_oblig_cant == true) {
    document.getElementById("por_obligaciones").checked = false
    orden_cant_sentencia_oblig = ""
    filtro_oblig_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(4)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("cant_senten_oblig")

    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i].checked) {
        inputs[i].checked = false
      }
    }
  }

  if (filtro_oblig_mat == true) {
    document.getElementById("por_obligaciones").checked = false
    mat_demanda = ""
    filtro_oblig_mat = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(5)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("opc_mat_demanda")

    for (let i = 0; i < inputs.length; i++) {
      if (inputs[i].checked) {
        inputs[i].checked = false
      }
    }
  }

  if (filtro_senten_no_tiene == true) {
    filtro_senten_no_tiene = false
    no_tiene_val = ""
    cant_filtros--
    const index = lista_orden_filtros.indexOf(6)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }
  let element = document.getElementById("penal_cbx");
  togglePenal_opciones(element);
  let element_ = document.getElementById("por_obligaciones")
  toggleObligacion_opciones(element_)
  document.getElementById("mostrar_sentencias").style = "display: none;"
}

function noTiene_opcion() {
  quitar_seleccion_sentencias_menosno_tiene();

  // console.log("no tiene opcion")
  if (filtro_senten_no_tiene == false) {
    filtro_senten_no_tiene = true
    no_tiene_val = "NO"
    lista_orden_filtros.push(6)
    cant_filtros++
  }
  // console.log("lista orden filtros", lista_orden_filtros)
}


/* FILTRO BIENES Y RENTAS */
function get_bienes_rentas(element) {
  switch (element.name) {
    case "cant_ingreso":
      if (filtro_ingres_cant == false) {
        filtro_ingres_cant = true
        cant_filtros++
        lista_orden_filtros.push(7)
      }
      break;
    case "cant_inmuebles":
      if (filtro_inmu_cant == false) {
        filtro_inmu_cant = true
        cant_filtros++
        lista_orden_filtros.push(8)
      }
      break;
    case "valor_inmuebles":
      if (filtro_inmu_valor == false) {
        filtro_inmu_valor = true
        cant_filtros++
        lista_orden_filtros.push(9)
      }
      break;
    case "cant_muebles":
      if (filtro_mueb_cant == false) {
        filtro_mueb_cant = true
        cant_filtros++
        lista_orden_filtros.push(10)
      }
      break;
    case "valor_muebles":
      if (filtro_mueb_valor == false) {
        filtro_mueb_valor = true
        cant_filtros++
        lista_orden_filtros.push(11)
      }
      break;
  }
}

function quitar_seleccion_b_r() {
  if (filtro_ingres_cant) {
    filtro_ingres_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(7)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    orden_cant_ingreso = ""
  }

  if (filtro_inmu_cant) {
    filtro_inmu_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(8)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    orden_cant_inmueble = ""
  }

  if (filtro_inmu_valor) {
    filtro_inmu_valor = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(9)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    orden_valor_inmueble = ""
  }

  if (filtro_mueb_cant) {
    filtro_mueb_cant = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(10)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    orden_cant_mueble = ""
  }

  if (filtro_mueb_valor) {
    filtro_mueb_valor = false
    cant_filtros--
    const index = lista_orden_filtros.indexOf(11)

    if (index > -1) {
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
  tiene_ingresos.checked = false
  tiene_bienes_inmuebles.checked = false
  tiene_bienes_muebles.checked = false
  document.getElementById("inputs-ingreso").style.display = "none"
  document.getElementById("inputs-canti-inmu").style.display = "none"
  document.getElementById("inputs-mueb").style.display = "none"
}

/* FILTRO RENUNCIAS */
function get_renuncia() {
  if (filtro_renuncias == false) {
    filtro_renuncias = true
    cant_filtros++
    lista_orden_filtros.push(12)
  }
}

function quitar_seleccion_renuncia() {
  if (filtro_renuncias == true) {
    filtro_renuncias = false
    let inputs = document.getElementsByName("cantidad_renuncia")
    cant_filtros--

    for (let i = 0; i < inputs.length; i++) {
      inputs[i].checked = false
    }
    const index = lista_orden_filtros.indexOf(12)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
    orden_renuncias = ""
  }
}


/* FILTRO EDAD */
function get_edad() {
  if (filtro_edad == false) {
    filtro_edad = true
    lista_orden_filtros.push(13)
    cant_filtros++
  }
}

function quitar_seleccion_edad() {
  if (filtro_edad == true) {
    cant_filtros--
    filtro_edad = false

    const index = lista_orden_filtros.indexOf(13)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    let inputs = document.getElementsByName("rango_edad")
    for (let i = 0; i < inputs.length; i++) {
      inputs[i].checked = false
    }
    rango_edad_val = ""
  }
}


/* FILTRO ORIUNDO  */
function get_oriundo() {
  if (filtro_oriundo == false) {
    filtro_oriundo = true
    cant_filtros++
    lista_orden_filtros.push(14)
  }

  let oriundo_inputs = document.getElementsByName("oriundo_input")

  if (oriundo_inputs[1].checked == true) {
    document.getElementById("desplegable_oriundo").style = "display:none"
    document.getElementById("nivel_academico").selectedIndex = 0
    return
  } else if (oriundo_inputs[0].checked == true) {
    document.getElementById("desplegable_oriundo").style = ""
  }
}

function quitar_seleccion_oriundo() {
  if (filtro_oriundo == true) {
    filtro_oriundo = false
    cant_filtros--
    oriundo = document.getElementById("desplegable_oriundo")
    oriundo.style = "display:none"
    const index = lista_orden_filtros.indexOf(14)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }

    oriundo_inputs = document.getElementsByName("oriundo_input")

    for (let i = 0; i < oriundo_inputs.length; i++) {
      if (oriundo_inputs[i].checked) {
        oriundo_inputs[i].checked = false
      }
    }
  }
}


/* FILTRO CARGO POSTULA */
function get_cargo_postula() {
  if (filtro_cargo_postula == false) {
    filtro_cargo_postula = true
    cant_filtros++
    lista_orden_filtros.push(15)
  }
}

function quitar_seleccion_postula() {
  if (filtro_cargo_postula == true) {
    filtro_cargo_postula = false
    cargo_postula = ""
    cant_filtros--
    document.getElementById("cargo_postula").selectedIndex = 0

    const index = lista_orden_filtros.indexOf(15)
    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }
}


/* FILTRO  ORGANIZACION POLITICA */
function get_org_politica() {
  if (filtro_organizacion == false) {
    cant_filtros++
    filtro_organizacion = true
    lista_orden_filtros.push(16)
  }
}

function quitar_seleccion_org_politica() {
  if (filtro_organizacion == true) {
    cant_filtros--
    filtro_organizacion = false
    let select_ = document.getElementById("select_org_politica")
    select_.selectedIndex = 0
    org_politica = ""
    const index = lista_orden_filtros.indexOf(16)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }
}


/* FILTRO DISTRITO ELECTORAL */
function get_distrito_electoral() {
  if (filtro_distrito == false) {
    filtro_distrito = true
    cant_filtros++
    lista_orden_filtros.push(17)
  }
}

function quitar_seleccion_distrito() {
  if (filtro_distrito == true) {
    filtro_distrito = false
    cant_filtros--
    let select_ = document.getElementById("dist_electo")
    select_.selectedIndex = 0
    const index = lista_orden_filtros.indexOf(17)

    if (index > -1) {
      lista_orden_filtros.splice(index, 1)
    }
  }
}
