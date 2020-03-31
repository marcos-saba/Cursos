print('++'*5, '\033[1;36mANÁLISE DE TRIÂNGULOS\033[m', '++'*5)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print(f'Os \033[32mseguimentos\033[m formam um \033[4;36mtriângulo\033[m do tipo ', end='')
    if r1 == r2 == r3:
        print('\033[1;33mEQUILÁTERO.')
    #elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2:
     #   print('\033[1;33mISÓSCELES.')
    elif r1 != r2 != r3 != r1:
        print('\033[1;33mESCALENO.')
    else:
        print('\033[1;33mISÓSCELES.')
else:
    print(f'Os \033[32mseguimentos \033[1;4;31mNÃO\033[m formam um triângulo.')
