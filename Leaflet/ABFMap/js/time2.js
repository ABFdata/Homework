// Create map object 
var map = L.map("map", {
    center: [37.09, -95.71],
    zoom: 4,
    timeDimension: true,
    timeDimensionOptions: {
        timeInterval: "2018-03-07/2018-03-08",
        period: "PT1H"
    },
    timeDimensionControl: true,

});

// add api key to variable 
var apiKey = "access_token=pk.eyJ1IjoiYWJmZGF0YSIsImEiOiJjamU2aHlrZTgwMGdxMzNxa3R3OG5wZmNkIn0._No3joCSQ0ZhN2KE30LC8w";

// Grayscale map
var grayscale = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?" + apiKey).addTo(map);

var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"


// load geoJson data
// Grabbing our GeoJSON data..
d3.json(link, function(data) {
    // Creating a GeoJSON layer with the retrieved data
    L.geoJson(data).addTo(map);
  });

// var wmsLayer = L.tileLayer.wms(link, {
//     layers: grayscale,
//     format: 'image/png',
//     transparent: true,

// });



// // Create and add a TimeDimension Layer to the Map
// var tdWmsLayer = L.timeDimension.layer.wms(wmsLayer);
// tdWmsLayer.addTo(map);


