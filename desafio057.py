# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
# 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um
# valor correto.
s = str(input('Informe o sexo da pessoa [M/F]: ')).strip().upper()
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor, informe o sexo da pessoa [M/F]: ')).strip().upper()
print(f'O sexo informado foi: {s}')
