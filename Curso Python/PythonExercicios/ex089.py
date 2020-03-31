from time import sleep
temp = list()
lista = []
print('\033[30m='*50)
print(f'\033[33m{" CADASTRO DE ALUNOS ":^50}\033[30m')
print('='*50)
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])
    resp = ' '
    while resp not in 'NnSs':
        resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('='*50)
print(f'{"N°.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for p, v in enumerate(lista):
    print(f'\033[32m{p:<4}\033[30m{v[0].capitalize():10}\033[33m{v[2]:>8.1f}', end=' ')
    print()
print('\033[30m-'*35)
while True:
    while True:
        resp = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if resp < 0 or resp > len(lista)-1 and resp != 999:
            print('\033[31mOpção inválida! Tente novamente.\033[30m')
        else:
            break
    if resp == 999:
        break
    print(f'\033[30mNotas de {lista[resp][0].capitalize()} são \033[33m{lista[resp][1]}')
    print('\033[30m-'*35)
print('='*50)
print('FINALIZANDO', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(.5)
print(f'\n{"<<< FINALIZADO. VOLTE SEMPRE >>>":^50}')
print('='*50)
