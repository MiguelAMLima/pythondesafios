# Desenvolva um programa que leia o primeiro termo e a razão de uma
# progressão aritmética. No final, mostre os 10 primeiros termos dessa
# progressão.
primeiro = int(input('Informe o primeiro termo da P.A.: '))
razao = int(input('Informe a razão da P.A.: '))
decimoprimeiro = primeiro + (10 * razao)
print('\nOs 10 primeiros termos da P.A. são:\n')
for c in range(primeiro, decimoprimeiro, razao):
    print(c, end=' → ')
print('FIM')
