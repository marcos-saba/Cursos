print('\033[30m+*'*5, ' TESTE DE FRASES PALÍNDROMAS ', '*+'*5)
frase = str(input('Digite uma frase (sem acentos ou pontuações): ')).strip().upper().split()
frase = ''.join(frase)
'''if frase.count('.') > 0:
    print('\033[31mDIGITE A FRASE SEM PONTUAÇÕES. TENTE NOVAMENTE.')
elif frase == '' or frase == ' ':
    print('\033[31mVALOR INVÁLIDO. TENTE NOVAMENTE.')
else:
    print(f'O inverso de {frase} é {frase[::-1]}.')
    if frase == frase[::-1]:
        print('A frase digitada é um \033[34mPALÍDROMO.')
    else:
        print('A frase \033[33mNÃO\033[m é um \033[33mPALÍDROMO.')'''
inverso = ''
for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
if inverso == frase:
    print('Temos um \033[34mPALÍNDROMO!')
else:
    print('A frase digitada \033[33mNÃO\033[m \033[30mé um \033[33mPALÍNDROMO!')