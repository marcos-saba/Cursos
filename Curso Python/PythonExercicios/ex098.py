from time import sleep


def contador(i, f, p):
    print('=' * 40)
    if p == 0:
        p = 1
    elif p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(.5)
    if i < f:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.5)
    else:
        while f <= i:
            print(i, end=' ')
            i -= p
            sleep(.5)
    print('FIM!', end='')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
print('='*40)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
passo = int(input('Passo:  '))
contador(ini, fim, passo)
