r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if (r2-r3) < r1 < (r2+r3) and (r1-r3) < r2 < (r1+r3) and (r1-r2) < r3 < (r1+r2):
    print('As três retas PODEM formar um triângulo.')
else:
    print('As três retas NÃO PODEM forma um triângulo')