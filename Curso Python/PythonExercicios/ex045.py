from random import randint
from time import sleep
print('-'*40)
print('=+'*5, '\033[1;4;32mJOKENPÔ\033[m', '+='*5)
print('\033[30mOpções:\033[m')
print('\033[32mpedra [0]\033[m, \033[30mpapel [1]\033[m, \033[36mtesoura [2]\033[m: ')
jogador = int(input('\033[30mSua escolha: \033[m'))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
cpu = randint(0, 2)
cores = {"limpa": '\033[m',
         "azul": '\033[34m',
         "amarelo": '\033[33m',
         "pretoebranco": '\033[7;30m',
         "vermelho": '\033[31m'}
if jogador != 0 and jogador != 1 and jogador != 2:
    print(f'{cores["vermelho"]} OPÇÃO INVÁLIDA! TENTE NOVAMENTE.{cores["limpa"]}')
else:
    print('\033[34mJO...\033[m')
    sleep(0.5)
    print('\033[33mKEN...\033[m')
    sleep(0.5)
    print('\033[1;36mPÔ!!!\033[m')
    sleep(0.1)
    print('='*22)
    if jogador == 0:
        print(f'\033[30mVOCÊ: \033[4;32m{itens[jogador]}\033[m')
    elif jogador == 1:
        print(f'\033[30mVOCÊ: \033[4;30m{itens[jogador]}\033[m')
    elif jogador == 2:
        print(f'\033[30mVOCÊ: \033[4;36m{itens[jogador]}\033[m')
    if cpu == 0:
        print(f'\033[30mCOMPUTADOR: \033[4;32m{itens[cpu]}\033[m')
    elif cpu == 1:
        print(f'\033[30mCOMPUTADOR: \033[4m{itens[cpu]}\033[m')
    elif cpu == 2:
        print(f'\033[30mCOMPUTADOR: \033[4;36m{itens[cpu]}\033[m')
    print('='*22)
    if jogador == 0 and cpu == 1 or jogador == 1 \
            and cpu == 2 or jogador == 2 and cpu == 0:
        print('#'*3, '\033[1;31mVOCÊ PERDEU!\033[m', '#'*3)
    elif jogador == 0 and cpu == 2 or jogador == 1 \
            and cpu == 0 or jogador == 2 and cpu == 1:
        print('#'*3, '\033[1;33mVOCÊ GANHOU!!\033[m', '#'*3)
    elif jogador == cpu:
        print('##'*3, '\033[1;30mEMPATE!\033[m', '##'*3)
print('-'*40)






