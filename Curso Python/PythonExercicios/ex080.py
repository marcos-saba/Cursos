valores = list()
print('\033[30m-' * 50)
for p in range(0, 5):
    valor = (int(input('Digite um valor: ')))
    if p == 0 or valor > max(valores):
        valores.append(valor)
        print(f'Adicionado o valor \033[34m{valor}\033[30m no '
              f'\033[33mfinal\033[30m da lista...')
    else:
        for c in range(0, len(valores)):
            if valor <= valores[c]:
                valores.insert(c, valor)
                print(f'Adicionado o valor \033[34m{valor}\033[30m na '
                      f'\033[33m{c + 1}ª\033[30m posição na lista...')
                break
print('-' * 50)
print(f'Os valores digitados em ordem foram \033[33m{valores}\033[30m')
print('-' * 50)
'''lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-'*50)
print(f'Os valores digitados em ordem foram {lista}')'''
