from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
'''maior = 0
menor = 0'''
print('\033[30mOs valores sorteados foram:\033[33m', end=' ')
for n in num:
    print(n, end=' ')
    ''''if c == 0:
        maior = a[0]
        menor = a[0]
    elif a[c] > maior:
        maior = a[c]
    elif a[c] < menor:
        menor = a[c]'''
print(f'\n\033[30mO maior valor sorteado foi:\033[33m {max(num)}')
print(f'\033[30mO menor valor sorteado foi: \033[33m{min(num)}')
