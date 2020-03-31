let num = [5, 8, 2, 9, 3]


//console.log(`Nosso vetor é o ${num}`)
//num.push(4)
//num[6] = 45
//console.log(num)
//console.log(num.length)

num.sort()
/*console.log(num)
console.log(`O vetor tem ${num.length} posições.`)
console.log(`O primeiro valor do vetor é ${num[0]}`)
/*for (var pos = 0; pos < num.length ; pos++){
    console.log(`O valor na posição ${pos+1} é ${num[pos]}`)
}*/
/*for(let pos in num){
    console.log(`O valor na posição ${Number(pos) + 1} é ${num[pos]}`)
}*/
let pos = num.indexOf(10)
if (pos == -1) {
    console.log('O valor não foi encontrado!')
}else{
    console.log(`O valor 8 está na posição ${pos}`)
}
