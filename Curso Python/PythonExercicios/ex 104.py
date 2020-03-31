def leiaInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            return int(num)
        else:
            print('\033[31mERRO! O valor digitado não é um número.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}.')

ok = False
valor = 0
# resposta alternativa:
'''while True:
    n = str(input(msg))
    if n.isnumeric():
        valor = int(n)
        ok = True
    else:
        print()
    if ok:
        break
return valor'''