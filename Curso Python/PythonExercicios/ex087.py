matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s_par = 0
s_ter = 0
#maior = 0
print('\033[30m='*40)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=' * 40)
for lin in range(0, 3):
    s_ter += matriz[lin][2]
    for c in range(0, 3):
        if matriz[lin][c] % 2 == 0:
            s_par += matriz[lin][c]
        print(f'[{matriz[lin][c]:^5}]', end=' ')
# for p, v in enumerate(matriz[1]):
#    if p == 0:
#       maior = v
#    elif v > maior:
#       maior = v
    print()
print('=' * 40)
print(f'A soma dos valores pares é \033[34m{s_par}')
print(f'\033[30mA soma dos valores da terceira coluna é \033[33m{s_ter}')
print(f'\033[30mO maior valor da segunda linha é \033[36m{max(matriz[1])}')
