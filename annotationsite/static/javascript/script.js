//Hi. I didn't touch this file at all for Milestone 3. A lot of the functionality here is incompatible with Django and I can't really access Django context values here at all, so everything is still static
//That being said none of this is part of the list, create, and edit views anyways so it shouldn't affect it at all. Even if it's still hardcodeded HTML

//side menu toggle
document.getElementById("menuToggle").addEventListener("click", function () {
  if (document.getElementById("sidenav").style.display == "none") {
    document.getElementById("sidenav").style.removeProperty("display");
  } else {
    document.getElementById("sidenav").style.display = "none";
  }
});

//annotation menu toggle
document.getElementById("dropdown").addEventListener("click", function () {
  if (document.getElementById("dropdownMenu").style.display == "block") {
    document.getElementById("dropdownMenu").style.display = "none";
  } else {
    document.getElementById("dropdownMenu").style.display = "block";
  }
});

//change div to update contents to Live Annotations
function getAnnotation() {
  let xhr = new XMLHttpRequest();
  xhr.onload = function () {
    data = JSON.parse(this.responseText);
    //clear the contents of panel
    document.getElementById("panel").innerHTML = "<h4><b>All Annotations:</b></h4>";
    //append things to panel contents
    for (const key in data) {
      document.getElementById("panel").innerHTML += `<p><b>${data[key].fields.timestamp}</b></p>`;
      document.getElementById("panel").innerHTML += `<p>${data[key].fields.annotation}</p>`;
      document.getElementById("panel").innerHTML += `<p><b>Source: </b><a href="${data[key].fields.citation}">${data[key].fields.citation}</a></p>`;
    }
  };
  xhr.open("GET", "getAnnotation");
  xhr.send();
}

//change div to update contents to chat replay
function getChat() {
  let xhr = new XMLHttpRequest();
  xhr.onload = function () {
    data = JSON.parse(this.responseText);
    document.getElementById("panel").innerHTML = "<h4><b>Chat Replay:</b></h4>";
    //append things to panel contents
    for (const key in data) {
      document.getElementById("panel").innerHTML += `<p>${data[key].fields.comment}</p>`;
    }
  };
  xhr.open("GET", "getChat");
  xhr.send();
}

// Live search
function liveSearch() {
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
  var formData = new FormData();
  annotationSearch = document.getElementById("annotationSearch").value;

  let xhr = new XMLHttpRequest();
  xhr.onload = function () {
    console.log(this.responseText);
    //clear the contents of panel
    document.getElementById("panel").innerHTML = "";
    data = JSON.parse(this.responseText);
    //append things to panel contents
    for (const key in data) {
      document.getElementById("panel").innerHTML += `<p><b>${data[key].fields.timestamp}</b></p>`;
      document.getElementById("panel").innerHTML += `<p>${data[key].fields.annotation}</p>`;
      document.getElementById("panel").innerHTML += `<p><b>Source: </b><a href="${data[key].fields.citation}">${data[key].fields.citation}</a></p>`;
    }
  };
  xhr.open("POST", "liveSearch");
  xhr.setRequestHeader("X-CSRFToken", csrftoken);
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  formData.append("annotationSearch", annotationSearch);
  xhr.send(formData);
}
