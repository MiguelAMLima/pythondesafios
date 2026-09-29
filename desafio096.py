# Faça um programa que tenha uma função chamada area(),
# que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}m x {comp}m é de {a}m²')


print('  Controle de Terrenos')
print('-' * 24)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
