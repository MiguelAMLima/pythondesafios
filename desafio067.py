# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.
while True:
    num = int(input('Digite um número inteiro para ver sua tabuada [negativo encerra]: '))
    print('-' * 65)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 65)
print('Programa encerrado!')
