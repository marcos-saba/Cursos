print('='*5, 'Cálculo de aumento de salário', '='*5)
sa = float(input(' Digite o salário em (R$): '))#salário
au = float(input(' Digite o aumento em (%): '))#aumento
va = sa*(au/100)
ns = sa+va
print(' Salário atual: R$ {:.2f}. \n Aumento: {}%.'.format(sa, au))
print(' Valor do aumento: R$ {:.2f}. \n Novo salário c/ aumento: R$ {:.2f}.'.format(va, ns))
print('='*15, '+++++', '='*15)