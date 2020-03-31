def aumentar(v, a=0, form=False):
    total = v + (v * a / 100)
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
    valor = float(m)
    return f'R${valor:.2f}'


def resumo(v, a=0, d=0):
    import cores
    cores.cores(c=30)
    print('='*30)
    cores.cores(c=36)
    print(f'{"RESUMO DO VALOR":^30}')
    cores.cores(c=30)
    print(f'=' * 30)
    print(f'{"Preço analisado: ":20}\033[33m{moeda(v)}\033[30m')
    print(f'{"Dobro do preço: ":20}\033[33m{moeda(dobro(v))}\033[30m')
    print(f'{"Metade do preço: ":20}\033[33m{moeda(metade(v))}\033[30m')
    print(f'\033[35m{a:<3}\033[30m{"% de aumento:":17}\033[33m{moeda(aumentar(v, a))}\033[30m')
    print(f'\033[35m{d:<3}\033[30m{"% de redução:":17}\033[33m{moeda(diminuir(v, d))}\033[30m')
    print('='*30)



