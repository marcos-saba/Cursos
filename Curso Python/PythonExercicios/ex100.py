from time import sleep
from random import randint


def sorteia(sort):
    print('\033[30mSorteando 5 valores da lista: \033[33m', end='')
    for p in range(0, 5):
        sort.append(randint(0, 10))
        print(sort[p], end=' ')
        sleep(.5)
    print('\033[30mPRONTO!')


def somaPar(par):
    p = 0
    for v in par:
        if v % 2 == 0:
            p += v
    print(f'\033[30mSomando os valores pares de \033[33m{par}\033[30m, temos \033[36m{p}')


num = list()
sorteia(num)
somaPar(num)
