let nivel_academico = document.getElementById("nivel_academico")

// Valores
let nivel_academico_value;

for (let i = 0; i < nivel_academico.length; i++) {
  if (nivel_academico[i].selected) {
    nivel_academico_value = nivel_academico[i].value;
  }
}

console.log(nivel_academico_value)
console.log("hola")