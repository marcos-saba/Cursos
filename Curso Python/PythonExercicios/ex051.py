print('\033[30m##'*5, ' PROGRESSÃO ARITMÉTICA ', '##'*5)
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
decimo = pt + (10 - 1) * r
'''print('OS dez primeiros termos da PA são: ', end='')
for c in range(0, 10):
    pt += r
    print(f'\033[33m{pt}', end=' -> ')'''
for c in range(pt, decimo + r, r):
    print(f'\033[33m {c}', end=' -> ')
print('\033[36mFIM')