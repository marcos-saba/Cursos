lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#print(lanche)

for cont in range(0, len(lanche)):# forma completa c/ posiçào
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-'*38)
for comida in lanche:# forma simples s/ posição.
    print(f'Eu vou comer {comida}')
print('-'*38)
for pos, comida in enumerate(lanche):# forma complexa c/ posição
    print(f'Eu vou comer {comida} na posição {pos}')
print('-'*38)
print('Comi pra caramba!')
print('='*25)
print('Normal:')
print(lanche)
print('-'*25)
print('Ordem alfabética:')
print(sorted(lanche))