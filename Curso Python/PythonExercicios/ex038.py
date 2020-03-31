n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O \033[1;33mPRIMEIRO VALOR\033[m é \033[1;34mmaior\033[m.')
elif n2 > n1:
    print('O \033[1;33mSEGUNDO VALOR\033[m é \033[1;34mmaior\033[m.')
else:
    print('Não \033[1;30mEXISTE\033[m valor maior, os dois valores são \033[1;34mIGUAIS\033[m.')
