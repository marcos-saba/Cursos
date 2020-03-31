n = int(input('Digite um número: '))
print('[1] converter para binário\n[2] converter para octal \n[3] converter para hexadecimal')
c = int(input('Sua opção: '))
if c == 1:
    print(f'Binário: \033[1;30m{bin(n)[2:]}')
elif c == 2:
    print(f'Octal: \033[1;36m{oct(n)[2:]}')
elif c == 3:
    print(f'Hexadecimal: \033[1;33m{hex(n)[2:]}')
else:
    print('\033[31mOpção inválida!')
