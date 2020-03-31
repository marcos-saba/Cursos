print('\033[30m#'*10, ' PARES', '#'*10)
print(f'Os pares entre 1 e 50 são: ')
for c in range(2, 51, 2):
    print(f'\033[36m{c} ', end='')
