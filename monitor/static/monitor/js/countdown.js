var countDownDate = new Date("Jun 26, 2018 19:00:00").getTime();

var x = setInterval(function() {
  var now = new Date().getTime();
  var distance = countDownDate - now;
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
  document.getElementById("countdown").innerHTML = days + "d " + hours + "h "+ minutes + "m " + seconds + "s ";
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "WE ARE OPEN SOURCE at : <a href='https://github.com/xdanielsb'> CHECK THE SOURCE CODE </a>";
  }
}, 1000);
