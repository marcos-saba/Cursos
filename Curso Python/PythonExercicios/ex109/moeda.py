def aumentar(v=0, a=0, form=False):
    valor = float(v)
    total = valor + (valor * a / 100)
    if form:
        return moeda(total)
    else:
        return total


def diminuir(v=0, d=0, form=False):
    total = v - (v * d / 100)
    if form:
        return moeda(total)
    else:
        return total


def dobro(v=0, form=False):
    total = v * 2
    if form:
        return moeda(total)
    else:
        return total


def metade(v=0, form=False):
    total = v / 2
    if form:
        return moeda(total)
    else:
        return total


def moeda(m):
    return f'R${m:.2f}'.replace('.', ',')