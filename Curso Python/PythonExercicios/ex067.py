print('\033[30m='*11, ' \033[4;36mTABUADA INTERATIVA\033[m \033[30m', '='*11)
while True:
    n = int(input('Digite um número para mostrar a sua tabuada: '))
    print('-'*15)
    if n < 0:
        break
    for c in range(1, 11):
        t = n * c
        print(f'\033[33m{n}\033[30m  x {c:2} = \033[34m{t}\033[30m')
    print('-'*15)
print('\033[36mPrograma encerrado.')