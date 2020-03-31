def aumentar(v=0, a=0):
    total = v + (v * a / 100)
    return total


def diminuir(v=0, d=0):
    total = v - (v * d / 100)
    return total


def dobro(v=0):
    total = v * 2
    return total


def metade(v=0):
    total = v / 2
    return total


def moeda(m):
    return f'R${m:.2f}'.replace('.', ',')
