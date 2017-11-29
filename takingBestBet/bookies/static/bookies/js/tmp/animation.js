$('document').ready(function() {
getInfo();
function getInfo() {
$.getJSON("keys.json", function(json) {
    console.log(json); // this will show the info it in firebug console
});
/*
let apiKey = "58fc9cea78d41ee3c822d4acfb19d27f";

let host = "https://86qbtjzii8.execute-api.ap-southeast-2.amazonaws.com"
let region = "shared"; // alternative choice "live_uk"
let sport = "sports"; // can be changed

let request = new XMLHttpRequest();
let url = host + "/" + region + "/" + sport;
request.onreadystatechange = function() {
	if (this.readyState === 4 && this.status === 200) {
		let response = JSON.parse(this.responseText);
		console.log(response);
	}
}

request.open("GET", url, true);
request.send();
*/
console.log('hello world');
}
});
