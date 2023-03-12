# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Qual foi a distância da viagem em Km? '))
if distancia <= 200:
    preco = int(distancia) * 0.50
    print('O preço da passagem para {:.2f}Km é de R${:.2f}'.format(distancia, preco))
else:
    preco = int(distancia) * 0.45
    print('O preço da passagem para {:.2f}Km é de R${:.2f}'.format(distancia, preco))
