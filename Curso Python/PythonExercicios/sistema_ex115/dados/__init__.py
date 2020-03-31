from sistema_ex115 import interface


def mostrarCadastro():
    try:
        ficha = open('Ficha_de_Cadastro.txt', 'r')
        interface.texto('PESSOAS CADASTRADAS')
        print('\033[30m', end='')
        print(ficha.read())
    except FileNotFoundError:
        print('\033[33mAinda não existe pessoas Cadastradas.')
        print('Tente a Opção "2".\033[m')


def cadastrar():
    interface.texto('NOVO CADASTRO')
    ficha = open('Ficha_de_Cadastro.txt', 'a')
    print('\033[30m', end='')
    nome = str(input('Nome: '))
    idade = interface.leiaInt('\033[30mIdade: ')
    ficha.write(f"{nome:<30}\t\t{idade} anos\n")
    print(f'\033[30mNovo registro de {nome} foi adicionado com sucesso!.')
    ficha.close()
