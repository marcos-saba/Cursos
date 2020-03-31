num = (int(input('Digite um valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite mais outro valor: ')),
       int(input('Digite o último valor: ')))
print('-' * 36)
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if num.count(3) == 0:  # if 3 in num:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 foi digitado na {num.index(3) + 1}ª posição')
print('Os valores pares digitados: ', end='')
for v in num:
    if v % 2 == 0:
        print(v, end=' ')
print('')
print('-' * 36)
