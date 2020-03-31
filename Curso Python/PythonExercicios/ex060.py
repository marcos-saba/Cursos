print('=='*7, ' FATORIAL ', '=='*7)
n1 = int(input('Digite um número para ver seu fatorial: '))
fatorial = 1
n2 = n1
print(f'Fatorial no número {n1}!:')
'''while n2 > 0:
    print(f'{n2}', end='')
    print(' x ' if n2 > 1 else ' = ', end='')
    fatorial *= n2
    n2 -= 1
print(f'{fatorial}')'''
for c in range(n1, 0, -1):
    print(f'{c}', end='')
    print(' x 'if c > 1 else ' = ', end='')
    fatorial *= c
print(f'{fatorial}')
'''from math import factorial
n1 = int(input('Digite um número: '))
print(f'Fatorial do número {n1}!: {factorial(n1)} ')'''