def voto(ano):
    from datetime import date
    i = date.today().year - ano
    if i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    elif 65 > i >= 18:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    else:
        if i >= 65 or 18 > i >= 16:
            return f'Com {i} anos: VOTO OPCIONAL'


print('-'*45)
nasc = int(input('En que ano você nasceu? '))
print(voto(nasc))
