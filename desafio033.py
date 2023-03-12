# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
lista = {num1, num2, num3}
lista_ordenada = sorted(lista)
print('O maior dos três números é {}'.format(lista_ordenada[2]))
print('O menor dos três números é {}'.format(lista_ordenada[0]))
