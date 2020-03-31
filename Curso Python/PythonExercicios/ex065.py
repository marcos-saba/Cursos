print('\033[30m---'*11)
print('COMPARANDO VALORES')
print('---'*11)
n = int(input(f'Digite um valor: '))
print('---'*11)
resposta = 'S'
cont = maior = menor = 0
soma = n
while resposta != 'N':
    cont += 1
    if cont == 1:
        menor = maior = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    print('Quer continuar? \nSIM [ S ]\nNÃO [ N ]')
    resposta = str(input('Resposta: ')).upper().strip()
    if resposta[0] != 'S' and resposta[0] != 'N':
        print('\033[31mOpção inválida. tente de novamente.\033[30m')
        cont -= 1
    else:
        if resposta[0] == 'S':
            print('---'*11)
            n = int(input('Digite outro valor: '))
            print('---'*11)
            soma += n
media = soma / cont
print('---'*11)
print(f'Média dos valores digitados: \033[36m{media:.2f}\033[30m'
      f'\nMaior valor: \033[33m{maior}\033[30m'
      f'\nMenor valor: \033[34m{menor}\033[30m')
print('---'*11)
