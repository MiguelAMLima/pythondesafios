# Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
# a digitar valores.
num = int(input('Digite um valor inteiro: '))
soma = maior = menor = num
cont = 1
continuar = str(input('Deseja continuar digitando valores? [S/N]: ')).strip().upper()[0]
while continuar != 'N':
    num = int(input('Digite um valor inteiro: '))
    soma += num
    cont += 1
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    continuar = str(input('Deseja continuar digitando valores? [S/N]: ')).strip().upper()[0]
print(f'\nO maior valor digitado foi: {maior}\nO menor valor digitado foi: {menor}'
      f'\nA média entre os {cont} valores digitados foi: {(soma / cont):.2f}')
