 google.charts.load('current', {'packages':['corechart', 'line']});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var i = 0;
          var data = new google.visualization.DataTable();
          data.addColumn('date', 'Dia');
          data.addColumn('number', 'Nvidia RTX2060');

    {% for row in results %}
       if( i < 60){
        {% if row[2] == 'Nvidia RTX 2060'%}
            data.addRows([[ new Date(2021, 8, 1 + i), {{ row[0] }} ]]);
        {% endif %}
            i++;
       };
    {% endfor %}
      var options = {
            title: 'Variação do preço das placas de vídeo',
            subtitle: 'Em reais (BRL)',
          vAxis: {
              scaleType: 'log',
              title: 'Preço',
              textStyle: {
                color: 'black',
                fontSize: 12,
                bold: true
              },
              titleTextStyle: {
                color: 'black',
                fontSize: 16,
                bold: true,
              },
            },
          hAxis: {
              format: 'd/M',
              title: 'Dia',
              textStyle: {
                fontSize: 12,
                color: 'black',
              },
            },
          axes: {
              x: {
                20: {side: 'bottom'},
              },
            },
          backgroundColor: '#f1f8e9',
      };
      var chart = new google.charts.Line(document.getElementById('line_top_x'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    };
