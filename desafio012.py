# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
preco = float(input('Qual o preço do produto? R$'))
desc = preco - ((5 / 100) * preco)
print('O novo preço do produto com 5% de desconto é R${:.2f}'.format(desc))
