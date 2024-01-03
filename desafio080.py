# Crie um programa onde o usuário possa digitar 5 valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()). No final, mostre a lista ordenada na tela.
listanum = []
for c in range(1, 6):
    valor = float(input(f'Digite o {c}º valor: '))
    if c == 1 or valor > listanum[-1]:
        listanum.append(valor)
        print(f'{valor} foi adicionado ao fim da lista.')
    else:
        pos = 0
        while pos < len(listanum):
            if valor <= listanum[pos]:
                listanum.insert(pos, valor)
                print(f'{valor} adicionado na posição {pos} da lista.')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram: {listanum}')
