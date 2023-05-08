# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores.
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input(f'Informe o ano de nascimento da {c}ª pessoa: '))
    if (date.today().year - nascimento) >= 21:
        maior += 1
    else:
        menor += 1
print(f'Nº de pessoas que atingiram a maioridade: {maior}\nNº de pessoas que NÃO atingiram a maioridade: {menor}')
