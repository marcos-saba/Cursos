listao = [[], []]
for c in range(0, 7):
    v = (int(input(f'Digite o {c+1}° valor: ')))
    if v % 2 == 0:
        listao[0].append(v)
    else:
        listao[1].append(v)
listao[0].sort()
listao[1].sort()
print('='*50)
print(f'Os valores pares digitados foram: {listao[0]}')
print(f'Os valores ímpares digitados foram: {listao[1]}')
