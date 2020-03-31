from datetime import date
print('=='*5, '\033[1;4;32mCLASSIFICAÇÃO DE ATLETAS\033[m', '=='*5)
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = int(atual - ano)

if 1850 > ano or ano > atual:
    print('\033[1;31mHÁ ERRO NO ANO DE NASCIMENTE. TENTE NOVAMENTE.\033[m')
else:
    print(f'Idade do atleta: \033[1;4;34m{idade}\033[m.')
if 9 >= idade > 0:
    print('Classificação do atleta: \033[33mMIRIN\033[m.')
elif 9 < idade <= 14:
    print('Classificação do atleta: \033[33mINFANTIL\033[m.')
elif 14 < idade <= 19:
    print('Classificação do atleta: \033[33mJUNIOR\033[m.')
elif idade == 20:
    print('Classificação do atleta: \033[33mSÊNIOR\033[m.')
elif idade > 20 and 1850 < ano < atual:
    print('Classificação do atleta: \033[33mMASTER\033[m.')
