var myConfig = {
  backgroundColor: "#fff",
  globals: {
    fontFamily: "Raleway",
    color: "#666"
  },
  graphset: [{
    type: "gauge",
    x: 0,
    y: 0,
    width: "31.5%",
    height: "50%",
    "media-rules": [{
      "max-width": 650,
      "x": 0,
      "y": "2%",
      "width": '100%',
      "height": "20%",
    },{
      "min-width": 651,
    x: 0,
    y: 0,
    width: "31.5%",
    height: "50%",
    }],
    title: {
      text: "Energy Output",
      "media-rules": [{
        "max-width": 650,
        "visible": false
      }]
    },
    scaleR: {
      aperture: 130,
      values: "0:40:10",
      guide: {
        backgroundColor: "#E3DEDA",
        alpha: 1
      },
      ring: {
        backgroundColor: "#E3DEDA",
        "media-rules": [{
          "max-width": 650,
          "visible": false
        }]
      },
      center: {
        size: 20,
        borderWidth: 2,
        borderColor: "#23211E",
        "media-rules": [{
          "max-width": 650,
          "size": 10
        }]
      },
      item: {
        offsetR: 0
      },
      tick: {
        visible: false
      },
      markers: [{
        type: "area",
        range: [0, 35],
        backgroundColor: "#00AE4D"
      }]
    },
    plotarea: {
      marginTop: "35%"
    },
    plot: {
      csize: "3%",
      size: "100%"
    },
    scale: {
      sizeFactor: 1.2,
      "media-rules": [{
        "max-width": 650,
        sizeFactor: 1.6,
      }]
    },
    tooltip: {
      visible: false
    },
    series: [{
      values: [35],
      backgroundColor: "#23211E",
      valueBox: {
        text: "%v",
        placement: "center",
        fontColor: "#00AE4D",
        fontSize: 14,
        "media-rules": [{
          "max-width": 650,
          "fontSize": 10
        }]
      }
    }]
  }, {
    type: "gauge",
    x: "34.5%",
    y: 0,
    width: "31.5%",
    height: "50%",
    "media-rules": [{
      "max-width": 650,
      "x": 0,
      "y": "20%",
      "width": '100%',
      "height": "20%",
    },{
      "min-width": 651,
      x: "34.5%",
      y: 0,
      width: "31.5%",
      height: "50%",
    }],
    title: {
      text: "Energy Recycled",
      "media-rules": [{
        "max-width": 650,
        "visible": false
      }]
    },
    scaleR: {
      aperture: 130,
      values: "0:20:5",
      guide: {
        backgroundColor: "#E3DEDA",
        alpha: 1
      },
      ring: {
        backgroundColor: "#E3DEDA",
        "media-rules": [{
          "max-width": 650,
          "visible": false
        }]
      },
      center: {
        size: 20,
        borderWidth: 2,
        borderColor: "#23211E",
        "media-rules": [{
          "max-width": 650,
          "size": 10
        }]
      },
      item: {
        offsetR: 0
      },
      tick: {
        visible: false
      },
      markers: [{
        type: "area",
        range: [0, 11],
        backgroundColor: "#E2D51A"
      }]
    },
    plotarea: {
      marginTop: "35%"
    },
    plot: {
      csize: "3%",
      size: "100%"
    },
    scale: {
      sizeFactor: 1.2,
      "media-rules": [{
        "max-width": 650,
        sizeFactor: 1.6,
      }]
    },
    tooltip: {
      visible: false
    },
    series: [{
      values: [11],
      backgroundColor: "#23211E",
      valueBox: {
        text: "%v",
        placement: "center",
        fontColor: "#E2D51A",
        fontSize: 14,
        "media-rules": [{
          "max-width": 650,
          "fontSize": 10
        }]
      }
    }]
  }, {
    type: "gauge",
    x: "69%",
    y: 0,
    width: "31.5%",
    height: "50%",
    "media-rules": [{
      "max-width": 650,
      "x": 0,
      "y": "40%",
      "width": '100%',
      "height": "20%",
    },{
      "min-width": 651,
      "x": "69%",
      "y": 0,
      "width": "31.5%",
      "height": "50%",
    }],
    title: {
      text: "Energy Consumed",
      "media-rules": [{
        "max-width": 650,
        "visible": false
      }]
    },
    scaleR: {
      aperture: 130,
      values: "0:100:25",
      guide: {
        backgroundColor: "#E3DEDA",
        alpha: 1
      },
      ring: {
        backgroundColor: "#E3DEDA",
        "media-rules": [{
          "max-width": 650,
          "visible": false
        }]
      },
      center: {
        size: 20,
        borderWidth: 2,
        borderColor: "#23211E",
        "media-rules": [{
          "max-width": 650,
          "size": 10
        }]
      },
      item: {
        offsetR: 0
      },
      tick: {
        visible: false
      },
      markers: [{
        type: "area",
        range: [0, 28],
        backgroundColor: "#FB301E"
      }]
    },
    plotarea: {
      marginTop: "35%"
    },
    plot: {
      csize: "3%",
      size: "100%"
    },
    scale: {
      sizeFactor: 1.2,
      "media-rules": [{
        "max-width": 650,
        sizeFactor: 1.6,
      }]
    },
    tooltip: {
      visible: false
    },
    series: [{
      values: [28],
      backgroundColor: "#23211E",
      valueBox: {
        text: "%v",
        placement: "center",
        fontColor: "#FB301E",
        fontSize: 14,
        "media-rules": [{
          "max-width": 650,
          "fontSize": 10
        }]
      }
    }]
  }, {
    type: "line",
    title: {
      text: "Meter History",
      adjustLayout: true,
      "media-rules": [{
        "max-width": 650,
        "fontSize": 14
      }]
    },
    x: 0,
    y: "45%",
    width: "100%",
    height: "55%",
    "media-rules": [{
      "max-width": 650,
      "x": 0,
      "y": "60%",
      "width": '100%',
      "height": "40%%",
    }],
    scaleX: {
      minValue: 1373045400000,
      step: 3000,
      transform: {
        type: "date",
        all: "%D<br>%H:%i:%s"
      }
    },
    "scale-y": {
      values: "0:100:25",
      placement: "default",
      lineColor: "#FB301E",
      tick: {
        lineColor: "#FB301E"
      },
      item: {
        fontColor: "#FB301E",
        bold: true
      }
    },
    "scale-y-2": {
      values: "0:20:5",
      placement: "default",
      lineColor: "#E2D51A",
      tick: {
        lineColor: "#E2D51A"
      },
      item: {
        fontColor: "#E2D51A",
        bold: true
      }
    },
    "scale-y-3": {
      values: "0:40:10",
      placement: "default",
      lineColor: "#00AE4D",
      tick: {
        lineColor: "#00AE4D",
      },
      item: {
        fontColor: "#00AE4D",
        bold: true
      }
    },
    plotarea: {
      margin: "dynamic",
      marginRight: "4%"
    },
    crosshairX: {
      lineColor: "#23211E",
      scaleLabel: {
        backgroundColor: "#E3DEDA",
        fontColor: "#414042"
      },
      plotLabel: {
        backgroundColor: "#f0ece8",
        fontColor: "#414042",
        borderWidth: 1,
        borderColor: "#000"
      }
    },
    tooltip: {
      visible: false
    },
    series: [{
      values: [35, 38, 40, 35, 38, 40, 35, 38, 40],
      lineColor: "#00AE4D",
      text: "Energy Output",
      scales: "scale-x, scale-y-3",
      marker: {
        borderWidth: 2,
        borderColor: "#00AE4D",
        backgroundColor: "#fff",
        type: "circle"
      }
    }, {
      values: [11, 15, 19, 11, 15, 19, 11, 15, 19],
      lineColor: "#E2D51A",
      text: "Energy Recycled",
      scales: "scale-x, scale-y-2",
      marker: {
        borderWidth: 2,
        borderColor: "#E2D51A",
        backgroundColor: "#fff",
        type: "triangle",
        size: 5
      }
    }, {
      values: [28, 21, 30, 28, 21, 30, 28, 21, 30],
      lineColor: "#FB301E",
      text: "Energy Consumed",
      scales: "scale-x, scale-y",
      marker: {
        borderWidth: 2,
        borderColor: "#FB301E",
        backgroundColor: "#fff",
        type: "square"
      }
    }]
  }]
};

