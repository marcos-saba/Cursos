print('\033[30m==='*11)
print('SOMA DE VALORES ALEATÓRIOS')
print('==='*11)
r = int(input('Digite um número inteiro (999 para parar): '))
cont = 0
s = r
while r != 999:
    r = int(input('Digite outro número (999 para parar): '))
    cont += 1
    if r != 999:
        s += r
print('==='*10)
if cont == 0 and s == 999:
    s = 0
    print(f'Foram digitados {cont} valor(es) e a \nsoma entre ele(s) vale {s}.')
else:
    print(f'Foram digitados {cont} valor(es) e a \nsoma entre ele(s) vale {s}.')
print('==='*11)
print('Fim.')
print('==='*11)
