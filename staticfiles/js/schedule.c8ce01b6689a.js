function onchange_horario(element) {
    let selected_number = element.options[element.selectedIndex].value
    let json_horarios = {
      10: '7:00 a. m. a 9:00 a. m.',
      1: '9:00 a. m. a 10:00 a. m.',
      2: '10:00 a. m. a 11:00 a. m.',
      3: '11:00 a. m. a 12:00 p. m.',
      4: '12:00 p. m. a 1:00 p. m.',
      5: '1:00 p. m. a 2:00 p. m.',
      6: '2:00 p. m. a 3:00 p. m.',
      7: '3:00 p. m. a 4:00 p. m.',
      8: '4:00 p. m. a 5:00 p. m.',
      9: '5:00 p. m. a 6:00 p. m.',
      0: '6:00 p. m. a 7:00 p. m.',
    }
  
    let schedule = document.getElementById('schedule')
    schedule.innerHTML = json_horarios[selected_number]
  }
