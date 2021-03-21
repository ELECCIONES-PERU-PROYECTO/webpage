function find_no_tiene(el) {
  return el == 6
}

function mostrar_tiposentencias(){
  let x = lista_orden_filtros.filter(find_no_tiene)

  if(x == 6)
    quitar_seleccion_sentencias()

  document.getElementById("si-sentencia").checked = true
  let div_opc_sentencias = document.getElementById("mostrar_sentencias")
  div_opc_sentencias.style.display="block"
  div_opc_sentencias.style.paddingLeft="10px"
}

function mostrar_input_ingreso(item){
  if (item.checked == true){
    document.getElementById("inputs-ingreso").style.display="block"
  }else{
    document.getElementById("inputs-ingreso").style.display="none"
  }
}

function mostrar_input_inmub(item){
  if (item.checked == true){
    document.getElementById("inputs-canti-inmu").style.display="block"
  }else{
    document.getElementById("inputs-canti-inmu").style.display="none"
  }
}
function mostrar_input_mueb(item){
  if (item.checked == true){
    document.getElementById("inputs-mueb").style.display="block"
  }else{
    document.getElementById("inputs-mueb").style.display="none"
  }
}

let dni_hoja_de_vida = ""
let cargo_postula_dato = ""

function verHojadeVida(element){
  // console.log(URL)
  dni_hoja_de_vida = element.id
  //cargo_postula_dato = element.dataset.cargo_postula
  cargo_postula_dato = element.name
  //cargo_postula_dato = element.dataset.cargopostulacion
  // console.log("cargo_postula_dato: ",cargo_postula_dato)
  let url_ = URL + "/candidato/hojadevida/"+dni_hoja_de_vida+"/"+cargo_postula_dato
  // console.log(url_)
  window.open(url_);
  // window.location = url_
}
