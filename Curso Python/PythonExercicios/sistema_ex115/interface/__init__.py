def menu(lista):
    texto('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[30m - \033[34m{item}\033[m')
        c += 1
    print('\033[30m-' * 45)
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc


def texto(txt):
    print('\033[30m', end='')
    print('-'*45)
    print(f'{txt:^45}')
    print('-'*45)
    print('\033[m', end='')


def leiaInt(msg):
    while True:
        try:
            resp = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Valor digitado inválido.\033[m')
        else:
            break
    return resp
