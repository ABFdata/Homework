// Create map object 
var map = L.map("map", {
    center: [37.09, -95.71],
    zoom: 2

});

// Add tile layer
L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/outdoors-v10/tiles/256/{z}/{x}/{y}?" +
    "access_token=pk.eyJ1IjoiYWJmZGF0YSIsImEiOiJjamU2aHlrZTgwMGdxMzNxa3R3OG5wZmNkIn0._No3joCSQ0ZhN2KE30LC8w").addTo(map);

// Store our API endpoint inside queryUrl
// var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson"
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"


 function styleInfo(feature){
     return{
     fillOpacity: 0.75,
     color: getColor(feature.properties.mag),
     radius: getRadius(feature.properties.mag),
     stroke: true,
     border: true,
     weight: 0.5
    };
 };

 function getColor(magnitude){
     switch(true) {
         case magnitude > 5:
         return "#FF0000"; // red
         case magnitude > 4:
         return "#FFA500"; // orange
         case magnitude > 3:
         return "#FFFF00"; // yellow
         case magnitude > 2:
         return "#FFDAB9"; // peachpuff
         case magnitude > 1:
         return "#9ACD32"; // yellowgreen
         default:
         return "#FFE4C4"; // bisque
     }
 };

 //  #FF0000 red
 //  #FF4500 orangered
 //  #FFA500 orange  
 //  #FFFF00 yellow 
 //  #FFDAB9 peachpuff
 //  #FFE4C4 bisque  
 //  #FFFFE0 lightyellow  
 //  #9ACD32 yellowgreen

 // function get Radius

 function getRadius(magnitude){
    switch(true) {
        case magnitude > 5:
        return 20;
        case magnitude > 4:
        return 15;
        case magnitude > 3:
        return 10;
        case magnitude > 2:
        return 7;
        case magnitude > 1:
        return 5;
        default:
        return 3;
    }
};

//create a function: populateInfo to add data
function populateInfo(feature, layer) {
    layer.bindPopup("<h1 class='infoHeader'>Weekly Earthquake Data</h1> \
    <p class='description'>" + "Location: " + feature.properties.place + "</p>\
    <p class='description'>" + "Magnitude: " + feature.properties.mag + "</p>");
        
};

// Here we add a GeoJSON layer to the map once the file is loaded.
d3.json(link, function(data){
    L.geoJson(data, {
        // We turn each feature into a circleMarker on the map.
        pointToLayer: function(feature, latlng) {
          return L.circleMarker(latlng);
        },
        // We set the style for each circleMarker using our styleInfo function.
        style: styleInfo,
        // We create a popup for each marker to display the magnitude and location of the earthquake after the marker has been created and styled
        onEachFeature: populateInfo,
        
        
      }).addTo(map);

});

    





