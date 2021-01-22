let dni = 17903382

win_href = window.location.hostname

function get_nivel_academico(){
  let nivel_academico = document.getElementById("nivel_academico")
  let nivel_academico_value = nivel_academico.options[nivel_academico.selectedIndex].value;
  // location.replace('https://' + win_href + ':8000/elecciones/candidatos/estudios/' + nivel_academico_value)
}

function filter() {
  // get_range_edad()
  get_nivel_academico()
}