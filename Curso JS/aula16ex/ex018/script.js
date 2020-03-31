let num = document.getElementById('txtnum')
let listanum = document.getElementById('lsnum')
let res = document.getElementById('res')
let lista = []

function adicionar(){  
    let n = Number(num.value)    
    
    if(n < 1 || n > 100 || n == 0 || lista.indexOf(n) !== -1){
        window.alert('Valor inválido e ou já encontrado na lista!')
    }else{
        res.innerHTML = ''
        lista.push(n)
        let item = document.createElement('option')
        item.text += `Valor ${n} adicionado.`
        listanum.appendChild(item)
    }
    num.value = ''   //limpa campo número
    num.focus()      //foca o curso no campo
}

function finalizar(){   
    if (lista.length == 0){
        window.alert('Adicione valores antes de finalizar.')
    }else{
        let soma = 0
        let maior = lista[0]
        let menor = lista[0]
        for (let pos in lista){    //busca maior, menor e soma números da lista
            soma += lista[pos]
            if(lista[pos] > maior)
                maior = lista[pos]
            if(lista[pos] < menor)
                menor = lista[pos]
            }
        
        let media = soma / lista.length
        
        res.innerHTML = ''  //limpa último texto
        res.innerHTML += `<p>Ao todo, temos ${lista.length} números informados. </p>`
        res.innerHTML += `<p>O maior número informado foi ${maior}. </p>`
        res.innerHTML += `<p>O menor número informado foi ${menor}. </p>`
        res.innerHTML += `<p>Somando todos os valores temos ${soma}. </p>`
        res.innerHTML += `<p>A média dos valores digitados é ${media}.</p>` 
    }  
}