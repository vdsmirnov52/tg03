/**	file: static/js/document_ready.js
*/

function	set_shadow (shstat) {	$.ajax({data: 'shstat='+ shstat +'&' +$('form').serialize()});	}

$(document).ready(function () {
	$.ajaxSetup({ url: "/ajax", type: "post", error: onAjaxError, success: onAjaxSuccess, timeout: 30000 });
	$('#panele').css({'height': -66 + document.documentElement.clientHeight +'px', 'width': '100%'});
	$('#my_body').css({'height': -70 + document.documentElement.clientHeight +'px', 'width': '100%', 'overflow': 'auto'});
//	start_ws();
/*
	mymap = L.map('map').setView([56.32354, 43.99121], 10);

var	rnic_nn = ' &copy; <a href="http://rnc52.ru/" title="РНИЦ Нижегородской области">RNIC 52</s>';
var	osmLayer = new L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
		maxZoom: 14,
		attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors |' + rnic_nn
	}).addTo(mymap);
var	yndx = new L.Yandex();
var	ytraffic = new L.Yandex("null", {traffic:true, opacity:0.8, overlay:true});

var	baseMaps = { 'L.Yandex': yndx, "OpenStreetMap": osmLayer },
	overlays = { };	//"Marker": marker};

var	layersControl = new L.Control.Layers(baseMaps, overlays),	// overlayMaps),
	popup = new L.Popup();

mymap.addControl(layersControl);
mymap.on('click', (e) => {
    popup.setLatLng(e.latlng);
    popup.setContent('Point ' +
      ' (' + e.latlng.lat.toFixed(6) +
      ', ' + e.latlng.lng.toFixed(6) + ')');
    mymap.openPopup(popup);
  })
*/
});
