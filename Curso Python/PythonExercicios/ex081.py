num = []
quant = 1
print('\033[30m-'*45)
while True:
    num.append(int(input('Digite um número: ')))
    resp = ' '
    while resp[0] not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp[0] == 'N':
        break
    quant += 1
print('-'*45)
print(f'Você digitou {quant} números.')
num.sort(reverse=True)
print(f'\033[30mOs números em ordem decrescente são \033[34m{num}\033[30m')
if 5 in num:
    print('O número\033[33m 5\033[30m faz parte da lista e \napareceu nas posições\033[33m ', end='')
    for p, v in enumerate(num):
        if v == 5:
            print(p, end='... ')
else:
    print('\033[30mO número \033[33m5\033[30m não está na lista.')
print('')
print('\033[30m-'*45)
