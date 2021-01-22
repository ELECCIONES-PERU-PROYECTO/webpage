let dni = 17903382

let win_href = window.location.hostname

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



function filter() {
  // get_range_edad()
  get_nivel_academico()
}