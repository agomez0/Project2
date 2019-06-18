// create a map layer
var arena_layer;

d3.json("/venue_coords").then(function(response){
  // list for arena markers
  var arena_markers = [];
  for (var i=0; i < response.length; i++) {
    // coordinates for each arena
    var coords = [response[i].latitude, response[i].longitude];
    // push each marker to the list
    arena_markers.push(L.marker(coords, {
      draggable: false,
    }).bindPopup("<h4>" + response[i].venue + "</h4>"));
  }
  // add markers to the layer
  arena_layer = L.layerGroup(arena_markers);
})

// light map layer
var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

// outdoor map layer
var outdoors = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.outdoors",
  accessToken: API_KEY
});

// satellite map layer
var satellite = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href='https://www.openstreetmap.org/'>OpenStreetMap</a> contributors, <a href='https://creativecommons.org/licenses/by-sa/2.0/'>CC-BY-SA</a>, Imagery © <a href='https://www.mapbox.com/'>Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-satellite",
  accessToken: API_KEY
});


function read_route(route) {
 
  d3.json(route).then(function(data){
    var heat_array = [];
    
    for (var i = 0; i < data.length; i++) {
      // push all crime coordinates to the list
      heat_array.push(data[i]);
    }

    // add the crime coordinates to a heat layer
    var heat = L.heatLayer(heat_array, {
      radius: 20,
      blur: 35
    });

    // map formats
    var baseMaps = {
      Light: light,
      Outdoors: outdoors,
      Satellite: satellite
    };
    
    // map layers
    var overlayMaps = {
      Arenas: arena_layer,
      HeatMap: heat
    };
    
    // Create map object and set default layers
    var myMap = L.map("map", {
      center: [34.0469, -118.2468],
      zoom: 13,
      layers: [outdoors, heat, arena_layer]
    });
    
    // adding all layers to myMap
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);
  })
};

read_route("/crime_coords");