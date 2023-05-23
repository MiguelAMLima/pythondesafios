# Escreva um programa que leia um número n inteiro qualquer e mostre na tela
# os n primeiros elementos de uma sequência de Fibonacci.
print('-=' * 11)
print(f'{"Sequência de Fibonacci":^22}')
print('-=' * 11)
n = int(input('Digite quantos elementos deseja calcular: '))
print('')
antecessor1 = 1
antecessor2 = 0
print(f'{antecessor2} ➟ {antecessor1}', end=' ➟ ')
cont = 3
while cont <= n:
    termo = antecessor1 + antecessor2
    antecessor2 = antecessor1
    antecessor1 = termo
    cont += 1
    print(f'{termo}', end=' ➟ ')
print('FIM')
