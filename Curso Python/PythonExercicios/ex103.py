def ficha(n='<desconhecido>', g=0):
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


print('\033[30m-'*35)
nome = str(input('Nome do Jogador: ')).capitalize().strip()
gol = input('Número de Gols: ').strip()
if gol == '' and nome == '':
    print(ficha())
elif nome == '' and gol.isnumeric():
    print(ficha(g=int(gol)))
else:
    print(ficha(nome))
