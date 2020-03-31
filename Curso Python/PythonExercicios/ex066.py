cont = s = 0
while True:
    n = int(input('\033[30mDigite um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Foram digitados \033[32m{cont}\033[30m valor(es) e a soma entre eles vale \033[33m{s}\033[m.')
