$('document').ready(function() {
	console.log("document ready");
	getOdds();
function getOdds() {
	console.log("in get odds");
	/*
	let apiKey = "58fc9cea78d41ee3c822d4acfb19d27f";

	let host = "https://api.the-odds-api.com"
	let region = "shared"; // alternative choice "live_uk"
	let sport = "sports"; // can be changed
	let query = {
		"region" : region,
		"sport": sport
	};
	let s = document.createElement("script");
	s.src = "jsonp_api_call?x=" + JSON.stringify(query);
	document.body.appendChild(s);
	*/
	let url = "https://www.google.com/";
	let method = "GET";
	let request = createCORSRequest(method, url);
	//request.setRequestHeader('x-api-key': '58fc9cea78d41ee3c822d4acfb19d27f');
	request.onload = function() {
		var responseText = request.responseText;
		console.log(responseText);
		// process the response.
	};

	if (!request) {
		alert('CORS not supported');
		return;
	}

	request.onerror = function() {
		console.log('There was an error!');
	};
	request.withCredentials = true;
	request.send();
}

function apiCall(info) {
	console.log(info);
}

function createCORSRequest(method, url) {
  var request = new XMLHttpRequest();
  if ("withCredentials" in request) {
    // XHR for Chrome/Firefox/Opera/Safari.
    request.open(method, url, true);
  } else if (typeof XDomainRequest != "undefined") {
    // XDomainRequest for IE.
    request = new XDomainRequest();
    request.open(method, url);
  } else {
    // CORS not supported.
    request = null;
  }
  return request;
}
});
