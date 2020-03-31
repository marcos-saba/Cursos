#valor = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
lin = col = 0
print('\033[30m')
'''for c in range(0, 9):
    valor = int(input(f'Digite um valor para [{lin}, {col}]: '))
    if lin == 0:
        matriz[0].append(valor)
    elif lin == 1:
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)
    if col < 2:
        col += 1
    else:
        col = 0
    if c < 2:
        lin = 0
    elif 2 <= c < 5:
        lin = 1
    else:
        lin = 2
print('='*32)
for p, v in enumerate(matriz):
    print(f'\033[30m[ \033[33m{v[0]:^5}\033[30m ][ \033[33m{v[1]:^5}\033[30m ]'
          f'[ \033[33m{v[2]:^5}\033[30m ]')'''
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('-'*32)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
