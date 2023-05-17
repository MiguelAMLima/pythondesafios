# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# (Fazer com while e com for)
"""num = int(input('Digite um número inteiro para calcular seu fatorial: '))
fatorial = num
multiplicador = num - 1
while multiplicador >= 1:
    fatorial = fatorial * multiplicador
    multiplicador -= 1
print(f'O fatorial de {num} é {fatorial}')"""

num = int(input('Digite um número inteiro para calcular seu fatorial: '))
fatorial = num
for multiplicador in range(num - 1, 0, -1):
    fatorial = fatorial * multiplicador
print(f'O fatorial de {num} é {fatorial}')
