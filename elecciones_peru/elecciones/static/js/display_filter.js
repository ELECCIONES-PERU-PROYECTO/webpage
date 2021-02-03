/*
function tipo_candiato(element){
    if(element.text == "Candidatos Congresales"){
        let div3 = document.getElementById("filtros_organizaciones")
        div3.style.display ="none"	
        let div4 = document.getElementById("filtros_candidatos")
        div4.style.display ="block"



        document.getElementById("distrito_congreso").style = ""
        document.getElementById("postula_presidentes").style = "display : none"
        document.getElementsByName("tipo_candidato_filter")[0].id = "congresales"
        console.log(document.getElementsByName("tipo_candidato_filter")[0].id)
    }
    else if (element.text == "Candidatos Presidenciales"){
        let div3 = document.getElementById("filtros_organizaciones")
        div3.style.display ="none"	
        let div4 = document.getElementById("filtros_candidatos")
        div4.style.display ="block"



        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = ""
        document.getElementsByName("tipo_candidato_filter")[0].id = "presidenciales"
        console.log(document.getElementsByName("tipo_candidato_filter")[0].id)

    }
    else if (element.text == "Candidatos Parlamento Andino"){
        let div3 = document.getElementById("filtros_organizaciones")
        div3.style.display ="none"	
        let div4 = document.getElementById("filtros_candidatos")
        div4.style.display ="block"


        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = "display : none"
        document.getElementsByName("tipo_candidato_filter")[0].id = "parlamento"
        console.log(document.getElementsByName("tipo_candidato_filter")[0].id)


    }
}

*/

		
function activar_organizaciones(){
    console.log("activar_organizaciones")
    
    //let new_data = JSON.parse(sessionStorage.getItem('data_filtro')) 
    //new_data['data_filtro'] = 'organizaciones'
    let new_data = {data_filtro:'organizaciones', tipo_candiato_s : ''}
    
    sessionStorage.setItem('data_filtro',JSON.stringify(new_data))

    
    let data = JSON.parse(sessionStorage.getItem('data_filtro')) 
    console.log("despues del update -> data['data_filtro'] : " , data['data_filtro'])

    let div1 = document.getElementById("filtros_candidatos")
    div1.style.display ="none"
    let div2 = document.getElementById("filtros_organizaciones")
    div2.style.display ="block"
    //let tabla_organizaciones = document.getElementById("tabla_organizaciones")
    //let tabla_candidatos = document.getElementById("tabla_candidatos")    
    //let columnas1 = document.getElementsByName("columnas_congresales") 
    //for(let i =0  ; i < columnas.length  ; i++){
    //    columnas1[i].style.display="display:none"
    //}
//
    //let columnas2 = document.getElementsByName("columnas_organizaciones") 
    //for(let i =0  ; i < columnas.length  ; i++){
    //    columnas2[i].style.display=""
    //}
    //let columnas3 = document.getElementsByName("columnas_presidenciales") 
    //for(let i =0  ; i < columnas.length  ; i++){
    //    columnas3[i].style.display="display:none"
    //}

    //tabla_organizaciones.style.display="block"
    //tabla_candidatos.style.display="none"
}
function activar_candidatos(text){
    console.log("activar_candidatos")




    let div3 = document.getElementById("filtros_organizaciones")
    div3.style.display ="none"	
    let div4 = document.getElementById("filtros_candidatos")
    div4.style.display ="block"



    let opc_candidatos = document.getElementById("opciones_candidatos")
    opc_candidatos.style.display = ""

    //let columnas_congresales_ = document.getElementsByName("columnas_congresales")
    //let columnas_presidenciales_ = document.getElementsByName("columnas_presidenciales")
//
    //let columnas2 = document.getElementsByName("columnas_organizaciones") 
    //for(let i =0  ; i < columnas2.length  ; i++){
    //    columnas2[i].style.display="display:none"
    //}
    //tabla_organizaciones.style.display="none"
    //tabla_candidatos.style.display="block"
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

        //for (let i = 0 ; i < columnas_presidenciales_.length; i++){
        //    columnas_presidenciales_[i].style = ""
        //}
//
        //for (let i = 0 ; i < columnas_congresales_.length; i++){
        //    columnas_congresales_[i].style = "display:none"
        //}

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
        //for (let i = 0 ; i < columnas_presidenciales_.length; i++){
        //    columnas_presidenciales_[i].style = "display:none"
        //}
//
        //for (let i = 0 ; i < columnas_congresales_.length; i++){
        //    columnas_congresales_[i].style = "display:none"
        //}

    }


}

let dni_hoja_de_vida = ""
function verHojadeVida(element){   
    //let jeje = document.getElementsByName("get_candidato_dato")
    dni_hoja_de_vida = element.textContent
    let url_ = "http://127.0.0.1:8000/elecciones/candidato/hojadevida/"+ dni_hoja_de_vida
    
    window.location = url_
    console.log(element.textContent)
    getHojadeVida()


}