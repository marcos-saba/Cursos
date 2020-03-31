def notas(*nt, sit=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param nt: recebe uma ou mais notas dos alunos.
    :param sit: valor opcional, mostrando ou não a situação do aluno(True/False).
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('\033[30m-'*len(nt)*15)
    lnota = dict()
    lnota['total'] = len(nt)
    lnota['maior'] = max(nt)
    lnota['menor'] = min(nt)
    lnota['média'] = sum(nt) / len(nt)
    if sit:
        if lnota['média'] >= 7:
            lnota['situação'] = 'BOA'
        elif 5 < lnota['média'] < 7:
            lnota['situação'] = 'RAZOÁVEL'
        else:
            lnota['situação'] = 'RUIM'
    return lnota


resp = notas(7, 3, 5.5, 2, 9, 5, sit=True)
print(resp)
