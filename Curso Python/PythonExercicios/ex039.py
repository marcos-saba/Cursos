from datetime import date
ano = int(input('Qual o ano de nascimento? '))
print('Qual o seu sexo? \n [1] Masculino  [2] Feminino')
gen = int(input('RESPOSTA: '))
atual = int(date.today().year)
idade = (atual - ano)
if 1850 > ano or ano > atual:
    print('\033[1;33m Há um erro no seu ano de nascimento. Tente novamente.'.upper())
elif gen == 2:
    print('Você é do sexo feminino e está dispensada do alistamento obrigatório.')
elif gen != 1 and gen != 2:
    print('\033[1;31mOPÇÃO INVÁLIDA! TENTE NOVAMENTE.\033[m')
elif idade < 18:
    print(f'Sua idade é de \033[1;34m{idade}\033[m anos.')
    print(f'\033[1;30mAINDA\033[m faltam {(18-idade)} anos para você se alistar no serviço militar.')
    print(f'Seu alistamento será em {(18-idade) + atual}.')
elif idade == 18:
    print(f'Sua idade é de \033[1;34m{idade}\033[m anos.')
    print('\033[1;33mEstá na hora de você se alistar\033[m!!')
elif idade > 18:
    print(f'Sua idade é de \033[1;34m{idade}\033[m anos.')
    print('Você já passou do tempo de alistamento.')
    print(f'Seu alistamento foi no ano de {(atual) - (idade - 18) }.')

