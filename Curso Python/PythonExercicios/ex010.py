print('='*5, 'Conversor de moeda', '='*5)
real = float(input('Digite o valor: R$ '))
dolar = 3.27
print('Com R$ {0:.2f}, você pode comprar U$ {1:.2f}.'.format(real, real/dolar))

