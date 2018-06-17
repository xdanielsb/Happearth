'use strict'
/**
 * @file custom.js
 * @author Daniel Santos <dfsantosbu@unal.edu.co>
 * @version 1
 */

 function displayOptions(){
  if(document.getElementById("sub-progress").style.display == "inline"){
    document.getElementById("sub-progress").style.display = "none";
  }else{
    document.getElementById("sub-progress").style.display = "inline";
  }
 }

 function displayRightMenu(){
  document.getElementById("sidenav-right").style.width = "260px";
  document.getElementById("bell1").style.display = "none";
 }

 function hideRightMenu(){
  document.getElementById("sidenav-right").style.width = "0px";
  document.getElementById("bell1").style.display = "inline";
 }

 function displayOptionsWallet(){
  if(document.getElementById("sub-wallet").style.display == "block"){
    document.getElementById("sub-wallet").style.display = "none";
    // document.getElementById("trade").style.display = "block";
    // document.getElementById("options-wallet").style.display = "block";
  }else{
    document.getElementById("sub-wallet").style.display = "block";
    // document.getElementById("trade").style.display = "none";
    // document.getElementById("options-wallet").style.display = "none";
  }

 }

 function clickBoiler(){
  // alert("hello")
  if(document.getElementById("opt_two_actions").style.display == "none"){
    document.getElementById("opt_two_actions").style.display = "block";
    document.getElementById("dmodes").style.display = "block";
    document.getElementById("opt_one_actions").style.display = "none";
    document.getElementById("community-goal").style.display = "none";
    document.getElementById("doted").style.display = "none";

  }else{
    document.getElementById("opt_two_actions").style.display = "none";
    document.getElementById("dmodes").style.display = "none";
    document.getElementById("opt_one_actions").style.display = "block";
    document.getElementById("community-goal").style.display = "block";
    document.getElementById("doted").style.display = "block";
  }
 }
function changeImage(){
  var rates = document.getElementsByName('temperature_scale');
  var rate_value;
  for(var i = 0; i < rates.length; i++){
      if(rates[i].checked){
        document.getElementById("series-image").src="img/time"+rates[i].value+".png";
      }
  }
 }
$(document).ready(function(){
  $(".inside").click(hideRightMenu);
});



