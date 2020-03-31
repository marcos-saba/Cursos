def leiaDinheiro(msg):
    while True:
        num = str(input(msg).strip().replace(',', '.'))
        cont = 0
        if num.count('.') > 1:
            cont -= 1
        for c, p in enumerate(num):
            if p.isnumeric():
                cont += 1
            if p == '.':
                cont += 1
        if cont == len(num) and len(num) > 0 and num != '.':
            break
        else:
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
    return float(num)


def teste(msg):
    while True:
        num = str(input(msg).strip().replace(',', '.'))
        t = num.count('.')
        if t <= 1 and num.replace('.', '0').isnumeric() and num != '.':
            break
        else:
            print(f'\033[31mERRO: "{num}" é um preço inválido!\033[m')
    return float(num)
