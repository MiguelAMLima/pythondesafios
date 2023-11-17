# Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não
# será adicionado. No final, serão exibidos todos os valores únicos
# digitados, em ordem crescente.
listanum = []
while True:
    num = float(input('Digite um valor: '))
    if num not in listanum:
        listanum.append(num)
        print(f'Valor {num} adicionado à lista!')
    else:
        print(f'O valor {num} já foi digitado, não será adicionado à lista novamente.')
    continuar = str(input('Deseja continuar? [S/N]: ')).strip()[0]
    if continuar in 'Nn':
        break
print('=-' * 30)
listanum.sort()
print(f'Valores digitados em ordem crescente: {listanum}')
