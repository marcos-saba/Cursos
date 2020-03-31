from datetime import date
print('Digite o ano de nascimento das sete pessoas:')
maior = 0
menor = 0
c = 0
for c in range(0, 7):
    ano = int(input(f'{c + 1}° pessoa: '))
    idade = (date.today().year) - ano
    if ano > (date.today().year) or ano < 1870:
        print('\033[31mANO INVÁLIDO. TENTE NOVAMENTE.')
        break
    else:
        if idade >= 21:
            maior += 1
        else:
            menor += 1
if c < 6:
    print('')
else:
    print(f'Pessoas que atingiram a maior idade: {maior}\nPessoas que ainda não atingiram a maior idade: {menor}')
