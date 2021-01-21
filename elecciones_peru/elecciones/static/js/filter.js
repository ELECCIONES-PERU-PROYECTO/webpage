let nivel_academico = document.getElementById("nivel_academico")
let nivel_academico_value;

function get_nivel_academico() {
  nivel_academico_value = nivel_academico.options[nivel_academico.selectedIndex].value;
  return nivel_academico_value
}
