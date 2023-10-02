# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(1, 1000), randint(1, 1000), randint(1, 1000),
       randint(1, 1000), randint(1, 1000))
print(f'Valores gerados aleatoriamente: {num}'
      f'\nO maior valor da lista é: {max(num)}'
      f'\nO menor valor da lista é: {min(num)}')
