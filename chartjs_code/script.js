
// Our labels along the x-axis
var years = [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050];
// For drawing the lines
var africa = [-86,114,106,106,107,111,133,221,783,2478];
var asia = [282,350,411,502,635,809,947,1402,3700,5267];
var europe = [168,170,178,190,203,276,408,547,675,734];
var latinAmerica = [40,20,10,16,24,38,74,167,508,784];
var northAmerica = [6,3,2,2,7,26,82,172,312,433];

var jsonfile = {
    "jsonarray": [{
       "time": "Joe",
       "sentiment": 12
    },{
       "time": "Tom",
       "sentiment": 14
    }]
 };
 
 var labels = amy_klobuchar.jsonarray.map(function(e) {
    return e.time;
 });
 var data = jsonfile.jsonarray.map(function(e) {
    return e.sentiment;
 });;

var ctx = document.getElementById("myChart");
var myChart = new Chart(ctx, {
  type: 'line',
  data: {
    // labels: labels,
    datasets: [
      { 
        data: amy_klobuchar,
        label: 'Amy Klobuchar',
        borderColor: "#3e95cd"
      },
      // { 
      //   data: andrew_yang, 
      //   label: 'Andrew Yang',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: bernie_sanders, 
      //   label: 'Bernie Sanders',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: elizabeth_warren, 
      //   label: 'Elizabeth Warren',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: joe_biden, 
      //   label: 'Joe Biden',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: pete_buttigieg, 
      //   label: 'Pete Buttigieg',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: tom_steyer, 
      //   label: 'Tom Steyer',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: donald_trump, 
      //   label: 'Donald Trump',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: democrat, 
      //   label: 'Democrat',
      //   borderColor: "#3e95cd"
      // },
      // { 
      //   data: republican, 
      //   label: 'Republican',
      //   borderColor: "#3e95cd"
      // }
    ]
  },
  options:{
    scales:{
      xAxes :[{
        type: "time",
        time: {
          format: "YYYY-MM-DDThh:mm:ss"
        },
        scaleLabel: {
          display: true,
          labelString: 'Date'
        }
      }]
    }
  }
});