v1 = float(input('Qual a velocidade do carro (km/h)? '))
m = (v1 - 80)*7
if v1 > 80:
    print(f'Sua velocidade foi de {v1}km/h e está acima do limte de velocidade que é de 80km\h. \nVocê foi multado em R${m:.2f}.')
else:
    print('Tenha um bom dia! Dirija com segurança!')