print('\033[30m')
'''p1 = float(input('Primeiro peso(kg): '))
p2 = float(input('Segundo peso(kg): '))
p3 = float(input('Terceiro peso(kg): '))
p4 = float(input('Quarto peso(kg): '))
p5 = float(input('Quinto peso(kg): '))
if p2 < p1 > p3 and p4 < p1 > p5:
    maior = p1
elif p1 < p2 > p3 and p4 < p2 > p5:
    maior = p2
elif p1 < p3 > p2 and p4 < p3 > p5:
    maior = p3
elif p1 < p4 > p2 and p3 < p4 > p5:
    maior = p4
else:
    maior = p5
if p2 > p1 < p3 and p4 > p1 < p5:
    menor = p1
elif p1 > p2 < p3 and p4 > p2 < p5:
    menor = p2
elif p1 > p3 < p2 and p4 > p3 < p5:
    menor = p3
elif p1 > p4 < p2 and p3 > p4 < p5:
    menor = p4
else:
    menor = p5'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso foi \033[34m{maior:.1f} kg\033[m \033[30me o menor peso foi \033[32m{menor:.1f} kg.')



