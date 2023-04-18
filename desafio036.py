# Escreva um programa para aprovar o empréstimo bancário para a compra de uma
# casa. O programa vai perguntar o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# não pode exceder 30% do salário ou então o empréstimo será negado.
print('Bem-vindo ao programa de análise de empréstimos, para começar:')
valor = float(input('Informe o valor da casa que deseja comprar: '))
salario = float(input('Informe o salário do comprador: '))
tempo = int(input('Informe em quantos anos deseja pagar: '))
prestacao = valor / (tempo * 12)
if prestacao > ((30 / 100) * salario):
    print('O valor da prestação mensal foi de R$:{:.2f} e ultrapassou 30% do seu salário,'
          ' portanto seu empréstimo foi negado!'.format(prestacao))
else:
    print('Seu empréstimo foi aprovado! o valor da prestação mensal será de R$:{:.2f}'.format(prestacao))
