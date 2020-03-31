from random import randint
from time import sleep
print('\033[30m=+' * 10, '\033[1;33m JOGO DA ADIVINHAÇÃO\033[m ', '\033[30m+=' * 10)
print('\033[31m---\033[m' * 21)
print('\033[30mO computador vai escolher um número entre'
      '\033[1;32m 0\033[m \033[30me \033[1;32m10\033[m\033[30m, tente acertar: ')
for d in range(0, 63):
    print('\033[30m_', end='')
    sleep(0.07)
print('')
print('O computador está escolhendo um número ', end='')
for c in range(0, 5):
    print('.', end='')
    sleep(0.4)
cpu = randint(0, 10)
tentativas = 0
acertou = False
player = ''
print('')
print('Pronto!')
sleep(0.01)
while not acertou:
    print('\033[30m==' * 12)
    player = int(input('\033[30mSeu palpite: '))
    tentativas += 1
    for c in range(0, 5):
        print('\033[30m. \033[m', end='')
        sleep(0.3)
    if player == cpu:
        acertou = True
    else:
        if player < cpu:
            print('')
            print('\033[30m==' * 12)
            print('\033[30mMais... Tente de novo. ')
        elif player > cpu:
            print('')
            print('\033[30m==' * 12)
            print('Menos... Tente de novo. ')
print('')
print('\033[30m==' * 12)
print('\033[31m---\033[m' * 21)
if tentativas == 1:
    print(f'\033[1;33mNOSSA!! Você é incrível, acertou de primeira!!!\033[m')
elif 1 < tentativas < 5:
    print(f'\033[1;34mWOW!! PARABÉNS!!! \033[33mVocê conseguiu acertar o número '
          f'\nem apenas\033[1;36m {tentativas} \033[33mtentativas!')
elif 5 <= tentativas < 10:
    print(f'\033[1;33mUhm... PARABÉNS!! \033[34mVocê conseguiu adivinhar o número '
          f'\nem menos de \033[33m10\033[m \033[34mtentativas. Você precisou só de \033[1;32m{tentativas}\033[34m!')
else:
    print(f'\033[1;32mUfa! Finalmente você conseguiu adivinhar o número, parabéns! '
          f'\nLevou \033[36m{tentativas} \033[32mtentativas, mas tudo bem. Mais sorte da próxima!')
print('\033[31m---' * 21)
print(f'\033[30mVocê:\033[1;34m {player} \n\033[30mCPU:\033[1;32m {cpu}')
