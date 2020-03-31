print('\033[30m='*40)
aluno = {'nome': str(input('Nome: '))}
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-'*40)
print(f'   - Nome é igual a {aluno["nome"].capitalize()}')
print(f'   - Média é igual a {aluno["média"]:.1f}')
print(f'   - Situação é igual a {aluno["situação"]}')
print('='*40)
