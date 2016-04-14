google.charts.load('current', {'packages':['geochart']});
google.charts.setOnLoadCallback(drawRegionsMap);

var geochart = [];

var data = {}
var options = {
	width: 1300,
	height: 900, 
	region: "US", 
	resolution: "provinces",
	colorAxis: {
		minValue: -1,
		maxValue: 1,
		colors: ['#D91E18','white', '#4183D7']
	}
};
var raw = {
	'State': 'Rating',
	'US-AK': 0,
	'US-AL': 0,
	'US-AR': 0,
	'US-AZ': 0,
	'US-CA': 0,
	'US-CO': 0,
	'US-CT': 0,
	'US-DE': 0,
	'US-FL': 0,
	'US-GA': 0,
	'US-HI': 0,
	'US-IA': 0,
	'US-ID': 0,
	'US-IL': 0,
	'US-IN': 0,
	'US-KS': 0,
	'US-KY': 0,
	'US-LA': 0,
	'US-MA': 0,
	'US-MD': 0,
	'US-ME': 0,
	'US-MI': 0,
	'US-MN': 0,
	'US-MO': 0,
	'US-MS': 0,
	'US-MT': 0,
	'US-NC': 0,
	'US-ND': 0,
	'US-NE': 0,
	'US-NH': 0,
	'US-NJ': 0,
	'US-NM': 0,
	'US-NV': 0,
	'US-NY': 0,
	'US-OH': 0,
	'US-OK': 0,
	'US-OR': 0,
	'US-PA': 0,
	'US-RI': 0,
	'US-SC': 0,
	'US-SD': 0,
	'US-TN': 0,
	'US-TX': 0,
	'US-UT': 0,
	'US-VA': 0,
	'US-VT': 0,
	'US-WA': 0,
	'US-WI': 0,
	'US-WV': 0,
	'US-WY': 0
};

var manifest = {
	'US-AK': {total: 0.0, pol: 0.0},
	'US-AL': {total: 0.0, pol: 0.0},
	'US-AR': {total: 0.0, pol: 0.0},
	'US-AZ': {total: 0.0, pol: 0.0},
	'US-CA': {total: 0.0, pol: 0.0},
	'US-CO': {total: 0.0, pol: 0.0},
	'US-CT': {total: 0.0, pol: 0.0},
	'US-DE': {total: 0.0, pol: 0.0},
	'US-FL': {total: 0.0, pol: 0.0},
	'US-GA': {total: 0.0, pol: 0.0},
	'US-HI': {total: 0.0, pol: 0.0},
	'US-IA': {total: 0.0, pol: 0.0},
	'US-ID': {total: 0.0, pol: 0.0},
	'US-IL': {total: 0.0, pol: 0.0},
	'US-IN': {total: 0.0, pol: 0.0},
	'US-KS': {total: 0.0, pol: 0.0},
	'US-KY': {total: 0.0, pol: 0.0},
	'US-LA': {total: 0.0, pol: 0.0},
	'US-MA': {total: 0.0, pol: 0.0},
	'US-MD': {total: 0.0, pol: 0.0},
	'US-ME': {total: 0.0, pol: 0.0},
	'US-MI': {total: 0.0, pol: 0.0},
	'US-MN': {total: 0.0, pol: 0.0},
	'US-MO': {total: 0.0, pol: 0.0},
	'US-MS': {total: 0.0, pol: 0.0},
	'US-MT': {total: 0.0, pol: 0.0},
	'US-NC': {total: 0.0, pol: 0.0},
	'US-ND': {total: 0.0, pol: 0.0},
	'US-NE': {total: 0.0, pol: 0.0},
	'US-NH': {total: 0.0, pol: 0.0},
	'US-NJ': {total: 0.0, pol: 0.0},
	'US-NM': {total: 0.0, pol: 0.0},
	'US-NV': {total: 0.0, pol: 0.0},
	'US-NY': {total: 0.0, pol: 0.0},
	'US-OH': {total: 0.0, pol: 0.0},
	'US-OK': {total: 0.0, pol: 0.0},
	'US-OR': {total: 0.0, pol: 0.0},
	'US-PA': {total: 0.0, pol: 0.0},
	'US-RI': {total: 0.0, pol: 0.0},
	'US-SC': {total: 0.0, pol: 0.0},
	'US-SD': {total: 0.0, pol: 0.0},
	'US-TN': {total: 0.0, pol: 0.0},
	'US-TX': {total: 0.0, pol: 0.0},
	'US-UT': {total: 0.0, pol: 0.0},
	'US-VA': {total: 0.0, pol: 0.0},
	'US-VT': {total: 0.0, pol: 0.0},
	'US-WA': {total: 0.0, pol: 0.0},
	'US-WI': {total: 0.0, pol: 0.0},
	'US-WV': {total: 0.0, pol: 0.0},
	'US-WY': {total: 0.0, pol: 0.0}
};

var output = []

// FUnctions
function rawToArray(raw) {
	output = []
	for (var type in raw) {
		output.push([type, raw[type]])
	}
	return output;
}

function updateMap(state, value) {
	state = 'US-' + state;
	raw[state] = value;
	output = rawToArray(raw);
	data = google.visualization.arrayToDataTable(output);
	geochart.draw(data, options);
}

function drawRegionsMap() {

	output = rawToArray(raw);
	data = google.visualization.arrayToDataTable(output);
	console.log(data);

	geochart = new google.visualization.GeoChart(document.getElementById('regions_div'));

	geochart.draw(data, options);
	// SocketIO Events
	var socket = io();

	socket.on('tweet', function(msg) {
		var val = 0.0;
		var state = 'US-' + msg.state;
		manifest[state]['total'] += 1;
		manifest[state]['pol'] += parseInt(msg.pol);
		console.log(manifest[state]['pol'], manifest[state]['total']);
		val = manifest[state]['pol'] / manifest[state]['total'];
		updateMap(state, val);
	});
}
