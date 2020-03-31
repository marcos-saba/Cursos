def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a}m².')


print('-' * 20)
print('CONTROLE DE TERRENO')
print('-'*20)
print('-'*45)
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m):'))
area(larg, comp)
print('-'*45)
