from ex109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 60%, temos {moeda.aumentar(p, 11, True)}')
print(f'Diminuindo 16%, temos {moeda.diminuir(p, 16, True)}')
