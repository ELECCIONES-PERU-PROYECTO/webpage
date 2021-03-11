let organizacion_politica = ""
let info_extra = ""
let tipo_candidato = ""

function cambiar_organizacion(select_)
{  
    if (select_.id == "academico_select" || select_.id == "edad_select")
    {
        info_extra = select_.options[select_.selectedIndex].value
        return;
    }
    
    organizacion_politica = select_.options[select_.selectedIndex].value
    document.getElementById("academico_select").selectedIndex = 0
    document.getElementById("edad_select").selectedIndex = 0
    info_extra = ""
}

function tipo_candidato_select(select_)
{
    tipo_candidato = select_.options[select_.selectedIndex].value
    console.log("tipo_candidato",tipo_candidato)
}


function busqueda_url(id_)
{   
  
    if(id_=="edad_busqueda")
    {
        window.location = "http://127.0.0.1:8000/busqueda/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/"+info_extra+"(1/unk/unk/unk/unk/"+organizacion_politica+"(2/unk/"+tipo_candidato
    }
    else if (id_=="bien_mueble"){
        window.location = "http://127.0.0.1:8000/busqueda/unk/DESC(1/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/unk/"+organizacion_politica+"(2/unk/"+tipo_candidato
    }
    else if (id_=="inmueble_busqueda"){}
    else if (id_=="ingreso_busqueda"){}
    else if (id_=="sentencias_busqueda"){}
    else if (id_=="renuncia_busqueda"){}
    else if (id_=="cargo_previos_busqueda"){}
    else if (id_=="academico_busqueda"){}

}


