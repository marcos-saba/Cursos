import random
print('='*5, 'SORTEIO DE ALUNOS', '='*5)
nome1 = str(input('Digite o nome do(a) primeiro aluno(a): '))
nome2 = str(input('Digite o nome do(a) segundo aluno(a): '))
nome3 = str(input('Digite o nome do(a) terceiro aluno(a): '))
nome4 = str(input('Digite o nome do(a) quarto aluno(a): '))
print(f'O(a) aluno(a) sorteado(a) foi {random.choice([nome1, nome2, nome3, nome4])}.')
#lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)

