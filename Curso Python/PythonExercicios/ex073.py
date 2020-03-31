lista_times = ('Palmeiras', 'Cruzeiro', 'Grêmio RS', 'Santos SP',
               'Corinthians', 'Flamengo', 'Atlético MG', 'Atlético PR',
               'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo',
               'Fluminense', 'Vasco da Gama', 'Bahia BA', 'Sport PE',
               'Vitória BA', 'Ponte Preta', 'América MG', 'Coritiba')
cont = 0
cont2 = 10
print('\033[30m-'*58)
print(f'\033[32m{"CLASSIFICAÇÃO CAMPEONATO BRASILEIRO 2019":^58}\033[30m')
print('-'*58)
for c in range(0, (len(lista_times)-10)):
    if cont <= len(lista_times) >= cont2:
        print(f'\033[33m{lista_times[cont]:.<20}{cont+1:3}ª{"":10}{lista_times[cont2]:.<20}{cont2+1:3}ª')
    cont += 1
    cont2 += 1
print('\033[30m='*58)
print(f'Os primeiros 5 colocados são:\033[33m {lista_times[0:5]}')
print('\033[30m='*58)
print(f'Os últimos 4 colocados são:\033[33m {lista_times[-4:]}')
print('\033[30m='*58)
print(f'Os times em ordem alfabética:\033[33m {sorted(lista_times)}')
print('\033[30m='*58)
print(f'O Chapecoense está na {lista_times.index("Chapecoense")+1}ª posição')
print('-'*58)