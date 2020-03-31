#from math import hypot
import math
print('='*5, 'Cálculo triângulo retângulo', '='*5)
cat_op = float(input('Digite o comprimento do cateto oposto: '))
cat_adj = float(input('Digite o comprimento do cateto adjacente: '))
hip = math.hypot(cat_op, cat_adj)
print(f'O comprimento da hipotenusa do triângulo retângulo, cujos catetos são {cat_op:.2f} e {cat_adj:.2f} é {hip:.2f}.')
