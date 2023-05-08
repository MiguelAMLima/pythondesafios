# Faça um programa que leia um número inteiro e diga se ele é ou não
# um número primo.
num = int(input('Digite um número inteiro: '))
divisor = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[34m{c}\033[m', end=' ')
        divisor = divisor + 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if divisor == 2:
    print(f'\nO número {num} é PRIMO!')
else:
    print(f'\nO número {num} NÃO é PRIMO!')
