nome = ''
preco = maior = menor = cont = tot = 0
barato = ''
print('\033[30m-'*30)
print(f' {"LOJA BARATEIRO":^30} ')
print('-'*30)
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    tot += preco
    cont += 1
    if preco > 1000:
        maior += 1
    if cont == 1 or preco < menor:
        barato = nome
        menor = preco
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta == 'N':
        break
print('-'*12, '*FIM*', '-'*12)
print(f'O total da compra foi de R${tot:.2f} '
      f'\nTemos {maior} produtos custando mais de R$1000.00 '
      f'\nO produto mais barato foi {barato.capitalize()} que custa R${menor:.2f} ')
