valores = list()
print('\033[30m-'*40)
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('\033[33mValor já existente! Não será adicionado...\033[30m')
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
        if resp[0] in 'SN':
            break
    if resp in 'N':
        break
valores.sort()
print('-'*40)
print(f'Você digitou os valores {valores}')
