print('\033[30m='*5, ' BANCO DOS DESESPERAODS ', '='*5)
print('-'*33)
valor = int(input('Que valor você quer sacar? R$'))
tot = valor
c = 50
totc = 0
print('-'*33)
while True:
    if tot >= c:
        tot -= c
        totc += 1
    else:
        if totc > 0:
            print(f'Total de {totc} cédulas de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        totc = 0
        if tot == 0:
            break
print('-'*33)
print('Obrigado por usar o Banco DSP! \nVolte smepre que estiver desesperado!')