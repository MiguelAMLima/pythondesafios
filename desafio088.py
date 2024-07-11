# Faça um programa que ajude um jogador da mega sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear
# 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
# composta.
from random import randint
from time import sleep
print('-' * 31)
print(f'{"MEGA SENA":^31}')
print('-' * 31)
jogos = []
lista = []
tot = 1
quant = int(input('Quantos jogos você quer sortear? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('\n', '-=' * 5, f'SORTEANDO {quant} JOGOS', '-=' * 5, '\n')
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('\n', '-=' * 6, '< BOA SORTE! >', '-=' * 6)
