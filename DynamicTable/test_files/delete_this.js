function handleSearchButtonClick() {
    // Format search field by trimming value whitespace and changing to lowercase string
    var filterDatetime = $datetimeInput.value;
    
    // set filtered UFO Data to an array of all data that match the datetime filter
    filteredUFOData = dataSet.filter(function(UFOdata) {
        var UFOdatetime = UFOdata.datetime;
    
        // if true, add datetime to filtered UFO Data
        return UFOdatetime === filterDatetime;
    });
renderTable();