from utilidadesCeV import moeda, dado

p = dado.teste('\033[30mDigite o preço: R$')
moeda.resumo(p, 25, 27)
