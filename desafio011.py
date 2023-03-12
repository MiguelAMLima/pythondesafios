# Faça um programa que leia a largura e a altura de
# uma parede em metros, calcule sua área e a
# quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta 2m².
larg = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
area = larg * alt
tinta = area / 2
print('A área da parede é de {}m² e a quantidade de tinta necessária para pintá-la é de {} litros!'
      .format(area, tinta))
