# Escreva um programa que pergunte o salário de um funcionário e calcule o
# valor do seu aumento. Para salários superiores a R$1.250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Digite o valor do salário do funcionário: R$'))
if salario > 1250.00:
    print('O aumento do seu salário será de R${}\nSeu novo salário é de R${}'
          .format((0.1 * salario), salario + (0.1 * salario)))
else:
    print('O aumento do seu salário será de R${}\nSeu novo salário é de R${}'
          .format((0.15 * salario), salario + (0.15 * salario)))