zingchart.render({
  id: 'myChart',
  data: myConfig,
  height: "100%",
  width: '100%'
});

/*
 * SetInterval is used to simulate live input. We also have
 * a feed attribute that takes in http requests, websockets,
 * and return value from a JS function.
 */
setInterval(function() {
  var colors = ['#00AE4D', '#E2D51A', '#FB301E'];
  var Marker = function(bgColor, ceiling) {
    return {
      type: "area",
      range: [0, ceiling],
      backgroundColor: bgColor
    }
  };
  var randomOffset0 = [-5, 5, 3, -3, 2, -2];
  var randomOffset1 = [10, -10, -5, 5, 3, -3, 2, -2, 7, -7];
  var output0 = Math.ceil(33 + randomOffset0[Math.floor(Math.random() * 6)]);
  var output1 = Math.ceil(11 + randomOffset0[Math.floor(Math.random() * 6)]);
  var output2 = Math.ceil(22 + randomOffset1[Math.floor(Math.random() * 9)]);

  // 1) update gauge values
  zingchart.exec('myChart', 'appendseriesdata', {
    graphid: 0,
    plotindex: 0,
    update: false,
    data: {
      values: [output0]
    }
  });
  zingchart.exec('myChart', 'appendseriesdata', {
    graphid: 1,
    plotindex: 0,
    update: false,
    data: {
      values: [output1]
    }
  });
  zingchart.exec('myChart', 'appendseriesdata', {
    graphid: 2,
    plotindex: 0,
    update: false,
    data: {
      values: [output2]
    }
  });

  // 2) update guage markers
  zingchart.exec('myChart', 'modify', {
    graphid: 0,
    update: false,
    data: {
      scaleR: {
        markers: [
          Marker(colors[0], output0)
        ]
      }
    }
  });
  zingchart.exec('myChart', 'modify', {
    graphid: 1,
    update: false,
    data: {
      scaleR: {
        markers: [
          Marker(colors[1], output1)
        ]
      }
    }
  });
  zingchart.exec('myChart', 'modify', {
    graphid: 2,
    update: false,
    data: {
      scaleR: {
        markers: [
          Marker(colors[2], output2)
        ]
      }
    }
  });

  // 3) update line graph
  zingchart.exec('myChart', 'appendseriesvalues', {
    graphid: 3,
    update: false,
    values: [
      [output0],
      [output1],
      [output2]
    ]
  });

  // batch update all chart modifications
  zingchart.exec('myChart', 'update');

}, 1500);
