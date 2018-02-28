// D3 Scatterplot Assignment

// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.

var svgWidth = 960;
var svgHeight = 500;

var margin = { top: 20, right: 40, bottom: 60, left: 50 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("body")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// read data
d3.csv("healthData.csv", function(err, healthData){
  // line generator
  d3.select("body").append("div").attr("class", "tooltip");

// Set the ranges with scaling functions
var xTimeScale = d3.scaleTime()
.range([0, width]);

var yLinearScale1 = d3.scaleLinear()
.range([height, 0]);

var yLinearScale2 = d3.scaleLinear()
.range([height, 0]);

// Create axis functions
var bottomAxis = d3.axisBottom(xTimeScale)
// Specify the number of tick marks (approximately).
.ticks(15);
var leftAxis = d3.axisLeft(yLinearScale1);
var rightAxis = d3.axisRight(yLinearScale2);

// Scale the domain
xTimeScale.domain(d3.extent(healthData, function(data) {
  return data.date;
}));
yLinearScale1.domain([d3.min(healthData, function(data) {
  return data.poorHealth;
}), d3.max(healthData, function(data) {
  return data.poorHealth;
})]);















// when the browser window is resized, responsify() is called
d3.select(window).on("resize", makeResponsive);

// When the browser loads, makeResponsive() is called.
makeResponsive();

// The code for the chart is wrapped inside a function that automatically resizes the chart
function makeResponsive() {
    // if the SVG area isn't empty when the browser loads, remove it and replace it with a resized version of the chart
    var svgArea = d3.select("body").select("svg");
    if (!svgArea.empty()) {
      svgArea.remove();
    }
  
    // SVG wrapper dimensions are determined by the current width and height of the browser window.
    var svgWidth = window.innerWidth;
    var svgHeight = window.innerHeight;
  
    var svg = d3
      .select(".chart")
      .append("svg")
      .attr("height", svgHeight)
      .attr("width", svgWidth);

// // read data
// d3.csv("healthData.csv", function(err, healthData){
//     // line generator
//     d3.select("body").append("div").attr("class", "tooltip");

var chart = svg.append("g").attr("transform", "translate(100,-300)");

    var toolTip = d3
        .tip()
        .attr("class", "tooltip")
        .offset([40, -60])
        .html(function(data){
            var numPoorHealth = +data.poorHealth;
            var nonHsGrads = data.lessThanHS;
            return "The percentage of people over 60 with " + numPoorHealth + 
            " and The percentage of people over 60 who are non high school grads "
            + nonHsGrads
        });

    chart.call(toolTip);

    chart
      .selectAll("circle")
      .data(healthData)
      .enter()
      .append("circle")
      .attr("cx", function(data, index) {
        return index * svgWidth / 20;
      })
      .attr("cy", function(data, index) {
        return 600 - +data.poorHealth * svgHeight / 80;
      })
      .attr("r", "5")
      .attr("fill", "red")
      // onclick event to display an alert message
      .on("click", function(data, index) {
        toolTip.show(data);
      })
      // on hover event
      .on("mouseover", function(data, index) {
        toolTip.show(data);
      })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });
  };
});


