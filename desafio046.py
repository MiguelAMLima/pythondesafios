# Faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de
# 1 segundo entre eles.
from time import sleep
print(f'\033[1;34m{" CONTAGEM REGRESSIVA ":=^41}\033[m')
for c in range(10, 0, -1):
    print(f'\033[1;35m{c:^40}\033[m')
    sleep(1)
print(f'\033[1;33m{"* POW! POW! POW! POW! POW! *":^41}\033[m')
