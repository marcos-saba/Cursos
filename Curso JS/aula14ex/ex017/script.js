function tabuada(){
    var num = document.getElementById('txtn')
    var valor = document.getElementById('val')
   
    if(num.value.length == 0){
        alert('Por favor digite um número')
    }else{
        var n = Number(num.value)
        valor.innerHTML = ' '
        for(var c = 1; c <= 10; c++){
            let item = document.createElement('option')
            item.text += `${n} x ${c} = ${n*c}`
            item.value = `valor${c}`
            valor.appendChild(item)

        }   
    }
}