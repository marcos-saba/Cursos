print('\033[30m-' * 48)
jogador = {'nome': str(input('Nome do Jogador: '))}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
tot = 0
for g in range(0, partidas):
    gol = int(input(f'Quantos gols na partida {g}? '))
    gols.append(gol)
    jogador['gols'] = gols
    tot += gol  # sum(gols)
    jogador['total'] = tot
print('=' * 48)
print(f'\033[33m{jogador}\033[30m')
print('=' * 48)
for j, v in jogador.items():
    print(f'O campo \033[34m{j}\033[30m tem o valor \033[32m{v}\033[30m.')
print('\033[30m=' * 48)
print(f'O jogador \033[34m{jogador["nome"]}\033[30m jogou '
      f'\033[33m{partidas}\033[30m partidas. ')  # len(jogador['gols'])
for p in range(0, partidas):
    print(f'    \033[30m=> Na partida \033[33m{p}\033[30m, fez '
          f'\033[32m{jogador["gols"][p]}\033[30m gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('-' * 48)
