function contador(){
    var inicio = document.getElementById('txtini')
    var fim = document.getElementById('txtfim')
    var pass = document.getElementById('txtpas')
    var res = document.getElementById('res')
    
    if (inicio.value.length == 0 || fim.value.length == 0 || pass.value.length == 0){
        alert('Falta dados. Impossível contar!')
    }else{
        if(pass.value == 0){
            window.alert('Passo inválido! Contando PASSO 1')
            pass.value = 1
        }
        
        res.innerHTML = 'Contando: <br>'               
        var i = Number(inicio.value)
        var f = Number(fim.value)
        var p = Number(pass.value)
        
        if (i > f){
            if(p < 0){
                p = p * (-1)            }
            for(var c = i; f <= c; c -= p){
                res.innerHTML += ` ${c} \u{27A1} `
            }
            res.innerText += `\u{1F3C1}`
        }else{
            if (p < 0){
                p = p * (-1)            }
            for(var c = i; c <= f; c += p){
                res.innerHTML += ` ${c} \u{27A1}` 
            }
            res.innerText += `\u{1F3C1}`
        }
    }
}  
