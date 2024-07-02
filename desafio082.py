# Crie um programa que leia vários números e coloque-os em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores
# pares e os valores ímpares digitados, respectivamente. Ao final, mostre
# o conteúdo das 3 listas geradas.
num = list()
par = list()
impar = list()
while True:
    num.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 24)
print(f'A lista completa é: {num}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {impar}')
