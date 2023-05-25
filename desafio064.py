# Crie um programa que leia vários números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles.
valor = soma = cont = 0
while valor != 999:
    valor = int(input('Informe um valor para a soma [Parada: 999]: '))
    if valor != 999:
        soma += valor
        cont += 1
print(f'Você informou {cont} valores e a soma entre eles é {soma}.')
