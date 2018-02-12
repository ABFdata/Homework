// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $datetimeInput = document.querySelector("#datetime");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);

// Set filteredDate to dateData initially // data is the data.js file
var filteredUFOdata = dataSet;

// renderTable renders the filteredDate to tbody
function renderTable() {
    $tbody.innerHTML = "";
    for (var i = 0; i < filteredUFOdata.length; i++) {
        // Get the current date object and its fields
        var UFOdata = filteredUFOdata[i];
        var fields = Object.keys(UFOdata);
        // Create a new row in the tbody, set the index to be the i + startingIndex
        var $row = $tbody.insertRow(i);
        for (var j= 0; j < fields.length; j++) {
            // For every field in the UFOdata object, create a new cell and set its inner text to be the current value at the current address field
            var field = fields[j];
            var $cell = $row.insertCell(j);
            $cell.innerText = UFOdata[field];
        }
    }
}

function handleSearchButtonClick() {
    // Format the user's search by removing leading and trailing whitespace, lowercase the string
    var filterDatetime = $datetimeInput.value;
    
  
    // Set filteredDate to an array of all dates whose "datetime" matches the filter
    filteredUFOdata = dataSet.filter(function(UFOdata) {
       var UFOdatetime = UFOdata.datetime;
    //    if (dateState === filterState && dateDate === filterDate) {
    //        return true;

    //    }
    //    return false;

       // If true, add the date to the filteredDate, otherwise don't add it to filteredDate
        return UFOdatetime === filterDatetime;
    });
    renderTable();
  }
  
  // Render the table for the first time on page load
  renderTable();
  