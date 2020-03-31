print(f'\033[30m{" LOJAS JOÃO DA SILVA ":#^40}')

preco = float(input('\033[30mPreço do produto: R$ '))
print('''Qual a forma de pagamento? 
[ 1 ] à vista dinheiro/cheque 
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão  
[ 4 ] 3x ou mais no cartão''')
forma = int(input('Qual opção: '))
if forma == 1:
    pg = preco - (preco * 10 / 100)
    print(f'Preço à vista com \033[33m10% \033[mde desconto: \033[34mR${pg:.2f}. ')
elif forma == 2:
    pg = preco - (preco * 5 / 100)
    print(f'Preço à vista com \033[33m5% \033[mde desconto: \033[34mR${pg:.2f}.')
elif forma == 3:
    pg = preco
    print(f'Valor das parcelas em \033[33m2x s/juros: \033[34mR$ {pg/2:.2f}\033[m')
    print(f'\033[30mPreço final à prazo \033[33ms/juros\033[m em \033[33m2x no cartão\033[m: \033[30mR${pg:.2f}.')
elif forma == 4:
    pg = preco + (preco * 20 / 100)
    p = int(input('Quantas parcelas? '))
    print(f'Sua compra será parcelada em \033[33m{p} x\033[m de\033[33m R${(pg/p):.2f}\033[m.')
    print(f'\033[30mPreço final\033[33m com juros: \033[32mR${pg:.2f}.')
else:
    print('\033[1;31mOpção inválida!')
