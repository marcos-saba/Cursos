print('\033[30m#'*8, 'TABUADA', '#'*8)
n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'\033[30m{n} x {c:2} = \033[32m{n*c}')
