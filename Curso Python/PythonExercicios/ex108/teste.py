from ex108 import moeda
from cores import cores

cores(c=30)
print('='*5, 'Cálculo de preços', '='*5)
p = float(input('Digite um preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 20%, temos {moeda.moeda(moeda.aumentar(p, 20))}')
print(f'Reduzindo 17%, temos {moeda.moeda(moeda.diminuir(p, 17))}')
