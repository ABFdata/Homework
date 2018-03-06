// Create map object 
var map = L.map("map", {
    center: [37.09, -95.71],
    zoom: 4

});

// Add tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1IjoiYWJmZGF0YSIsImEiOiJjamU2aHlrZTgwMGdxMzNxa3R3OG5wZmNkIn0._No3joCSQ0ZhN2KE30LC8w").addTo(map);

// earthquakes all week data
var plates_link = "../json/plates2.json"

// Here we add a GeoJSON layer to the map once the file is loaded.
// Grabbing our GeoJSON data..
d3.json(plates_link, function(data) {
    // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data).addTo(map);
  });
