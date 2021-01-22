// Retorna todos los candidatos
async function getCandidatos() {
  try {
    const response = await axios.get('/candidatos')
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}

// Retorna el andidato que tenga el dni en la ruta
async function getCandidato() {
  try {
    const response = await axios.get('/candidato/dni/?dni='+ dni)
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}


async function grado_esudios() {
  try {
    const response = await axios.get('/candidatos/estudios/?niv_acad=' + nivel_academico_value)
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}
