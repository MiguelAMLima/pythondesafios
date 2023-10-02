# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9;
# B) Em que posição foi digitado o primeiro valor 3; C) Quais foram os
# números pares.
valores = (int(input('Digite o 1º número inteiro: ')),
           int(input('Digite o 2º número inteiro: ')),
           int(input('Digite o 3º número inteiro: ')),
           int(input('Digite o 4º número inteiro: ')))
print(f'Você digitou os valores: {valores}')
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O 1º valor "3" foi digitado na {valores.index(3) + 1}ª posição.')
else:
    print('Nenhum valor "3" foi digitado')
print('Os valores pares digitados foram: ', end='')
for num in valores:
    if num % 2 == 0:
        print('(', num, sep='', end=') ')
