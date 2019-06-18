function group_by_distance(data) {
    var output = {};
    for (var i = 0; i < data.length; i++) {
        // obtains distance from the venue
        var currentCrime = +data[i].dist_from_venue;
        // If the crime has been seen before...
        if (currentCrime in output) {
            // Add one to the counter
            output[currentCrime] += 1;
        }
        else {
            // Set the counter at 1
            output[currentCrime] = 1;
        }
    }
    return output;
}

function split_key_values(obj) {
    // split the keys and values into two lists
    var output = {
        x: [],
        y: []
    };

    var sorted = Object.keys(obj);
    sorted = sorted.sort();

    sorted.forEach((key) => {
        // sorts the values in the correct order
        output.x.push(+key);
        output.y.push(obj[key])
    });
    
    return output;
}

d3.json("/staples_crimes").then(function (data) {
    var staples_data = split_key_values(group_by_distance(data));
    console.log(staples_data);
    // create a line trace for all crimes near the Staples Center
    var trace1 = {
        x: staples_data.x,
        y: staples_data.y,
        type: "scatter",
        line: {
            color: "#DC143C"
          },
        name: "Staples Center"
       };
    d3.json("/coliseum_crimes").then(function (data) {
        var coliseum_data = split_key_values(group_by_distance(data));
        console.log(coliseum_data);
        // create a line trace for all crimes near the Coliseum
        var trace2 = {
            x: coliseum_data.x,
            y: coliseum_data.y,
            type: "scatter",
            line: {
                color: "#FFD700"
              },
            name: "Coliseum"
           };
        d3.json("/dodger_crimes").then(function (data) {
            var dodger_data = split_key_values(group_by_distance(data));
            console.log(dodger_data);
            // create a line trace for all crimes near the Dodger Stadium
            var trace3 = {
                x: dodger_data.x,
                y: dodger_data.y,
                type: "scatter",
                line: {
                    color: "#0000FF"
                  },
                name: "Dodger Stadium"
               };
    // Add titles
    var layout = {
        title: "Crime Count vs. Distance, by Arena",
        xaxis: { title: "Distance from Arena (mi)"},
        yaxis: { title: "Number of Crimes"}
    };

    var line_data = [trace1,trace2,trace3];

    Plotly.newPlot("plot", line_data, layout);
        });
    });
});

