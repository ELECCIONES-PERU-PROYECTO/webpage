let filtro_id = ""
let filtro_info = ""
let filtro_orden = ""


function button_filter_org(){
    if (filtro_id==""){
        setTimeout(function(){
            UIkit.notification('Marque al menos un filtro');
    }, 1000);
    return "again"
    }        
    let url = "http://127.0.0.1:8000/elecciones/candidatos"
    if(filtro_id=="opc_edad"){
        let select_edad = document.getElementById("select_org_politica_orga")
        let organizacion = select_edad.options[select_edad.selectedIndex].value
        let rango=""
        inputs_edad = document.getElementsByName("opc_edad")
        for (let i = 0 ; i < inputs_edad.length; i++){
            if(inputs_edad[i].checked){
                rango = inputs_edad[i].value
            }
        }
        console.log("rango: ",rango)
        if (organizacion=="default"){
            setTimeout(function(){
                UIkit.notification('Llene todos los 2 espacios del filtro Edad');
        }, 1000);
        return "again"
        }        
        url = url+"/"+filtro_id+"/"+organizacion+"/"+rango+"/"+"unk"
    }else if (filtro_id=="genero"){
        let select_ = document.getElementById("genero_desplegable")
        let organizacion = select_.options[select_.selectedIndex].value
        let inputs_genero = document.getElementsByName("opc_genero")
        let inputs_orden = document.getElementsByName("genero_orden")
        let orden = ""
        let genero = ""
        for (let i = 0 ; i < inputs_genero.length; i++){
            if(inputs_genero[i].checked){
                genero = inputs_genero[i].value
            }
        }
        for (let i = 0 ; i < inputs_orden.length; i++){
            if(inputs_orden[i].checked){
                orden = inputs_orden[i].value
            }
        }
        url = url+"/"+ filtro_id+"/"+organizacion+"/"+genero+"/"+orden

    }else if (filtro_id=="primaria" || filtro_id == "secundaria" || 
    filtro_id == "tecnicos"  ||filtro_id == "nouni"|| filtro_id == "uni" ||   filtro_id =="postgrado"  ||filtro_id=="maestrodoctor"  
    ){
        let select_ = document.getElementById("select_estudios")
        let organizacion = select_.options[select_.selectedIndex].value
        let orden = filtro_info

        url = url+"/"+filtro_id+"/"+organizacion+"/unk"+"/"+orden
    }else if (filtro_id=="penal_obligaciones_in"){
        let select_edad = document.getElementById("penal_select")
        let organizacion = select_edad.options[select_edad.selectedIndex].value
        url = url+"/"+filtro_id+"/"+organizacion+"/"+filtro_info+"/unk"
    }else if (filtro_id=="penal_cant"){
        let select_edad = document.getElementById("penal_select")
        let organizacion = select_edad.options[select_edad.selectedIndex].value
        url = url+"/"+filtro_id+"/"+organizacion+"/"+filtro_info+"/unk"
    }else if (filtro_id=="civil_cant"){
        let select_edad = document.getElementById("penal_select")
        let organizacion = select_edad.options[select_edad.selectedIndex].value
        url = url+"/"+filtro_id+"/"+organizacion+"/"+filtro_info+"/unk"
    }else if (filtro_id=="opc_si"){
        let select_edad = document.getElementById("oriun_orga_select")
        let organizacion = select_edad.options[select_edad.selectedIndex].value
        let select_ = document.getElementById("oriundo_select_departamento")
        let departamento = select_.options[select_.selectedIndex].value

        
        url = url+"/"+filtro_id+"/"+organizacion+"/"+departamento+"/"+filtro_info

    }else if (filtro_id=="opc_no"){
        let select_edad = document.getElementById("oriun_orga_select")
        let organizacion = select_edad.options[select_edad.selectedIndex].value
        let select_ = document.getElementById("oriundo_select_departamento")
        let departamento = select_.options[select_.selectedIndex].value
        url = url+"/"+filtro_id+"/"+organizacion+"/"+departamento+"/"+filtro_info

    }else if (filtro_id=="elecvsnacimiento_name"){
        url = url+"/"+filtro_id+"/unk/unk/"+filtro_info
    }else if (filtro_id=="2019priv" ){
        console.log("2019_priv: --> filtro_info : ",filtro_info)
        let bool_presento=""
        let orden_=""
        let bool_presento_inputs = document.getElementsByName("2019_presente")
        let orden_inputs = document.getElementsByName("2019_ingre")
        for(let i = 0 ; i < bool_presento_inputs.length; i++){
            if(bool_presento_inputs[i].checked == true)
                bool_presento = bool_presento_inputs[i].value  
        }
        for(let i = 0 ; i < orden_inputs.length; i++){
            if(orden_inputs[i].checked == true)
            orden_ = orden_inputs[i].value  
        }

        url = url+"/"+filtro_id+"/"+"unk"+"/"+bool_presento+"/"+orden_

    }else if (filtro_id=="2018priv" ){
        console.log("2018_priv: --> filtro_info : ",filtro_info)
        let bool_presento=""
        let orden_=""
        let bool_presento_inputs = document.getElementsByName("2018_presente")
        let orden_inputs = document.getElementsByName("2018_ingre")
        for(let i = 0 ; i < bool_presento_inputs.length; i++){
            if(bool_presento_inputs[i].checked == true)
                bool_presento = bool_presento_inputs[i].value  
        }
        for(let i = 0 ; i < orden_inputs.length; i++){
            if(orden_inputs[i].checked == true)
            orden_ = orden_inputs[i].value  
        }

        url = url+"/"+filtro_id+"/"+"unk"+"/"+bool_presento+"/"+orden_

    }else if (filtro_id=="2017priv" ){
        console.log("2018_priv: --> filtro_info : ",filtro_info)
        let bool_presento=""
        let orden_=""
        let bool_presento_inputs = document.getElementsByName("2017_presente")
        let orden_inputs = document.getElementsByName("2017_ingre")
        for(let i = 0 ; i < bool_presento_inputs.length; i++){
            if(bool_presento_inputs[i].checked == true)
                bool_presento = bool_presento_inputs[i].value  
        }
        for(let i = 0 ; i < orden_inputs.length; i++){
            if(orden_inputs[i].checked == true)
            orden_ = orden_inputs[i].value  
        }

        url = url+"/"+filtro_id+"/"+"unk"+"/"+bool_presento+"/"+orden_

    }
    else if(filtro_id=="publico_orden"){
        //let select_edad = document.getElementById("select_public")
        //let organizacion = select_edad.options[select_edad.selectedIndex].value
        url = url+"/"+filtro_id+"/unk/unk/"+filtro_info

    }
    
    console.log (url)
    //return ""
    window.location = url 

    getUrl_orga()  

}
function quitar_todas_selecciones(id_){
    let lista_inputs_all = document.getElementsByTagName("input")
    for (let i = 0 ; i<lista_inputs_all.length; i++){
        if (lista_inputs_all[i].id == id_){
            continue
        }
        lista_inputs_all[i].checked = false
    }
    let litsta_selects = document.getElementsByTagName("select")
    for (let i = 0 ; i<litsta_selects.length; i++){
        if (litsta_selects[i].id == id_){
            continue
        }
        litsta_selects[i].selectedIndex = 0
    }
    filtro_id= ""
    filtro_info=""
}


