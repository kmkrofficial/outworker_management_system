// function openNav() {
//     document.getElementById("mySidenav").style.width = "250px";
//     document.getElementById("main").style.marginLeft = "250px";
//     document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
//   }
  
//   function closeNav() {
//     document.getElementById("mySidenav").style.width = "0";
//     document.getElementById("main").style.marginLeft= "0";
//     document.body.style.backgroundColor = "white";
//   }

var x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.watchPosition(showPosition);
  } else {
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}
function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude +
  "<br>Longitude: " + position.coords.longitude;
}


function showPosition(position) {
    var latlon = position.coords.latitude + "," + position.coords.longitude;
  
    var img_url = "https://maps.googleapis.com/maps/api/staticmap?center="
    +latlon+"&zoom=14&size=400x300&sensor=false&key=AIzaSyBKMTaY4FQefZBrHSb2J7THLsEL1-G7K9I";
  
    document.getElementById("mapholder").innerHTML = "<img src='"+img_url+"'>";
  }

function showError(error) {
    switch(error.code) {
      case error.PERMISSION_DENIED:
        x.innerHTML = "User denied the request for Geolocation."
        break;
      case error.POSITION_UNAVAILABLE:
        x.innerHTML = "Location information is unavailable."
        break;
      case error.TIMEOUT:
        x.innerHTML = "The request to get user location timed out."
        break;
      case error.UNKNOWN_ERROR:
        x.innerHTML = "An unknown error occurred."
        break;
    }
  }


// search

$(document).ready(function() {

    const $valueSpan = $('.valueSpan');
    const $value = $('#slider11');
    $valueSpan.html($value.val());
    $value.on('input change', () => {
  
      $valueSpan.html($value.val());
    });
  });


// div loop

var toAdd = document.createDocumentFragment();
for(var i=0; i < 11; i++){
   var newDiv = document.createElement('div');
   newDiv.id = 'r'+i;
   newDiv.className = 'ansbox';
   toAdd.appendChild(newDiv);
}

document.appendChild(toAdd);