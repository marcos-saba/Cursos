print('+++ Digite três números diferentes +++')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
'''if n1 == n2 and n1 == n3:
    print('Os números são iguais!!')
if n1 >= n2 and n1 >= n3:
    print(f'O maior número é {n1}.')
if n2 > n1 and n2 >= n3:
    print(f'O maior número é {n2}.')
if n3 > n2 and n3 > n1:
    print(f'O maior número é {n3}.')
if n1 <= n2 and n1 <= n3:
    print(f'O menor número é {n1}.')
if n2 < n1 and n2 <= n3:
    print(f'O menor número é {n2}.')
if n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}.')'''
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'Maior: {maior} ')
print(f'Menor: {menor}')



