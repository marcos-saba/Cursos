maior = homem = mulher = 0
print('\033[30m-'*25)
while True:
    print(f'{"CADASTRE UMA PESSOA":^25}')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-'*25)
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 25)
    if resposta == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior} '
      f'\nAo todo temos {homem} homem(s) cadastrado(s). '
      f'\nE temos {mulher} mulher(es) com menos de 20 anos.')
print('-'*25)
print(f'{"FIM DO PROGRAMA":^25}')
print('-'*25)
