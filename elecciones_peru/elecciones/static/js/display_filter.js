
function tipo_candiato(element){
    if(element.text == "Candidatos Congresales"){
        document.getElementById("distrito_congreso").style = ""
        document.getElementById("postula_presidentes").style = "display : none"
    }
    else if (element.text == "Candidatos Presidenciales"){
        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = ""

    }
    else if (element.text == "Candidatos Parlamento Andino"){
        document.getElementById("distrito_congreso").style = "display : none"
        document.getElementById("postula_presidentes").style = "display : none"

    }
}