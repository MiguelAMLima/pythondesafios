# Faça um programa que leia um número inteiro e diga se ele é ou não
# um número primo.
num = int(input('Informe um número inteiro: '))
divisor = 0
for c in range(1, num + 1):
    if num % c == 0:
        divisor = divisor + 1
if divisor == 2:
    print('O número informado é PRIMO!')
else:
    print('O número informado NÃO é PRIMO!')
