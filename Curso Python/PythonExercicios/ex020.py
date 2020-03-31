import random
al1 = input('Digite o nome do(a) primeiro(a) aluno(a): ')
al2 = input('Digite o nome do (a) segundo(a) aluno(a): ')
al3 = input('Digite o nome do(a) terceiro(a) aluno(a): ')
al4 = input('Digite o nome do(a) quarto(a) aluno(a): ')
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f'A ordem dos alunos para a apresentação será: \n{lista}.')
#from random import shuffle






