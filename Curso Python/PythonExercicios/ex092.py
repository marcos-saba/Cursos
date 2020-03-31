from datetime import date
print('\033[30m-'*42)
dado = dict()
dado['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
dado['idade'] = date.today().year - ano
dado['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dado['ctps'] != 0:
    dado['contratação'] = int(input('Ano de contratação: '))
    dado['salário'] = float(input('Salário: R$ '))
    dado['aposentadoria'] = (dado['contratação'] + 35) - ano
print('='*42)
for i, d in dado.items():
    print(f'\033[34m{i} \033[30mtem o valor \033[33m{d}\033[30m')
print('-'*42)