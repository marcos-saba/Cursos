from time import sleep
print('\033[33m_ _ _'*8)
print('\033[33m_-_-_\033[m'*8)
print('\033[30mDigite dois valores:')
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
escolha = 0
sleep(0.3)
while escolha != 5:
    print('---'*5)
    escolha = int(input('''Aperte:
 [ 1 ] somar
 [ 2 ] multiplicar
 [ 3 ] maior 
 [ 4 ] novos números
 [ 5 ] sair do programa \nSua escolha: '''))
    print('---'*5)
    sleep(0.4)
    if escolha == 1:
        soma = n1 + n2
        print(f'Você selecionou a opção\033[36m {escolha}.\033[30m '
              f'\nA soma entre \033[32m{n1}\033[30m e \033[32m{n2} \033[30mvale \033[33m{soma}\033[30m.')
    elif escolha == 2:
        mult = n1 * n2
        print(f'Você selecionou a opção \033[36m{escolha}\033[30m. '
              f'\nA multiplicação entre \033[32m{n1}\033[30m e \033[32m{n2}\033[30m vale \033[33m{mult}\033[30m.')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Você selecionou a opção\033[36m {escolha}.\033[30m '
              f'\nO maior valor entre \033[32m{n1}\033[30m e \033[32m{n2}\033[30m é o \033[33m{maior}\033[30m')
    elif escolha == 4:
        n1 = float(input('Digite os novos valores: \nPrimeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif escolha == 5:
        print(f'Você selecionou a opção \033[36m{escolha}\033[30m. \nO programa será encerrado.')
        print('\033[33mEncerrando ', end='')
        for c in range(0, 5):
            print('.', end='')
            sleep(0.5)
        print('')
        print('\033[30m__' * 19)
        print('\033[30mO programa foi encerrado com sucesso!')
    else:
        print('\033[31mOpção inválida. Tente novamente. \033[30m')
