# Crie um programa que leia uma frase qualquer e diga se ela é um
# palíndromo, desconsiderando os espaços. Ex: Apos a sopa.
frase = str(input('Digite uma frase sem acentuação: ').upper())
frase = ''.join(frase.split())
inverso = ''
for c in range(len(frase) - 1, -1, -1):
    inverso = inverso + frase[c]
print(f'O inverso de {frase} é {inverso}')
if frase == inverso:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada NÃO é um PALÍNDROMO!')
