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

async function getUrl_datos() {
  try {
    const response = await axios.get('/candidatos/?nivel_academico='+ nivel_academico+"/?cargos_previos_order="+cargos_previos_order+"/?orden_cant_sentencia="+orden_cant_sentencia+"/?orden_cant_sentencia_oblig="+orden_cant_sentencia_oblig+"/?mat_demanda="+mat_demanda+"/?no_tiene_val="+no_tiene_val+"/?orden_cant_ingreso="+orden_cant_ingreso+"/?orden_cant_inmueble="+orden_cant_inmueble+"/?orden_valor_inmueble="+orden_valor_inmueble+"/?orden_cant_mueble="+orden_cant_mueble+"/?=orden_valor_mueble"+orden_valor_mueble+"/?orden_renuncias="+orden_renuncias+"/?rango_edad_val="+rango_edad_val+"/?nac_per_si="+nac_per_si+"/?nac_per_no="+nac_per_no+"/?departamento_nacimiento="+departamento_nacimiento+"/?cargo_postula="+cargo_postula+"/?org_politica="+org_politica+"/?dist_electoral="+dist_electoral+"/?tipo_candidato_="+tipo_candidato_)
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}

async function getUrl_orga(){
  //path('candidatos/<str:filtro_id>/<str:organizacion>/<str:infoextra>/<str:orden>')

  try {
    const response = await axios.get('/candidatos/?filtro_id='+filtro_id+"/?organizacion="+organizacion+"/?info_extra="+info_extra+"/?orden="+orden)
    console.log(response)
  } catch (error) {
    console.error(error)
  }

}

async function grado_estudios() {
  try {
    const response = await axios.get('/candidatos/estudios/?niv_acad=' + nivel_academico_value)
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}


async function test() {
  try {
    const response = await axios.get('/candidatos/?nivel_academico='+nivel_academico)
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
