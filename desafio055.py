# Faça um programa que leia o peso de cinco pessoas. No final, mostre
# qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
contmaior = 1
contmenor = 1
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            contmaior = c
        if peso < menor:
            menor = peso
            contmenor = c
print(f'O maior peso informado foi da {contmaior}ª pessoa, tendo {maior} Kg.')
print(f'O menor peso informado foi da {contmenor}ª pessoa, tendo {menor} Kg.')
