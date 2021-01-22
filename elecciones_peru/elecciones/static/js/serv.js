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

filters: [
  {"key" : "city", "value" : "chicago"},  
  {"key" : "city", "value" : "ohio"},
 ]

async function GET_USERS() {

  // Since we have mixed filters as objects in an array
  // we must map them creating a new array with their values
   const cityParams = state.filters.map((filter) =>
        filter.key === 'city' ? filter.value : undefined
      )
  
  const ageParams = state.filters.map((filter) =>
        filter.key === 'age' ? filter.value : undefined
      )
  
    const data = await this.$axios.get('/users', {
      params: {
        city: cityParams,
        age: ageParams
      },
      paramsSerializer: (params) => {
        return qs.stringify(params, { arrayFormat: 'repeat' })
      },
    })
  }
