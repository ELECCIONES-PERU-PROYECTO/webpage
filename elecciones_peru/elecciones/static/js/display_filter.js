
function tipo_candiato(element){
    if(element.text == "Candidatos Congresales"){
        document.getElementById("distrito_congreso").style = ""
        document.getElementById("postula_presidentes").style = "display : none"
        document.getElementsByName("tipo_candidato_filter")[0].id = "congresales"
        console.log(document.getElementsByName("tipo_candidato_filter")[0].id)
    }
    else if (element.text == "Candidatos Presidenciales"){
        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = ""
        document.getElementsByName("tipo_candidato_filter")[0].id = "presidenciales"
        console.log(document.getElementsByName("tipo_candidato_filter")[0].id)

    }
    else if (element.text == "Candidatos Parlamento Andino"){
        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = "display : none"
        document.getElementsByName("tipo_candidato_filter")[0].id = "parlamento"
        console.log(document.getElementsByName("tipo_candidato_filter")[0].id)


    }
}