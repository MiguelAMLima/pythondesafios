# Crie um programa que leia quanto dinheiro uma
# pessoa tem na carteira e mostre quantos
# dólares ela pode comprar. (dólar = 3,27)
real = float(input('Quantos reais você tem na carteira? R$'))
print('Com R${:.2f} você pode comprar U${:.2f}.'.format(real, real/3.27))
