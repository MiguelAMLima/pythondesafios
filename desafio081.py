# Crie um programa que vai ler vários números e colocá-los em uma lista.
# Depois disso, mostre: A) Quantos números foram digitados. B) A lista
# de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado
# e está ou não na lista.
listanum = []
while True:
    listanum.append(float(input(f'Digite o {len(listanum) + 1}º valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
listanum.sort(reverse=True)
print('-=' * 30)
print(f'Foram digitados {len(listanum)} valores.')
print(f'Lista de valores em ordem decrescente: {listanum}')
if 5 in listanum:
    print(f'O valor 5 foi digitado e adicionado à lista {listanum.count(5)}x')
else:
    print('O valor 5 não foi digitado, portanto, não está na lista.')
