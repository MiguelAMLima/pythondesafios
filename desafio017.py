# Faça um programa que leia o comprimento do cateto oposto e do cateto
# adjacente de um triângulo retângulo, calcule e mostre o comprimento
# da hipotenusa.
"""oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o comprimento do cateto adjacente '))
hipotenusa = ((oposto ** 2) + (adjacente ** 2)) ** (1/2)
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(oposto, adjacente, hipotenusa))"""

from math import hypot
oposto = float(input('Informe o comprimento do cateto oposto: '))
adjacente = float(input('Informe o omprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('Cateto oposto: {}\nCateto adjacente: {}\nHipotenusa: {}'.format(oposto, adjacente, hipotenusa))
