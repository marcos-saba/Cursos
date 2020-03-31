numeral = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print('\033[30m-'*34)
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        print('Tente novamente. ', end='')
    if 0 <= num <= 20:
        print(f'Você digitou o número \033[33m{numeral[num].capitalize()}\033[30m.')
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()
            if resp[0] not in 'NS':
                print('Tente novamente. ', end='')
            if resp[0] in 'NS':
                break
        if resp[0] in 'N':
            break
print('-'*34)
print(f'{"FIM":^34}')
print('-'*34)
