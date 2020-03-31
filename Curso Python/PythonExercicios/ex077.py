palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado',
            'programador', 'futuro')
print('\033[30m-'*38)
print(f'\033[33m{"VERIFICADOR DE VOGAIS":^38}\033[30m')
print('-'*38)
for palavra in palavras:
    print(f'\033[30m\nNa palavra \033[34m{palavra.upper():^12}\033[30m temos \033[36m', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
print('')
print('\033[30m-'*38)
