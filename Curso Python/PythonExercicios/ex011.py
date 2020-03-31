print('='*5, 'Cálculo de tinta', '='*5)
print('')
alt = float(input('Digite a altura da parede em (m): '))
lar = float(input('Digite a largura da parede em (m): '))
are = float(alt*lar)
tin = 2
print('Altura da parede: {:.2f} (m). \nLargura da parede: {:.2f} (m).'.format(alt, lar))
print('Área da parede: {:.2f} (m²).'.format(are))
print('A quantidade de tinta necessária para pintar a parede será de {:.2f} (L).'.format(are/tin))
print('')
print('='*10, '+++++', '='*10)

