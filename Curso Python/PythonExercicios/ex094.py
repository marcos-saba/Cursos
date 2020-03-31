pessoas = dict()
ficha = list()
totidade = 0
print(f'\033[32m{" CADASTRO DE PESSOAS ":*^45}\033[30m')
while True:
    pessoas['nome'] = str(input('Nome: ')).capitalize()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('\033[31mERRO! Por Favor, digite apenas M ou F.\033[30m')
    pessoas['idade'] = int(input('Idade: '))
    ficha.append(pessoas.copy())
    totidade += pessoas['idade']
    while True:
        resp = str(input('Quer continuar?[S/N] '))
        if resp in 'SsNn':
            break
        else:
            print('\033[31mERRO! Por favor, digite apenas S ou N.\033[30m')
    if resp in 'Nn':
        break
print('=.='*15)
media = totidade / len(ficha)
print(f'>> Ao todo foram cadastradas \033[33m{len(ficha)}\033[30m pessoa(s).')
print(f'>> A média de idade do grupo é de \033[33m{media:.2f}\033[30m anos.')
print('>> As mulheres cadastradas foram: \033[35m', end='')
for p in ficha:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('\033[30m>> Lista de pessoas acima da média de idade: ')
print()
for p in ficha:
    if p['idade'] > media:
        print(f'   nome = \033[34m{p["nome"]};\033[30m sexo = \033[32m{p["sexo"]}'
              f'\033[30m; idade = \033[33m{p["idade"]}\033[30m; ')
print('-'*45)
print('            <<<< ENCERRADO >>>>            ')
print('\033[30m*'*45)
