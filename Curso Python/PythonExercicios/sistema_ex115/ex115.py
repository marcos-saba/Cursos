from sistema_ex115 import interface, dados
from time import sleep

while True:
    resp = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resp == 1:
        dados.mostrarCadastro()
    elif resp == 2:
        dados.cadastrar()
    elif resp == 3:
        break
    else:
        print('\033[31mOpção inválida! Escolha uma opção entre 1 e 3.\033[m')
    sleep(.5)
print('\033[30m-'*45)
print('Saindo do sitema', end='')
for c in range(0, 3):
    print('.', end='')
    sleep(.5)
print(' Até logo!')
print('-'*45)
