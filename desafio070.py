# Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre: A) Qual é o
# total gasto na compra. B) Quantos produtos custam mais de R$1000. C) Qual
# é o nome do produto mais barato.
print('-' * 41)
print(f"{'ANÁLISE DE PRODUTOS':^41}")
print('-' * 41)
total = mais1000 = valorbarato = cont = 0
nomebarato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        mais1000 += 1
    if cont == 1 or preco < valorbarato:
        valorbarato = preco
        nomebarato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print('-' * 41)
    if continuar == 'N':
        break
print(f'Total gasto na compra: R${total:.2f}\nNúmero de produtos que custam mais de R$1000: {mais1000}'
      f'\nProduto mais barato: {nomebarato}, custando R${valorbarato:.2f}')
