dado = list()
lista_dados = list()
peso = list()
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
#    if len(lista_dados) == 0:
#       mai = men = dado[1]
#    else:
#        if dado[1] > mai:
#            mai = dado[1]
#        if dado[1]< men:
#            men = dado[1]
    peso.append(dado[1])
    lista_dados.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('='*45)
print(f'Ao todo, foram cadastradas {len(lista_dados)} pessoas.')
print(f'O maior peso foi {max(peso):.1f}Kg. Peso de ', end='')
for n in lista_dados:
    if n[1] == max(peso):
        print(f'[{n[0].capitalize().strip()}]', end=' ')
print(f'\nO menor peso foi {min(peso):.1f}Kg. Peso de ', end='')
for n in lista_dados:
    if n[1] == min(peso):
        print(f'[{n[0].capitalize().strip()}]', end=' ')



