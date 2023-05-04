# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços. Ex: Apos a sopa.
frase = str(input('Digite uma frase sem acentuação: ').lower())
frase = ''.join(frase.split())
frase2 = ''
for c in range(len(frase) - 1, -1, -1):
    frase2 = frase2 + frase[c]
if frase == frase2:
    print('A frase digitada é um PALÍNDROMO.')
else:
    print('A frase digitada NÃO é um PALÍNDROMO.')
