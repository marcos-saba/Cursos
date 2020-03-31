lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livros', 34.9)
cont = 0
cont2 = 1
print('\033[30m-' * 40)
print(f'\033[36m{"LISTAGEM DE PREÇOS":^40}\033[30m')
print('-' * 40)
for c in range(0, len(lista)):
    if cont <= len(lista) and cont2 <= len(lista):  # if c % 2 == 0
        print(f'\033[30m{lista[cont]:.<30}R$\033[33m{lista[cont2]:>7.2f}\033[m')
    cont += 2
    cont2 += 2
print('\033[30m-' * 40)
