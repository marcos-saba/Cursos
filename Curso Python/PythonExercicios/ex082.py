lista = []
pares = []
impares = []
print('\033[30m-'*45)
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp in 'N':
        break
for c, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-'*45)
print(f'A lista completa é \033[33m{lista}\033[30m')
print(f'A lista com os valores pares é \033[34m{pares}\033[30m')
print(f'A lista com os valores ímpares é \033[36m{impares}\033[30m')
print('-'*45)