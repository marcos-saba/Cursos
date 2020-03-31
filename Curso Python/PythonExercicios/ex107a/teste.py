from ex107a import moeda
from cores import cores

cores(c=30)
print('='*5, 'Cálculo de preços', '='*5)
p = float(input('Digite um preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 20%, temos {moeda.aumentar(p, 20)}')
print(f'Reduzindo 17%, temos {moeda.diminuir(p, 17)}')
