from random import sample
from time import sleep
print('\033[30m-'*40)
print(f'\033[1;32m{"JOGO DA MEGA SENA":^40}\033[m')
print('\033[30m-'*40)
qt_jogo = int(input('Quantos jogos você quer que eu sorteie? '))
jogos = 1
jogo = []
if qt_jogo <= 0:
    print('\033[31mNenhum jogo será sorteado!')
else:
    print()
    print('='*9, f' \033[33mSORTEANDO {qt_jogo} JOGOS\033[30m ', '='*9)
print()
while jogos <= qt_jogo:
    jogo = sample(range(1, 61), 6)
    jogo.sort()
    print(f'\033[30mJogo {jogos:2}: \033[34m{jogo}')
    jogos += 1
    sleep(0.7)
print()
print(f'\033[30m{" BOA SORTE! ":-^40}')
#lista = []
#cont = 0
#whle True:
    #num = rendint(1, 60)
    #if num not in lesta:
        #lista.append(num)
        #cont += 1
    #if cont >= 6:
        #break
