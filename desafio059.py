# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar ; [2] multiplicar ; [3] maior ; [4] novos números ; [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
opcao = 0
valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))
while opcao != 5:
    print('\nEscolha uma opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa')
    opcao = int(input('Opção escolhida: '))
    if opcao == 1:
        print(f'\nA soma entre {valor1} e {valor2} é {valor1 + valor2}')
    elif opcao == 2:
        print(f'\nA multiplicação entre {valor1} e {valor2} resulta em {valor1 * valor2}')
    elif opcao == 3:
        if valor1 > valor2:
            print(f'\nO maior valor é: {valor1}')
        elif valor2 > valor1:
            print(f'\nO maior valor é: {valor2}')
        else:
            print('\nOs valores são iguais!')
    elif opcao == 4:
        valor1 = float(input('\nDigite o novo primeiro valor: '))
        valor2 = float(input('Digite o novo segundo valor: '))
    elif opcao != 5:
        print('\nOpção inválida, tente novamente:')
    sleep(3)
print('\nFim do programa!')
