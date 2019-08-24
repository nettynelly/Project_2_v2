// @TODO: YOUR CODE HERE!

/*
You need to create a scatter plot between two of the data variables such as
 `Healthcare vs. Poverty` or `Smokers vs. Age`.

Using the D3 techniques we taught you in class, create a scatter plot that 
represents each state with circle elements. You'll code this graphic in the 
`app.js` file of your homework directory—make sure you pull in the data from 
`data.csv` by using the `d3.csv` function. Your scatter plot should ultimately 
appear like the image at the top of this section.

* Include state abbreviations in the circles.

* Create and situate your axes and labels to the left and bottom of the chart.

* Note: You'll need to use `python -m http.server` to run the visualization. This will 
host the page at `localhost:8000` in your web browser.
*/

// Step 1 - Process Data, use D3

// create container for values
// payload = {
//   'HealthcareProvider': [],
//   'Age_60': [],
//   'MetalLevel': [],
//   'StateCode': []
// }

// function processDataAndGraph(data) {
//   console.log(data);

//   payload = {
//     'Healthcare Provider': [],
//     'Age_60': [],
//     'Metal Level': [],
//     'State Code': []
//   }

//   // loop through data, extracting th healthcare and poverty values
//   data.forEach(function (row) {
//     payload['Age_60'].push(+row['Age_60']);
//     payload['Healthcare Provider'].push(row['Healthcare Provider']);
//     payload['Metal Level'].push(row['Metal Level']);
//     payload['State Code'].push(row['State Code']);
//   })

//   console.log('This is payload:', payload);

//   // Step 2 - Organize Data so that we can place into graphs

//   console.log('Payload Age_60:');
//   console.log(payload['Age_60']);

//   // payload['Poverty'].forEach(function(value) {
//   //   console.log(value);
//   // })

//   var health_care = ['Healthcare Provider'].concat(payload['Healthcare Provider'])
//   var age_data = ['Age_60'].concat(payload['Age_60']);
//   var state_code = ['State Code'].concat(payload['State Code']);

//   console.log('Healthcare Provider', health_care);
//   console.log('Age_60', age_data);
//   console.log('State Code', state_code);

//   // Step 3 - Make Scatter Chart
//   var chart = c3.generate({
//     bindto: '#scatter',
//     data: {
//       xs: {
//         'Age_60': 'Age_60',
//         'Healthcare Provider': 'Healthcare Provider'
//       },
//       // iris data from R
//       columns: [
//         age_data,
//         health_care,
//       ],
//       type: 'scatter'
//     },
//     axis: {
//       x: {
//         label: 'Age',
//         tick: {
//           fit: false
//         }
//       },
//       y: {
//         label: 'Healthcare Provider'
//       }
//     },
//     point: {
//       r: 5
//     },
//     tooltip: {
//       format: {
//         title: function (x, index) {
//           return `[${state_code[index + 1]}] Age Rate: ` + x;
//         }
//       }
//     }
//   });

// }

// Average Price ber State (Pie Chart)
d3.csv("static/assets/data/state_stats.csv")
  .then(function (data) {
    console.log('state_stats', data);

    var state_data_set = [
      ['State Min'],
      ['State Max'],
      ['State Average']
    ];

    var labels = [];

    // process data for each type (top 10 only)
    for (let i = 0; i < 10; i++) {
      // State Min
      state_data_set[0].push(data[i]['Min']);
      // State Max
      state_data_set[1].push(data[i]['Max']);
      // State Average
      state_data_set[2].push(data[i]['Average']);

      labels.push(data[i]['State Code']);
    }

    // pass the newly processed data to the function
    var chart = c3.generate({
      bindto: '#state-bar',
      data: {
          columns: state_data_set,
          type: 'bar',
          types: {
            'State Average': 'spline',
          },
          groups: [
              ['State Min', 'State Max']
          ]
      },
      axis: {
        x: {
          label: 'State',
          type: 'category',
          categories: labels,
          tick: {
            fit: false
          }
        },
        y: {
          label: 'Price'
        }
      }
    });
  })

// Healthcare Providers Graph
d3.csv("static/assets/data/hcp_averages.csv")
  .then(function (data) {
    // console.log(data);

    payload = {}

    // Process Data
    data.forEach(function (row) {
      // create lists for each metal level
      // console.log(row);
      if (!payload[row['Metal Level']]) {
        payload[row['Metal Level']] = [row['Metal Level']];
        payload[row['Metal Level']].push(+row['Age_60']);
        payload['HealthcareProvider'] = ['HealthcareProvider', row['HealthcareProvider']]
      } else {
        payload[row['Metal Level']].push(+row['Age_60']);
        payload['HealthcareProvider'].push(row['HealthcareProvider']);
      }
    })

    console.log('Payload:', payload);

    // Build Graph
    var chart = c3.generate({
      bindto: '#hcp-scatter',
      data: {
        columns: [
          payload["Catastrophic"],
          payload["Expanded Bronze"],
          payload["Bronze"],
          payload["Silver"],
          payload["Gold"],
          payload["Platinum"],
        ],
        type: 'scatter'
      },
      axis: {
        x: {
          label: 'Healthcare Providers',
          tick: {
            fit: false
          }
        },
        y: {
          show: true,
          max: 3000,
          min: 0,
          label: 'Age 60 Premium',
          padding: {
            top: 0,
            bottom: 0
          }
        }
      },
      point: {
        r: 5
      },
    });
  })