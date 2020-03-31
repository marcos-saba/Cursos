def leiaInt(inteiro):
    while True:
        try:
            num = int(input(inteiro))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[31mERRO! Digite um número inteiro válido!\033[m')
        else:
            break
    return num


def leiaFloat(real):
    while True:
        try:
            num = float(input(real))
        except KeyboardInterrupt:
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[31mERRO!Digite um número real válido!\033[m')
        else:
            break
    return num


n = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {n} e o real foi {r:.1f}.')
