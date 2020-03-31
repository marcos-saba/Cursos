
casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual é o seu salário? R$ '))
ano = int(input('Em quantos anos você pretende pagar? '))
parcela = casa/(ano*12)
cores = {'limpa': '\033[1;30m',}
print(f'Seu salário é de R${sal:.2f}.')
if parcela <= sal*30/100:
    print(f'Seu empréstimo foi \033[1;34mAPROVADO\033[m!! '
          f'\nO valor da sua parcela será de \033[1;34mR${parcela:.2f}\033[m em \033[33m{ano*12}\033[m vezes.')
elif parcela > sal*30/100:
    print(f'Infelizmente seu impréstimo \033[1;31mNÃO FOI APROVADO\033[m.'
          f'\nO valor das parcelas será de \033[1;31mR${parcela:.2f}\033[m '
          f'e excede \033[1;33m30%\033[m do seu salário.')
