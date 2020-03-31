media = 0
soma = 0
mulher = 0
maior = 0
velho = ''
for p in range(1, 5):
    print('-'*5, f' {p}° PESSOA ', '-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    soma += idade
    media = soma/4
    if p == 1 and sexo in 'M': # está incompleto!!
        maior = idade
        velho = nome
    if sexo in 'M' and idade > maior:
        maior = idade
        velho = nome
    if idade < 20 and sexo == 'F':
         mulher += 1
print(f'A média das idades do grupo foi {media} anos.')
print(f'Mulheres com menos de 20 anos: {mulher}')
print(f'Nome do homem mais velho: {velho.upper()}.')
