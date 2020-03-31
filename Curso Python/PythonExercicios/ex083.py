print('\033[30m-'*35)
print('ANÁLISE DE EXPRESSÕES')
print('-'*35)
expr = str(input('Digite uma expressão: ')).strip()
lista = []
'''for c in range(0, len(expr)):
    lista.append(expr[c])
if lista.count('(') == lista.count(')') and '(' in lista[0] and ')' in lista[-1]:
    print('Sua expressão está válida')
else:
    print('Sua expressão está errada!')'''
print('-'*35)

for símb in expr:
    if símb == '(':
        lista.append('(')
    elif símb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
