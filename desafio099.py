# Faça um programa que tenha uma função maior(), que receba
# vários parâmetros com valores inteiros. Seu programa tem
# que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(val):
    cont = m = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in val:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            m = valor
        else:
            if valor > m:
                m = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}')


valores = list()
i = 1
while True:
    v = int(input(f'Digite o {i}º valor [-1 para interromper]: '))
    if v == -1:
        break
    valores.append(v)
    i += 1
maior(valores)
