valores = list()
print('\033[30m='*50)
for c in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {c}: ')))
print('='*50)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == max(valores):
        print(p, end='... ')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for p, v in enumerate(valores):
    if v == min(valores):
        print(p, end='... ')
print()
print('='*50)
