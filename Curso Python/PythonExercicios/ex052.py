n = int(input('Digite um número inteiro: '))
'''if n != 2 and n % 2 == 0 or n != 3 and n % 3 == 0 or n != 5 \
        and n % 5 == 0 or n != 7 and n % 7 == 0 or n == 1:
    print(f'O número {n} não é primo.')
else:
    print(f'O número {n} é primo.')'''
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\033[m\nO número {n} foi divisível {tot} vez(es)')
if tot == 2:
    print('E por isso é primo.')
else:
    print('E por isso não é primo.')