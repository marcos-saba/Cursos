r = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
while r not in 'MF':
    r = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print(f'Sexo {r} registrado com sucesso! ')

