print('\033[30m=-='*8, ' \033[4mPROGRESSÃO ARITIMÉTICA\033[30m ', '\033[m\033[30m=-='*8)
ptermo = int(input('\33[30mPrimeiro termo: '))
razao = int(input('Razão: '))
contagem = 1
pa = ptermo
print(f'\033[30mOs 10 primeiros termos da PA do número \033[32m{ptermo}\033[30m são: '
      f'\ninício -> \033[33m', end='')
while contagem <= 10:
    print(pa, end=' -> ')
    pa += razao
    contagem += 1
print('\033[30mFim.')
print('=-='*25)


