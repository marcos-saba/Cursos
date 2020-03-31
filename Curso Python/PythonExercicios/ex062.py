print('\033[30m=+'*10, ' GERADOR DE PA 2.0 ', '+='*10)
ptermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
pa = ptermo
contagem = 1
resposta = 10
tot = 0
print(f'PA do número {ptermo}(10 termos): \nINÍCIO -> ', end='')
while resposta != 0:
    tot += resposta
    while contagem <= tot:
        print('\033[33m', pa, end=' -> ')
        pa += razao
        contagem += 1
    print('\033[30mPAUSA')
    resposta = int(input('\033[30mMais quantos termos? '))
print(f'PA total do número {ptermo}:\nINÍCIO=>', end='')
contagem = 1
while contagem <= tot:
    print('\033[33m', ptermo, end='=> ')
    ptermo += razao
    contagem += 1
print('\033[30mFIM')
print('\033[30m___'*21)
print(f'PA finalizada com o total de {tot} termos.')
print('==='*21)