from time import sleep


def titulo(msg):
    tam = len(msg) + 4
    print('=' * tam)
    print(f'  {msg}  ')
    print('=' * tam)
    sleep(1)
    cor('limpa')


def cor(cod):
    if cod == 'verde':
        print('\033[0;30;42m', end='')
    elif cod == 'limpa':
        print('\033[m', end='')
    elif cod == 'azul':
        print('\033[0;30;44m', end='')
    elif cod == 'branco':
        print('\033[7;30m', end='')
    elif cod == 'verm':
        print('\033[0;30;41m', end='')


def doc(sos):
    cor('azul')
    titulo(f"Acessando o manual do comando '{ajuda}'")
    cor('branco')
    help(sos)
    sleep(1)


while True:
    cor('verde')
    titulo('SISTEMA DE AJUDA PyHELP')
    ajuda = str(input('Função ou Biblioteca > ')).lower().strip()
    if ajuda == 'fim':
        break
    doc(ajuda)
cor('verm')
titulo('ATÉ LOGO')