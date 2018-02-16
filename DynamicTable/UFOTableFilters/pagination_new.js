// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $loadMoreBtn = document.querySelector("#load-btn")
var $datetimeInput = document.querySelector("#datetime");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");


// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
$loadMoreBtn.addEventListener("click", handleButtonClick);

// Set sliced data.js to ufoSubset variable initially
var ufoSubset = dataSet.slice(0, 50);

//Initially define filterData with no value, this will be used later in the code
var filteredUFOData;

// Set a resultsPerPage variable
var resultsPerPage = 50;

//handleButtonClick Function for loading more data
function handleButtonClick(){
  if(filteredUFOData){
    resultsPerPage += filteredUFOData.length;
  } else {
    resultsPerPage +=50;
  }
  var startingIndex = resultsPerPage - 50 + 1;
  var nextData = dataSet.slice(startingIndex, resultsPerPage);
  ufoSubset = ufoSubset.concat(nextData);

  renderTable();
}

// renderTable renders the filteredUFOData to the tbody
function renderTable(filteredUFOData) {
  if(filteredUFOData){
    $tbody.innerHTML = "";
    for (var i=0; i < filteredUFOData.length; i++) {
      // Get current filteredUFOData object and fields
      var UFOdata = filteredUFOData[i];
      var fields = Object.keys(UFOdata);
      // Create a new row in the tbody, set index to be i + startingIndex
      var $row = $tbody.insertRow(i);
      for (var j = 0; j < fields.length; j++){
        // For every field in the data object, create a new cell and set its inner text to be the current value at the current data field
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = UFOdata[field];
      }
    }
  } else {
    $tbody.innerHTML = "";
    for (var i = 0; i < ufoSubset.length; i++){
      // Get the current filteredUFOData object and fields
      var UFOdata = ufoSubset[i];
      var fields = Object.keys(UFOdata);
      // Create a new row in the tobody set the index to be i + startingIndex
      var $row = $tbody.insertRow(i);
      for (var j = 0; j <fields.lenght; j++) {
        // For every field in the data object, create a new cell and set inner text to be the current value at the current data field
        var field = fields[j];
        var $cell = $row.insertCell(j);
        $cell.innerText = UFOdata[field];
      }
    }
  }
}

function handleSearchButtonClick() {
  // Format user's search by removing leading & trailing whitespace, lowercase the string
  var filterDatetime = $datetimeInput.value.trim();
  var filterCity = $cityInput.value.trim().toLowerCase(); 
  var filterState = $stateInput.value.trim().toLowerCase();
  var filterCountry = $countryInput.value.trim().toLowerCase();
  var filterShape = $shapeInput.value.trim().toLowerCase();


  // Set filtered "Data" to an array of all UFO subset data whose "data" matches the filter
  filteredUFOData = ufoSubset.filter(function(UFOdata) {
    var UFOdateTime = UFOdata.datetime.substring(0, filterDatetime.length).toLowerCase();
    var UFOcity =  UFOdata.city.substring(0, filterCity.length).toLowerCase();
    var UFOstate = UFOdata.state.substring(0, filterState.length).toLowerCase();
    var UFOcountry = UFOdata.country.substring(0, filterCountry.length).toLowerCase();
    var UFOshape = UFOdata.shape.substring(0, filterShape.length).toLowerCase(); 


    if (UFOdateTime == filterDatetime && UFOcity == filterCity && UFOstate == filterState && UFOcountry == filterCountry && UFOshape == filterShape) {
      return true;
    }
    return false;
  });
  renderTable(filteredUFOData);
}

// Render the table for the first time on page load
renderTable();
