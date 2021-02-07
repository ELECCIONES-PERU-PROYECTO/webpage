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
    const response = await axios.get('/candidatos/?filtro_id='+filtro_id+"/?info_extra="+info_extra+"/?orden="+orden)
    //const response = await axios.get('/candidatos/opc_edad/30-50/ASC')

    console.log(response)
  } catch (error) {
    console.error(error)
  }
}

async function getHojadeVida() {
  try {
    const response = await axios.get("/candidato/hojadevida/?dni_hoja_de_vida="+dni_hoja_de_vida+"/?cargo_postula_dato="+cargo_postula_dato)
    //const response = await axios.get('/candidatos/opc_edad/30-50/ASC')
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}

async function mainpage(){
  console.log("loading mainpage")
  try {
    const response = await axios.get('')
    console.log(response)
  } catch (error) {
    console.error(error)
  }
}

async function test() {
  try {
    const response = await axios.post('/candidatos/test', data)
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
    console.log(response);
  } catch (error) {
    console.error(error);
  }
}