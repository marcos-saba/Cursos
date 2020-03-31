print('Digite seis valores inteiros:')
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'{c}° valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'A soma do(s) {cont} valor(es) par(es) vale {s}.')
