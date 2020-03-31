print('\033[30m**'*15)
print('SEQUÊNCIA DE FIBONACCI')
print('**'*15)
n = int(input('Digite o número de termos: '))
n1 = 0
n2 = 1
n3 = n1 + n2
cont = 1
while cont <= n:
    print('\033[33m', n1, end=' -> ')
    cont += 1
    n3 = n1 + n2
    n1 = n2
    n2 = n3
print('\033[30mFim.')
print('')
print('**'*15)