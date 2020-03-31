from random import randint
from time import sleep
print('Tente descobrir um número entre 0 e 5.')
n = randint(0, 5)
num = int(input('Seu palpite? '))
print('PROCESSANDO...')
sleep(1)
if n == num:
    print('Você venceu! PARABÉNS!!')
else:
    print(f'Você perdeu. O número era {n}. \nMais sorte da próxima vez!')
