def aumentar(v, a=0, form=False):
    valor = float(v)
    total = valor + (valor * a / 100)
    if form:
        return moeda(total)
    else:
        return total


def diminuir(v, d=0, form=False):
    total = v - (v * d / 100)
    if form:
        return moeda(total)
    else:
        return total


def dobro(v, form=False):
    total = v * 2
    if form:
        return moeda(total)
    else:
        return total


def metade(v, form=False):
    total = v / 2
    if form:
        return moeda(total)
    else:
        return total


def moeda(m):
    return f'R${m:.2f}'.replace('.', ',')


def resumo(v, a=0, d=0):
    import cores
    cores.cores(c=30)
    print('='*30)
    cores.cores(c=36)
    print('RESUMO DO VALOR'.center(30))
    cores.cores(c=30)
    print(f'=' * 30)
    print(f'Preço analisado: \033[33m\t{moeda(v)}\033[30m')
    print(f'Dobro do preço: \033[33m\t{moeda(dobro(v))}\033[30m')
    print(f'Metade do preço: \033[33m\t{moeda(metade(v))}\033[30m')
    print(f'\033[35m{a}\033[30m% de aumento: \033[33m\t{moeda(aumentar(v, a))}\033[30m')
    print(f'\033[35m{d}\033[30m% de redução: \033[33m\t{moeda(diminuir(v, d))}\033[30m')
    print('='*30)
