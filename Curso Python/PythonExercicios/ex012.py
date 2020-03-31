print('='*5, 'Cálculo de desconto', '='*5)
p = float(input('Digite o preço do produto: R$ '))#preço
d = float(input('Digite o desconto em (%): '))#desconto
vd = (p*d/100)#valor do desconto
np = p-vd#novo preço
print('Preço original do produto: R$ {:.2f} \nDesconto: {}%'.format(p, d))
print('Valor do desconto: R$ {:.2f} \nTotal a pagar c/ desconto: R$ {:.2f}'.format(vd, np))
print('='*12, '++++', '='*12)
