# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip()
print('Número de vezes que a letra "a" aparece: {}'.format(frase.lower().count('a')))
print('Posição em que o "a" aparece pela primeira vez: {}'.format(frase.lower().find('a') + 1))
print('Posição em que o "a" aparece pela última vez: {}'.format(frase.lower().rfind('a') + 1))
