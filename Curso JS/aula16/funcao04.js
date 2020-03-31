function fatoriral(n){
    for (let c = n - 1 ; c > 1; c--){
        n *= c
    }
    return n
}

console.log(fatoriral(5))