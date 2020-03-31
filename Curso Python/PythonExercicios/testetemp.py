from time import sleep
from random import choice
cores = {'roxo': '\033[1;4;35m',
         'clear': '\033[m',
         'verde': '\033[1;32m',
         'vermelho': '\033[1;31m',
         'neg': '\033[1;30m'}
print('{}='.format(cores['neg'])*15, ' > {}JOKENPÔ{} < '.format(cores['roxo'], cores['neg']), '='*15)
ppt = ['PEDRA', 'PAPEL', 'TESOURA']
res = choice(ppt)
jogada = str(input('{}Escolha pedra, papel ou tesoura: '.format(cores['neg']))).strip().upper()
# Repetindo o input para respostas não válidas:
while not jogada in ppt:
    print('{}Sua resposta não é válida, tente novamente !'.format(cores['neg']))
    jogada = str(input('{}Escolha pedra, papel ou tesoura: '.format(cores['neg']))).strip().upper()
print('{}PROCESSANDO ...'.format(cores['neg']))
sleep(1.3)
if res == ppt[0] and jogada == ppt[1]:
    print('{}Parabéns, você venceu !!{} Eu joguei {} !!'.format(cores['verde'], cores['neg'], res.title()))
elif res == ppt[1] and jogada == ppt[2]:
    print('{}Parabéns, você venceu !!{} Eu joguei {} !!'.format(cores['verde'], cores['neg'], res.title()))
elif res == ppt[2] and jogada == ppt[0]:
    print('{}Parabéns, você venceu !!{} Eu joguei {} !!'.format(cores['verde'], cores['neg'], res.title()))
elif res == jogada:
    print('EMPATE')
else:
    print('{}Você perdeu !! {}Eu joguei {}.'.format(cores['vermelho'], cores['neg'], res.title()))

