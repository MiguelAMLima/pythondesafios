# Crie um programa que simule o funcionamento de um caixa eletrônico. No
# início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('=' * 41)
print(f"{'BANCO STYNGEL':^41}")
print('=' * 41)
valor = int(input('Qual valor inteiro será sacado? R$'))
print('=' * 41)
print(f'O valor de R${valor} será sacado em:')
cinquenta = vinte = dez = um = 0
if valor / 50 >= 1:
    cinquenta = int(valor / 50)
    valor = valor % 50
    print(f'{cinquenta} cédulas de R$50.')
if valor / 20 >= 1:
    vinte = int(valor / 20)
    valor = valor % 20
    print(f'{vinte} cédulas de R$20.')
if valor / 10 >= 1:
    dez = int(valor / 10)
    valor = valor % 10
    print(f'{dez} cédulas de R$10.')
if valor / 1 >= 1:
    um = int(valor / 1)
    print(f'{um} cédulas de R$1.')
print('=' * 41)
