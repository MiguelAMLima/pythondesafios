# Faça um algoritmo que leia o salário de um
# funcionário e mostre seu novo salário, com
# 15% de aumento.
sal = float(input('Qual o salário do funcionário? R$:'))
aum = sal + ((15/100) * sal)
print('Seu novo salário com 15% de aumento é R${:.2f}'.format(aum))
