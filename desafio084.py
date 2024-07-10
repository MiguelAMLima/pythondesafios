# Faça um programa que leia nome e peso de várias pessoas, guardando
# tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as
# pessoas mais leves.
peso = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(peso) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    peso.append(dados[:])
    dados.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(peso)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de: ', end='')
for p in peso:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de: ', end='')
for p in peso:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print('\n', '-=' * 30)
