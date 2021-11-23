    var NvidiaRTX2060, NvidiaRTX3060, NvidiaRTX3070, NvidiaRTX3080, NvidiaRTX3090;
    var placasSelecionadas = [];
    var feito = [];

    var matriz = [[],[],[],[],[]];
    {% for row in results %}
        {% if row[2] == 'Nvidia RTX 2060'%}
            var adicionar = matriz[0].push({{ row[0] }});
        {% endif %}
        {% if row[2] == 'Nvidia RTX 3060'%}
            var adicionar = matriz[1].push({{ row[0] }});
        {% endif %}
        {% if row[2] == 'Nvidia RTX 3070'%}
            var adicionar = matriz[2].push({{ row[0] }});
        {% endif %}
        {% if row[2] == 'Nvidia RTX 3080'%}
            var adicionar = matriz[3].push({{ row[0] }});
        {% endif %}
        {% if row[2] == 'Nvidia RTX 3090'%}
            var adicionar = matriz[4].push({{ row[0] }});
        {% endif %}
    {% endfor %}

    class Placa{
        constructor(nome, preco) {
            this.nome = nome;
            this.preco = preco;
        }
    }
    let aPlaca2060 = new Placa("Nvidia RTX2060", matriz[0]);
    let aPlaca3060 = new Placa("Nvidia RTX3060", matriz[1]);
    let aPlaca3070 = new Placa("Nvidia RTX3070", matriz[2]);
    let aPlaca3080 = new Placa("Nvidia RTX3080", matriz[3]);
    let aPlaca3090 = new Placa("Nvidia RTX3090", matriz[4]);

    function valor(){
            var nomePlacaVideo = document.getElementsByName('RTX');
            placasSelecionadas = [];
            feito = [];
            for(var i = 0; i< nomePlacaVideo.length; i++){
                if ( nomePlacaVideo[i].checked ) {
                    if(nomePlacaVideo[i].value == "Nvidia RTX2060"){
                        var adicionar = placasSelecionadas.push("Nvidia RTX2060");
                        var NvidiaRTX2060 = "Nvidia RTX2060";
                        var adicionarPlaca = feito.push(aPlaca2060.preco);
                    }
                    else if(nomePlacaVideo[i].value == "Nvidia RTX3060") {
                        var adicionar = placasSelecionadas.push("Nvidia RTX3060");
                        var NvidiaRTX3060 = "Nvidia RTX3060";
                        var adicionarPlaca = feito.push(aPlaca3060.preco);
                    }
                    else if(nomePlacaVideo[i].value == "Nvidia RTX3070") {
                        var adicionar = placasSelecionadas.push("Nvidia RTX3070");
                        var NvidiaRTX3070 = "Nvidia RTX3070";
                        var adicionarPlaca = feito.push(aPlaca3070.preco);
                    }
                    else if(nomePlacaVideo[i].value == "Nvidia RTX3080") {
                        var adicionar = placasSelecionadas.push("Nvidia RTX3080");
                        var NvidiaRTX3080 = "Nvidia RTX3080";
                        var adicionarPlaca = feito.push(aPlaca3080.preco);
                    }
                    else if(nomePlacaVideo[i].value == "Nvidia RTX3090") {
                        var adicionar = placasSelecionadas.push("Nvidia RTX3090");
                        var NvidiaRTX3090 = "Nvidia RTX3090";
                        var adicionarPlaca = feito.push(aPlaca3090.preco);
                    }
                }
            }
        }
    var checkBoxes = document.querySelectorAll(".checkbox");
    var selecionados = 0;
    var btn = document.querySelector("#send");
    btn.addEventListener("click", function(e) {
        e.preventDefault();
        selecionados = 0;
        checkBoxes.forEach(function(el){
           if(el.checked){
                selecionados++;
           }
           google.charts.load('current', {'packages':['corechart', 'line']});
           google.charts.setOnLoadCallback(drawChart);
        });
    });
    function drawChart() {
      var i = 0;
          var data = new google.visualization.DataTable();
          data.addColumn('date', 'Dia');
          for(let i = 0; i < placasSelecionadas.length; i++){
            data.addColumn('number', placasSelecionadas[i]);
          }
    {% for row in results %}
       if( i < 60){
          if( selecionados == 5){
            data.addRows([[ new Date(2021, 8, 1 + i), feito[0][i], feito[1][i], feito[2][i], feito[3][i], feito[4][i] ]]);
          }
          if( selecionados == 4){
            data.addRows([[ new Date(2021, 8, 1 + i), feito[0][i], feito[1][i], feito[2][i], feito[3][i] ]]);
          }
          if( selecionados == 3){
            data.addRows([[ new Date(2021, 8, 1 + i), feito[0][i], feito[1][i], feito[2][i] ]]);
          }
          else if( selecionados == 2){
            data.addRows([[ new Date(2021, 8, 1 + i), feito[0][i], feito[1][i] ]]);
          }
          else if( selecionados == 1){
            data.addRows([[ new Date(2021, 8, 1 + i), feito[0][i] ]]);
          }
            i++;
       };
    {% endfor %}
      var options = {
            title: 'Variação do preço das placas de vídeo.',
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
                bold: true
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
          width: 1300,
          height: 540,
          axes: {
              x: {
                20: {side: 'bottom'},
              },
            },
          backgroundColor: '#f1f8e9'
      };
      var chart = new google.charts.Line(document.getElementById('line_top_x'));
      chart.draw(data, google.charts.Line.convertOptions(options));
    };
