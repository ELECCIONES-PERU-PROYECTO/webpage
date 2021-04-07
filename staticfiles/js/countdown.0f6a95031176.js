let countDownDate = new Date("Apr 11, 2021").getTime();

// Update the count down every 1 second
let x = setInterval(function() {

  // Get today's date and time
  let now = new Date().getTime();
    
  // Find the distance between now and the count down date
  let distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  let days = Math.floor(distance / (1000 * 60 * 60 * 24));
  let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    
  // Output the result in an element with id="demo"
  document.getElementById("countdown").innerHTML = (days != 0 ? days + (days == 1 ? " día" :  " días") + (hours != 0 ?  " y " + hours + (hours == 1 ? " hora" :  " horas") : "") : hours + (hours == 1 ? " hora" :  " horas"))
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "¡Es el día de las elecciones!";
    document.getElementById("countdown-title").style.display = "none"
    document.getElementById("countdown-footer").style.display = "none"
  }
}, 1000);