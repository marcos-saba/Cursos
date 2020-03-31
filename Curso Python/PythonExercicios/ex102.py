def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-'*32)
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}', end='')
            print(' x ' if c > 1 else ' = ', end='')
        f *= c
    return f'\033[33m{f}\033[30m'


print('\033[30m='*10, '\033[36m FATORIAL!\033[30m ', '='*10)
num = int(input('\033[30mFatorial de qual número? '))
resp = ' '
while resp not in 'SsNn':
    resp = str(input('Mostra o cálculo?[S/N] ')).strip()[0]
    if resp not in 'SsNn':
        print('\033[31mRESPONDA APENAS S/N!\033[30m')
ajuda = ' '
while ajuda not in 'SsNn':
    ajuda = str(input('Mostrar documentação da função?[S/N] ')).strip()[0]
    if ajuda not in 'SsNn':
        print('\033[31mRESPONDA APENSA S/N!\033[30m')
if resp in 'Ss':
    print(fatorial(num, True))
else:
    print(fatorial(num))
if ajuda in 'Ss':
    print()
    help(fatorial)