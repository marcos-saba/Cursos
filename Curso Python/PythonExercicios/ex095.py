jogador = dict()
time = list()
gol = list()
print('\033[30m-'*30)
while True:
    jogador['nome'] = str(input('Nome do Jogador: ')).capitalize()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, partidas):
        gol.append(int(input(f'Quantos gols na partida {p+1}? ')))
    jogador['gols'] = gol[:]
    jogador['total'] = sum(gol)
    time.append(jogador.copy())
    gol.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] '))
        if resp in 'SsNn':
            break
        print('\033[31mOPÇÃO INVÁLIDA! Responda apenas S ou N.\033[30m')
    if resp in 'Nn':
        break
    print('-'*30)
print('='*45)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
for p, j in enumerate(time):
    print(f'\033[34m{p:>3}\033[30m ', end='')
    for d in j.values():
        print(f'{str(d):<20}', end='')
    print()
print('\033[30m-'*45)
while True:
    opt = int(input('Mostrar dados de qual jogador[999 para sair]? '))
    if opt == 999:
        break
    if opt < 0 or opt >= len(time):
        print(f'\033[31mErro! Não existe jogador com o código {opt}! Tente novamente...\033[30m')
        print('-'*45)
    else:
        print(f'--- LEVATAMENTO DO JOGADOR \033[36m{time[opt]["nome"]}\033[30m:')
        for p, g in enumerate(time[opt]['gols']):
            print(f'    No jogo \033[34m{p+1}\033[30m fez \033[33m{g}\033[30m gols.')
        print('-'*35)
print('='*45)
print(f'{"<<< FIM >>>":^45}')
