def cores(e=0, e1=0, e2=0, c=0, f=0, b=False, limpa=False):
    """
    -> Função para aplicar cores no terminal.
    cores(1, 4, 7, c=30, f=40, b=True)
    cores(1, c=30); cores(1, 4, c=30)
    cores(1, 4, 7, c=30); cores(c=30)
    cores(limpa=True); cores(f=40, b=True)
    :param e: seleciona o estilo do texto (0, 1, 4, 7)
    :param e1: estilo opcional.(0, 1, 4, 7).
    :param e2: estilo opcional.(0, 1, 4, 7).
    :param c: seleciona a cor do texto (30 - 37). obs.: sempre declarar.(c=)
    :param f: seleciona a cor de fundo do texto (40 - 47).osb.: caso param b=True, sempre declarar(f=)
    :param b: opcional, aplica ou não o fundo (False/True)
    :param limpa: limpa as cores aplicadas (opcional - False/True).
    :return: cor e estilo selecionada.
    """
    if b:
        print(f'\033[{e};{c};{f}m', end='')
        if e1 > 0:
            print(f'\033[{e};{e1};{c};{f}m', end='')
        if e2 > 0:
            print(f'\033[{e};{e1};{e2};{c};{f}m', end='')

    elif limpa:
        print('\033[m', end='')
    else:
        print(f'\033[{e};{c}m', end='')
        if 0 < e1 < 30:
            print(f'\033[{e};{e1};{c}m', end='')
        if 0 < e2 < 30:
            print(f'\033[{e};{e1};{e2};{c}m', end='')


def cor(e=0, c=0, f=0, msg=''):
    print(f'\033[{e};{c};{f}m', end='')
    print(msg, end='')
    print(f'\033[m', end='')


