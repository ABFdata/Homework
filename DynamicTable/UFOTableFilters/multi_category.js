// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#date");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredUFOData to dataSet initially - dataset is json object in data.js
var filteredUFOData = dataSet;

// renderTable renders the filteredUFOData to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < filteredUFOData.length; i++) {
    // Get get the current UFOData object and its fields
    var UFOdata = filteredUFOData[i];
    var fields = Object.keys(UFOdata);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the UFOData object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = UFOdata[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDatetime = $datetimeInput.value;
  var filterCity = $cityInput.value.trim().toLowerCase(); 
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();

  // Set filteredUFOData to an array of all addresses whose "state" matches the filter
  filteredUFOData = dataSet.filter(function(UFOdata) {
    var UFOdatetime = UFOdata.datetime;
    var UFOcity = UFOdata.city.substring(0, filterCity.length).toLowerCase();
    var UFOstate = UFOdata.state.substring(0, filterState.length).toLowerCase();
    var UFOcountry = UFOdata.country.substring(0, filterCountry.length).toLowerCase();
    var UFOshape = UFOdata.shape.substring(0, filterShape.length).toLowerCase();
    if (UFOdatetime === filterDatetime && UFOcity === filterCity && UFOstate === filterState
    && UFOcountry === filterCountry && UFOshape === filterShape) {
        return true;
    }
    return false;

    // If true, add the address to the filteredUFOData, otherwise don't add it to filteredUFOData
    //return UFOdatetime === filterDatetime;
    //return UFOcity === filterCity;
    //return UFOstate === filterState;
  });
  renderTable();
}

// Render the table for the first time on page load
renderTable();