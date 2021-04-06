
function onchange_horario(element)
{
  console.log("holaa")
  let selected_number = element.options[element.selectedIndex].value
  let json_horarios = 
  {
    "special":"#modal-group-1",
    "1" :  "#modal-group-2",
    "2" :  "#modal-group-3",
    "3" :  "#modal-group-4",
    "4" :  "#modal-group-5",
    "5" :  "#modal-group-6",
    "6" :  "#modal-group-7",
    "7" :  "#modal-group-8",
    "8" :  "#modal-group-9",
    "9" :  "#modal-group-0",
    "0" :  "#modal-group-11"
  }

  let button_modal = document.getElementById("button_modal")
  console.log("json_horarios[selected_number]: ", json_horarios[selected_number])
  
  button_modal.hreh = json_horarios[selected_number];

}
