function remove_inicio(data, selectList){
    var inicio = get_hora_inicio(data);
    var fim = get_hora_fim(data);
    var len = selectList.options.length;

for (i=1; i < len ; i++){
for (k=0; k < inicio.length; k++){

if (selectList.options[i].value == inicio[k]) {
  while (selectList.options[i].value < fim[k]){
  selectList.remove(i); 
  } 
};
};
};
  };

 function remove_fim(data, selectList, input_inicio){
    var inicio = get_hora_inicio(data);
    var fim = get_hora_fim(data);
    var len = selectList.options.length;

// remove todos os horários anteriores ao input
    
        while (selectList.options[1].value <= input_inicio){
          selectList.remove(1); 
    }
// remove todos os horários até o início do próximo atendimento
  for (i=0; i < inicio.length; i++){
    if (inicio[i] > input_inicio){
      while (selectList.options[selectList.options.length -1].value > inicio[i])
      selectList.remove(selectList.options.length -1)
    }
  }
    };

function reset_horarios(){
  var inicio = document.getElementById("id_hora_inicio").options;
  var fim = document.getElementById("id_hora_fim").options;
  var selectList_i = document.getElementById("id_hora_inicio");
  var selectList_f = document.getElementById("id_hora_fim");

  while (inicio.length > 1){
    selectList_i.remove(inicio.length - 1)
  };
  while (fim.length > 1){
    selectList_f.remove(fim.length - 1)
  };
  for (i=0; i < horarios.length; i++){
    var option = document.createElement("option");
    option.text = horarios[i];
    option.value = horarios[i];
    selectList_i.add(option);
  };
  for (i=0; i < horarios.length; i++){
    var option = document.createElement("option");
    option.text = horarios[i];
    option.value = horarios[i];
    selectList_f.add(option);
  }

}
 function reset_hora_fim(){
  var fim = document.getElementById("id_hora_fim").options;
  var selectList_f = document.getElementById("id_hora_fim");
  
  while (fim.length > 1){
    selectList_f.remove(fim.length - 1)
  };

  for (i=0; i < horarios.length; i++){
    var option = document.createElement("option");
    option.text = horarios[i];
    option.value = horarios[i];
    selectList_f.add(option);
  };
 }