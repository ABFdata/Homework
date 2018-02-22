// var trace1 = {
//     labels: ["beer", "wine", "martini", "margarita",
//         "ice tea", "rum & coke", "mai tai", "gin & tonic"],
//     values: [22.7, 17.1, 9.9, 8.7, 7.2, 6.1, 6.0, 4.6],
//     type: 'pie'
// };

// var data = [trace1];

// var layout = {
//     title: "Top 10 Samples",
// };

// Plotly.newPlot("plot", data, layout);

// var url = "/samples/<sample>";

// function buildPieChart() {
//     Plotly.d3.json(url, function (error, response) {

//         console.log(response);
//         var trace1 = {
//             type: "pie",
//             //mode: ""
//             name: "Top 10 Samples",
//             labels: response.map(url => data.otu_ids),
//             values: response.map(url => data.sample_values),


//         };

//         Plotly.newPlot("plot", data, layout);
//     });
// }

// buildPieChart();
