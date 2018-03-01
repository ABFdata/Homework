// D3 Scatterplot Assignment

// Students:
// =========
// Follow your written instructions and create a scatter plot with D3.js.

var svgWidth = 660; // 960
var svgHeight = 500; // 500

var margin = { top: 20, right: 40, bottom: 60, left: 100 };

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select(".chart")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var chart = svg.append("g");

// Append a div to the body to create tooltips, assign it a class
d3.select(".chart")
  .append("div")
  .attr("class", "tooltip")
  .style("opacity", 0);

d3.csv("healthData.csv", function(err, healthData) {
  if (err) throw err;

  healthData.forEach(function(data) {
    data.lessThanHS = +data.lessThanHS;
    data.poorHealth = +data.poorHealth;
    data.collegeGrad = +data.collegeGrad;

  });


  // Create scale functions
  var yLinearScale = d3.scaleLinear()
    .range([height, 0]);

  var xLinearScale = d3.scaleLinear()
    .range([0, width]);

  // Create axis functions
  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

// NEW LINE OF CODE FOR DYNAMIC CHART

 // These variables store the minimum and maximum values in a column in data.csv
 var xMin;
 var xMax;
 var yMax;

 // This function identifies the minimum and maximum values in a column in hairData.csv
  // and assign them to xMin and xMax variables, which will define the axis domain
    function findMinAndMax(dataColumnX) {
        xMin = d3.min(healthData, function (data) {
            return +data[dataColumnX] * 0.8;
        });

        xMax = d3.max(healthData, function (data) {
            return +data[dataColumnX] * 1.1;
        });

        yMax = d3.max(healthData, function (data) {
            return +data.poorHealth * 1.1;
        });
    }


// The default x-axis is 'lessThanHS'
  // Another axis can be assigned to the variable during an onclick event.
  // This variable is key to the ability to change axis/data column
  var currentAxisLabelX = "lessThanHS";


// Call findMinAndMax() with 'lessThanHS' as default
findMinAndMax(currentAxisLabelX);

// Set the domain of an axis to extend from the min to the max value of the data column
xLinearScale.domain([xMin, xMax]);
yLinearScale.domain([0, yMax]);

// Initialize tooltip
var toolTip = d3
    .tip()
    .attr("class", "tooltip")
    // Define position
    .offset([80, -60])
    // The html() method allows us to mix JavaScript with HTML in the callback function
    .html(function(data) {
      var state = data.state;
      //var school = +data.lessThanHS;
      var health = +data.poorHealth; // this line is the y axis
      var school = +data[currentAxisLabelX]; // this line is the current x axis which is lessThanHS
      var healthString;
      // Tooltip text depends on which axis is active/has been clicked
      if (currentAxisLabelX === "lessThanHS") {
        healthString = "Non hs grads: ";
      }
      else {
        healthString = "College grads: ";
      }
      return state +
        "<br>" +
        healthString +
        school + 
        "%" +
        "<br> Poor Health: " +
        health + "%";
    });

  // Scale the domain - OLD CODE FOR FIRST CHART
  /*
  xLinearScale.domain([6, d3.max(healthData, function(data) {
    return +data.lessThanHS;
  })]);
  yLinearScale.domain([0, d3.max(healthData, function(data) {
    return +data.poorHealth * 1.2;
  })]);

  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function(data) {
      var state = data.state;
      var school = +data.lessThanHS;
      var health = +data.poorHealth;
      return (state + "<br> Non hs grads: " + school + "%" + "<br> Poor Health: " + health + "%");
    });
    */


  // Create toolitp
  chart.call(toolTip);

  chart.selectAll("circle")
    .data(healthData)
    .enter().append("circle")
      .attr("cx", function(data, index) {
        console.log(data.lessThanHS);
        return xLinearScale(+data[currentAxisLabelX]);
      })
      .attr("cy", function(data, index) {
        return yLinearScale(data.poorHealth);
      })
      .attr("r", "5")
      .attr("fill", "lightslategray")
      .on("click", function(data) {
        toolTip.show(data);
      })
      .attr("r", "5")
      .attr("fill", "lightslategray")
      .on("mouseover", function(data) {
        toolTip.show(data);
      })
      // on mouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

  chart.append("g")
    .attr("transform", "translate(0," + height + ")")
    .attr("class", "x-axis")
    .call(bottomAxis);

  chart.append("g")
    .call(leftAxis);

// Append y-axis lables  
  chart.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axis-text")
      .attr("data-axis-name", "poorHealth")
      .text("Age 60+ with Poor Health (%)");

// Append x-axis labels
  chart
    .append("text")
    .attr(
        "transform", 
        "translate(" + width / 2 + " ," + (height + margin.top + 12) + ")"
    )
    // This axis label is active by default
    .attr("class", "axis-text active")
    .attr("data-axis-name", "lessThanHS")
    .text("Age 60+ non high school graduates (%)");

// Append other x axis
  chart
    .append("text")
    .attr(
      "transform",
      "translate(" + width / 2 + " ," + (height + margin.top + 30) + ")"
    )
    // This axis label is inactive by default
    .attr("class", "axis-text inactive")
    .attr("data-axis-name", "collegeGrad")
    .text("Age 60+ college graduates (%)");

  // Change an axis's status from inactive to active when clicked (if it was inactive)
  // Change the status of all active axes to inactive otherwise
  function labelChange(clickedAxis) {
    d3
      .selectAll(".axis-text")
      .filter(".active")
      // An alternative to .attr("class", <className>) method. Used to toggle classes.
      .classed("active", false)
      .classed("inactive", true);

    clickedAxis.classed("inactive", false).classed("active", true);
  }

  d3.selectAll(".axis-text").on("click", function() {
    // Assign a variable to current axis
    var clickedSelection = d3.select(this);
    // "true" or "false" based on whether the axis is currently selected
    var isClickedSelectionInactive = clickedSelection.classed("inactive");
    // console.log("this axis is inactive", isClickedSelectionInactive)
    // Grab the data-attribute of the axis and assign it to a variable
    // e.g. if data-axis-name is "poverty," var clickedAxis = "poverty"
    var clickedAxis = clickedSelection.attr("data-axis-name");
    console.log("current axis: ", clickedAxis);

    // The onclick events below take place only if the x-axis is inactive
    // Clicking on an already active axis will therefore do nothing
    if (isClickedSelectionInactive) {
      // Assign the clicked axis to the variable currentAxisLabelX
      currentAxisLabelX = clickedAxis;
      // Call findMinAndMax() to define the min and max domain values.
      findMinAndMax(currentAxisLabelX);
      // Set the domain for the x-axis
      xLinearScale.domain([xMin, xMax]);
      // Create a transition effect for the x-axis
      svg
        .select(".x-axis")
        .transition()
        // .ease(d3.easeElastic)
        .duration(1800)
        .call(bottomAxis);
      // Select all circles to create a transition effect, then relocate its horizontal location
      // based on the new axis that was selected/clicked
      d3.selectAll("circle").each(function() {
        d3
          .select(this)
          .transition()
          // .ease(d3.easeBounce)
          .attr("cx", function(data) {
            return xLinearScale(+data[currentAxisLabelX]);
          })
          .duration(1800);
      });

      // Change the status of the axes. See above for more info on this function.
      labelChange(clickedSelection);
    }
  });  
});



