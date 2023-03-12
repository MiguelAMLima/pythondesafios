# Desenvolva um programa que leia o comprimento de três retas e diga ao
# usuário se elas podem ou não formar um triângulo
print('-=' * 12)
print('Analisador de Triângulos')
print('-=' * 12)
reta1 = float(input('Informe o comprimento da primeira reta em metros: '))
reta2 = float(input('Informe o comprimento da segunda reta em metros: '))
reta3 = float(input('Informe o comprimento da terceira reta em metros: '))
if ((reta1 + reta2) > reta3) and ((reta1 + reta3) > reta2) and ((reta2 + reta3) > reta1):
    print('As três retas podem formar um triângulo!')
else:
    print('As três retas não podem formar um triângulo!')
