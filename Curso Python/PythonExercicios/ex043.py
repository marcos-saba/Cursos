print('=+'*5, '\033[1;33mCÁLCULADORA IMC\033[m', '+='*5)
peso = float(input('Peso(kg): '))
altura = float(input('Altura(m): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    m = '\033[33mABAIXO DO PESO\033[m'
elif 18.5 <= imc < 25:
    m = '\033[34mPESO IDEAL\033[m'
elif 25 <= imc < 30:
    m = '\033[33mSOBREPESO\033[m'
elif 30 <= imc < 40:
    m = '\033[1;4;33mOBESIDADE\033[m'
else:
    m = '\033[1;4;31mOBESIDADE MÓRBIDA\033[m'
print(f'Seu peso: \033[35m{peso:.2f}\033[m '
      f'\nSua altura: \033[35m{altura:.2f}\033[m'
      f'\nSeu IMC: \033[35m{imc:.1f}\033[m, {m}')
