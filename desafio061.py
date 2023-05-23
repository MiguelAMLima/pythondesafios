# Refaça o desafio051, lendo o primeiro termo e a razão de uma P.A., mostrando
# os 10 primeiros termos da progressão usando a estrutura while.
print('-=' * 10, end='-\n')
print(f'{"Gerador de P.A.":^21}')
print('-=' * 10, end='-\n')
primeiro = int(input('\nInforme o primeiro termo: '))
razao = int(input('Informe a razão da P.A.: '))
termo = primeiro
cont = 1
print('')
while cont <= 10:
    print(f'{termo}', end=' ➟ ')
    termo += razao
    cont += 1
print('FIM')
