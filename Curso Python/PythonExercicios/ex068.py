from random import randint, choice
print('\033[30m-+-'*15)
print('\033[33m=='*5, ' JOGO DO PAR OU ÍMPAR ', '=='*5)
print('\033[30m-+-'*15)
v = 0
while True:
    player = int(input('Digite um valor: '))
    esc_player = ' '
    while esc_player not in 'PI':
        esc_player = str(input('Par ou Ímpar? [P/I] ')).upper().strip()
    CPU = randint(0, 10)
    esc_CPU = choice(['P', 'I'])
    tot = player + CPU
    par = tot % 2
    if par == 0:
        print('---'*15)
        print(f'Você jogou \033[34m{player}\033[30m e o computador jogou '
              f'\033[33m{CPU}\033[30m. \nO total foi \033[36m{tot}\033[30m, DEU PAR.')
        print('---'*15)
    if par == 1:
        print('---'*15)
        print(f'Você jogou \033[34m{player}\033[30m e o computador jogou '
              f'\033[33m{CPU}\033[30m. \nO total foi \033[36m{tot}\033[30m, DEU ÍMPAR.')
        print('---'*15)
    if par == 0 and esc_player[0] == 'I' or par == 1 and esc_player[0] == 'P':
         print('\033[1;31mVOCÊ PERDEU!\033[m')
         break
    print('Você \033[1;33mGANHOU!!\033[m')
    print('\033[30mVamos de novo...')
    print('---'*15)
    v += 1
print('\033[30m-+-'*15)
print(f'\033[1;31mGAME OVER KID!! \033[30mvocê venceu \033[34m{v}\033[30m vez(es).')
