
window.onload = function(){
    var data = JSON.parse(sessionStorage.getItem('data_filtro'))
    if (data != null){
      if(data['tipo_filtro'] == "candidatos")
        activar_candidatos(data['tipo_candiato_s'])
      else
        activar_organizaciones()
    }
}
		
function activar_organizaciones(){
    let new_data = {data_filtro:'organizaciones', tipo_candiato_s : ''}
    sessionStorage.setItem('data_filtro',JSON.stringify(new_data))
    let data = JSON.parse(sessionStorage.getItem('data_filtro')) 
    let div1 = document.getElementById("filtros_candidatos")
    div1.style.display ="none"
    let div2 = document.getElementById("filtros_organizaciones")
    div2.style.display ="block"

}

function activar_candidatos(text){
    let div3 = document.getElementById("filtros_organizaciones")
    div3.style.display ="none"	
    let div4 = document.getElementById("filtros_candidatos")
    div4.style.display ="block"
    let opc_candidatos = document.getElementById("opciones_candidatos")
    opc_candidatos.style.display = ""
    if(text == "Candidatos Congresales"){
        let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Congresales' }
        sessionStorage.setItem('data_filtro',JSON.stringify(data))
        let div3 = document.getElementById("filtros_organizaciones")
        div3.style.display ="none"	
        let div4 = document.getElementById("filtros_candidatos")
        div4.style.display ="block"
        document.getElementById("distrito_congreso").style = ""
        document.getElementById("postula_presidentes").style = "display : none"
        document.getElementsByName("tipo_candidato_filter")[0].id = "congresales"       
    }
    if(text == "Candidatos Presidenciales"){
        let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Presidenciales' }
        sessionStorage.setItem('data_filtro',JSON.stringify(data))
        let div3 = document.getElementById("filtros_organizaciones")
        div3.style.display ="none"	
        let div4 = document.getElementById("filtros_candidatos")
        div4.style.display ="block"
        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = ""
        document.getElementsByName("tipo_candidato_filter")[0].id = "presidenciales"
    }
    if(text == "Candidatos Parlamento Andino"){
        let data = { tipo_filtro :'candidatos', tipo_candiato_s : 'Candidatos Parlamento Andino' }
        sessionStorage.setItem('data_filtro',JSON.stringify(data))
        let div3 = document.getElementById("filtros_organizaciones")
        div3.style.display ="none"	
        let div4 = document.getElementById("filtros_candidatos")
        div4.style.display ="block"
        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = "display : none"
        document.getElementsByName("tipo_candidato_filter")[0].id = "parlamento"
    }
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
    dni_hoja_de_vida = element.id
    cargo_postula_dato = element.name
    let url_ = "http://127.0.0.1:8000/elecciones/candidato/hojadevida/"+dni_hoja_de_vida+"/"+cargo_postula_dato    
    window.location = url_
}
