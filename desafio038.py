# Escreva um programa que leia dois números e compare-os, mostrando na
# tela uma mensagem: -O primeiro valor é maior; -O segundo valor é maior;
# -Não existe valor maior, os dois são iguais.
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))
if num1 > num2:
    print('Valor 1: {}\nValor 2: {}\nO primeiro valor é maior.'.format(num1, num2))
elif num2 > num1:
    print('Valor 1: {}\nValor 2: {}\nO segundo valor é maior.'.format(num1, num2))
else:
    print('Valor 1: {}\nValor 2: {}\nNão existe valor maior, os dois são iguais.'.format(num1, num2))
