$(function() {

  // Area Chart
  Morris.Area({
    element: 'morris-area-chart',
    data: [{
      period: '2018 Q1',
      may: 2666,
      april: null,
      march: 2647
    }, {
      period: '2018 Q2',
      may: 2778,
      april: 2294,
      march: 2441
    }, {
      period: '2018 Q3',
      may: 4912,
      april: 1969,
      march: 2501
    }, {
      period: '2018 Q4',
      may: 3767,
      april: 3597,
      march: 5689
    }, {
      period: '2018 Q1',
      may: 6810,
      april: 1914,
      march: 2293
    }, {
      period: '2018 Q2',
      may: 5670,
      april: 4293,
      march: 1881
    }, {
      period: '2018 Q3',
      may: 4820,
      april: 3795,
      march: 1588
    }, {
      period: '2018 Q4',
      may: 15073,
      april: 5967,
      march: 5175
    }, {
      period: '2018 Q1',
      may: 10687,
      april: 4460,
      march: 2028
    }, {
      period: '2018 Q2',
      may: 8432,
      april: 5713,
      march: 1791
    }],
    xkey: 'period',
    ykeys: ['may', 'april', 'march'],
    labels: ['May', 'April', 'March'],
    pointSize: 2,
    hideHover: 'auto',
    resize: true
  });

  // Donut Chart
  Morris.Donut({
    element: 'morris-donut-chart',
    data: [{
      label: "Lights",
      value: 120
    }, {
      label: "Heater",
      value: 300
    }, {
      label: "Utilities",
      value: 200
    }],
    resize: true
  });

  // Line Chart
  Morris.Line({
    // ID of the element in which to draw the chart.
    element: 'morris-line-chart',
    // Chart data records -- each entry in this array corresponds to a point on
    // the chart.
    data: [{
      d: '2018-4-01',
      consume: 802
    }, {
      d: '2018-4-02',
      consume: 783
    }, {
      d: '2018-4-03',
      consume: 820
    }, {
      d: '2018-4-04',
      consume: 839
    }, {
      d: '2018-4-05',
      consume: 792
    }, {
      d: '2018-4-06',
      consume: 859
    }, {
      d: '2018-4-07',
      consume: 790
    }, {
      d: '2018-4-08',
      consume: 1680
    }, {
      d: '2018-4-09',
      consume: 1592
    }, {
      d: '2018-4-10',
      consume: 1420
    }, {
      d: '2018-4-11',
      consume: 882
    }, {
      d: '2018-4-12',
      consume: 889
    }, {
      d: '2018-4-13',
      consume: 819
    }, {
      d: '2018-4-14',
      consume: 849
    }, {
      d: '2018-4-15',
      consume: 870
    }, {
      d: '2018-4-16',
      consume: 1063
    }, {
      d: '2018-4-17',
      consume: 1192
    }, {
      d: '2018-4-18',
      consume: 1224
    }, {
      d: '2018-4-19',
      consume: 1329
    }, {
      d: '2018-4-20',
      consume: 1329
    }, {
      d: '2018-4-21',
      consume: 1239
    }, {
      d: '2018-4-22',
      consume: 1190
    }, {
      d: '2018-4-23',
      consume: 1312
    }, {
      d: '2018-4-24',
      consume: 1293
    }, {
      d: '2018-4-25',
      consume: 1283
    }, {
      d: '2018-4-26',
      consume: 1248
    }, {
      d: '2018-4-27',
      consume: 1323
    }, {
      d: '2018-4-28',
      consume: 1390
    }, {
      d: '2018-4-29',
      consume: 1420
    }, {
      d: '2018-4-30',
      consume: 1529
    }, {
      d: '2018-4-31',
      consume: 1892
    }, ],
    xkey: 'd',
    ykeys: ['consume'],
    labels: ['consume'],
    smooth: false,
    resize: true
  });

  // Bar Chart
  Morris.Bar({
    element: 'morris-bar-chart',
    data: [{
      device: 'March',
      consume: 310
    }, {
      device: 'May',
      consume: 270
    }, {
      device: 'June',
      consume: 190
    }],
    xkey: 'device',
    ykeys: ['consume'],
    labels: ['consume'],
    barRatio: 0.4,
    xLabelAngle: 35,
    hideHover: 'auto',
    resize: true
  });


});

