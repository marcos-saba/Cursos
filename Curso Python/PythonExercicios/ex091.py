from random import randint
from time import sleep
from operator import itemgetter
cont = 1
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
ranking = list()
print('\033[30m='*40)
print('Valores sorteados: ')
for j, d in jogo.items():
    sleep(1)
    print(f'    O {j} tirou {d} no dado.')
print('-'*40)
print(f'{"<< RANKING DOS JOGADORES >>":^40}')
print()
ranking = sorted(jogo.items(), reverse=True, key=itemgetter(1))
for j in ranking:
    sleep(1)
    print(f'       {cont}° lugar: {j[0]} com {j[1]}.')
    cont += 1
print('='*40)