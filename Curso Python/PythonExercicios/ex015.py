d = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pg = (d * 60 + km * 0.15)
print(f'Dias alugados: {d}.\nKm rodados: {km} Km.')
print(f'O total a ser pago pelo aluguel do carro é de R${pg:.2f}.')



