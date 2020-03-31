sa = float(input('Qual o salário? R$ '))
if sa > 1250.00:
    print(f'O salário com aumento de 10% será de R${sa + (sa*10/100):.2f}.')
else:
    print(f'O salário com aumento de 15% será de R$ {sa + ( sa*15/100):.2f}')


