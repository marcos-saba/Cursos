print('='*5, 'Conversor', '='*5)
m = int(input('Digite uma distância em metros: '))
print(' A distância digitada foi: {}(m). \n Distância em centímetros: {}(cm). \n Distância em milímetro: {}(mm).'.format(m, m*100, m*1000))
print(f' Distância em quilômetros: {m/1000}(km).')
print(f' Distância em hectômetro: {m/100}(hm). \n Distância em decâmetro: {m/10}(dam).')
print('='*10, '+++', '='*10)
#km=1000m, hm=100m, dam=10m, cm=0.01m, mm=0.001m