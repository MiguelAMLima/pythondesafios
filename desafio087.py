# Aprimore o desafio anterior, mostrando no final: A) A soma de todos
# os valores pares digitados. B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = soma3col = maior2lin = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a posição {i}, {j}: '))
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
        if j == 2:
            soma3col += matriz[i][j]
        if i == 1:
            if j == 0 or matriz[i][j] > maior2lin:
                maior2lin = matriz[i][j]
print('-=' * 30)
print(f'{"Matriz:":^24}')
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[{matriz[i][j]:^6}]', end='')
    print()
print('-=' * 30)
print(f'Soma de valores pares: {somapar}')
print(f'Soma de valores da 3ª coluna: {soma3col}')
print(f'Maior valor da 2ª linha: {maior2lin}')
