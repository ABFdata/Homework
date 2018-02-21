/* data route */

// var url = "/names";

// function optionChanged() {
//     // data route
    
//     Plotly.d3.json(url, function(error, response) {

//         console.log(response);

//         // points to the select id tag selDataset
//         var selectTarget = document.getElementById("selDataset");
        
//         var option = document.createElement("option");
//         option.text = sample_names_list;
//         $getplotlytarget.addEventListener(option);
    
//         Plotly.newPlot("selDataset", option);


//         //document.createElement

//         //append


//     });

// }

// optionChanged();



// var select = document.getElementById("selectNumber"); 
// var options = ["1", "2", "3", "4", "5"]; 

// for(var i = 0; i < options.length; i++) {
//     var opt = options[i];
//     var el = document.createElement("option");
//     el.textContent = opt;
//     el.value = opt;
//     select.appendChild(el);
// }​

// Pie chart 
// Create pie chart that uses data from /samples/<sample> and /otu to display
// the top 10 samples

var trace1 = {
    labels: ["beer", "wine", "martini", "margarita",
        "ice tea", "rum & coke", "mai tai", "gin & tonic"],
    values: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
    type: 'pie'
};

var data = [trace1];

var layout = {
    title: "Top 10 Samples",
};

Plotly.newPlot("plot", data, layout);









