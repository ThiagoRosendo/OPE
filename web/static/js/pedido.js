function get_total1(){

    var item1 = document.getElementById("id_pedido_det-0-subtotal").value.replace(",", ".");
    var item2 = document.getElementById("id_pedido_det-1-subtotal").value.replace(",", ".");
    var item3 = document.getElementById("id_pedido_det-2-subtotal").value.replace(",", ".");
    
    if (item1 == "") {
        var item1 = "0";
    }
    
    if (item2 == "") {
        var item2 = "0";
    }
    
    if (item3 == "") {
        var item3 = "0";
    }
    var preco1 = parseFloat(item1);
    var preco2 = parseFloat(item2);
    var preco3 = parseFloat(item3);
    var total = (preco1 + preco2 + preco3).toFixed(2);
    
    document.getElementById("id_total").innerHTML = total.replace(".", ",");
    document.getElementById("id_valor_total").value = total;
    };

    function aplica_desconto(valor){
        if (valor == ''){
            return false
        }
        var item1 = document.getElementById("id_pedido_det-0-preco").value;
        var item2 = document.getElementById("id_pedido_det-1-preco").value;
        var item3 = document.getElementById("id_pedido_det-2-preco").value;
        var item1_r = item1.replace(",", ".");
        var item2_r = item2.replace(",", ".");
        var item3_r = item3.replace(",", ".");
        var item1_c = parseFloat(item1_r).toFixed(2);
        var item2_c = parseFloat(item2_r).toFixed(2);
        var item3_c = parseFloat(item3_r).toFixed(2);

        
        var desconto = valor.replace(",", ".");
        var desconto_float = parseFloat(desconto).toFixed(1);
        var operador = 1 - (desconto_float / 100);

           
    document.getElementById("id_pedido_det-0-preco").value = parseFloat(item1_c * operador).toFixed(2);
    document.getElementById("id_pedido_det-1-preco").value = parseFloat(item2_c * operador).toFixed(2);
    document.getElementById("id_pedido_det-2-preco").value = parseFloat(item3_c * operador).toFixed(2);


    };

    function aplica_total(){
        document.getElementById("id_valor_total").value = get_total1();

    }