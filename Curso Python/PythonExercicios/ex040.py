print('+='*5, '\033[1;4;30mCÁLCUCLO DE MÉDIA\033[m', '+='*5)
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('\033[30mMÉDIA: 5.0\033[m \033[33m\nRECUPERAÇÃO: 5.0 e 6.9\033[m \033[34m\nAPROVADO: 7.0\033[m')
if media < 5.0:
    print(f' Sua média foi \033[1;4;31m{media:.1f}.\n Você foi REPROVADO\033[m.')
elif 7 > media >= 5:
    print(f' Sua média foi \033[1;4;33m{media:.1f}\033[m.\n Você está de \033[1;4;33mRECUPERAÇÃO\033[m')
else:
    print(f' Sua média foi \033[1;4;34m{media:.1f}\033[m.'
          f'\n \033[1;36mPARABÉNS!!\033[m Você foi \033[1;4;34mAPROVADO!\033[m')
