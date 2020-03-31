from time import sleep


def maior(*num):
    print('\033[30m='*50)
    print('A analisando os valores passados...')
    sleep(.5)
    for p, v in enumerate(num):
        print(f'\033[33m{v}', end=' ')
        sleep(.5)
    print(f'\033[30m\nForam informados \033[34m{len(num)}\033[30m valores ao todo.')
    print(f'O maior valor informado foi \033[36m{max(num)}\033[30m.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior(10, 5, 1, 0, 6, 23, 6, 0, 2)
