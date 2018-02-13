// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $loadMoreBtn = document.querySelector("#load-btn")
var $datetimeInput = document.querySelector("#date");
var $cityInput = document.querySelector("#city");
var $stateInput = document.querySelector("#state");
var $countryInput = document.querySelector("#country");
var $shapeInput = document.querySelector("#shape");
var $searchBtn = document.querySelector("#search");


// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Add event listener to the button, call handleButtonClick when clicked
$loadMoreBtn.addEventListener("click", handleButtonClick);

// Set filteredUFOData to dataSet initially - dataset is json object in data.js
var filteredUFOData = dataSet;

// Set a startingIndex and resultsPerPage variable
var startingIndex = 0;
var resultsPerPage = 50;

function renderTableSection() {
    // Set the value of endingIndex to startingIndex + resultsPerPage
    var endingIndex = startingIndex + resultsPerPage;
    // Get a section of the filteredUFOData array to render
    var UFOSubset = filteredUFOData.slice(startingIndex, endingIndex);
    for (var i = 0; i < UFOSubset.length; i++) {
      // Get the current address object and its fields
      var UFOdata = UFOSubset[i];
      var fields = Object.keys(UFOdata);
      // Create a new row in the tbody, set the index to be i + startingIndex
      var $row = $tbody.insertRow(i + startingIndex);
      for (var j = 0; j < fields.length; j++) {
        // For every field in the address object, create a new cell and set its inner text to be the current value at the current address's field
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
  
    });
    renderTableSection();
  }

function handleButtonClick(){
    //Increase startingIndex by resultsPerPage, render next section of the table
    startingIndex += resultsPerPage;
    renderTableSection();
    // Check to see if there are any more results to render
    if (startingIndex + resultsPerPage >= filteredUFOData.length) {
        $loadMoreBtn.classList.add("disabled");
        $loadMoreBtn.innerText = "All UFO Data Loaded";
        $loadMoreBtn.removeEventListener("click", handleButtonClick);
    }
}

// Render the table for the first time on page load
renderTableSection();
