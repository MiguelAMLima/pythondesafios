# Faça um programa que leia um ângulo qualquer e mostre na tela o
# valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Informe o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o ângulo de {} temos:\nSeno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'
      .format(angulo, seno, cosseno, tangente))
