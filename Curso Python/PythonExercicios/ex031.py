d = float(input('Qual a distância da viagem (km)? '))
if d <= 200:
    print(f'A passagem custará R${d*.50:.2f}.')
else:
    print(f'A passagem custará R${d*.45:.2f}.')
#preço = distância = 0.50 if distância <=200 else distância * 0.45
