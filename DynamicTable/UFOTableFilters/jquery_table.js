$(document).ready(function() {
    $('#UFOData').DataTable();

} );
// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");

// Set filteredUFOData to init dataSet
var filteredUFOData = dataSet;

// Render filteredUFOData to tbody
function renderTable() {
    $tbody.innerHTML = "";
    for (var i = 0; i < filteredUFOData.length; i++) {

        // Get UFO Data object and its fields
        var UFOdata = filteredUFOData[i];
        var fields = Object.keys(UFOdata);

        // Create new row in tbody
        var $row = $tbody.insertRow(i);
        for (var j = 0; j < fields.length; j++) {

            // For every field in the UFOData object create a new cell at set its inner text to be the current value at the current address's field
            var field = fields[j];
            var $cell = $row.insertCell(j);
            $cell.innerText = UFOdata[field];
        }

    }

}

// render full dataSet first load
renderTable();