//list.length = 0
//EDAD
function set_valor(element){



    console.log("element.id : ",element.id)
    quitar_todas_selecciones(element.id)


    filtro_id = element.name
    filtro_info = element.value


    if (element.name == "opc_educacion"){
        inputs_educacion = document.getElementsByName("opc_educacion")
    for (let i = 0 ; i < inputs_educacion.length; i++){
        if(inputs_educacion[i].checked == true){
            if(i ==0 || i==1){
                filtro_id = "primaria"
                filtro_info = inputs_educacion[i].value
            }
            else if(i ==2 || i==3){
                filtro_id = "secundaria"
                filtro_info = inputs_educacion[i].value
            }
            else if(i ==4 || i==5){
                filtro_id = "tecnicos" 
                filtro_info = inputs_educacion[i].value 
            }
            else if(i ==6 || i==7){
                filtro_id = "nouni"
                filtro_info = inputs_educacion[i].value  
            }
            else if(i ==8 || i==9){
                filtro_id = "uni"
                filtro_info = inputs_educacion[i].value  
            }

            else if(i ==10 || i==11){
                filtro_id = "postgrado"
                filtro_info = inputs_educacion[i].value  
            }
            else if(i ==12 || i==13){
                filtro_id = "maestrodoctor"
                filtro_info = inputs_educacion[i].value  
            }
        }
    }
    }
    else if (element.name == "opc_genero" || element.name =="genero_orden"){
        filtro_id = "genero"
    }


    else if(element.name =="2019_presente" || element.name =="2019_ingre"){
        filtro_id = "2019priv"
    }
    else if(element.name =="2018_presente" || element.name =="2018_ingre"){
        filtro_id = "2018priv"
    }    else if(element.name =="2017_presente" || element.name =="2017_ingre"){
        filtro_id = "2017priv"
    }

    if (element.id == "oriundo" && element.value == "NO"){
        select = document.getElementsByName("uwuselectoriundo")
        select[0].selectedIndex = 0
    }

    console.log("filtro_id: ",filtro_id)
    console.log("filtro_info: ",filtro_info)


}


