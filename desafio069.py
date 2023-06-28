# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
# cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre: A) Quantas pessoas têm mais de 18 anos. B) Quantos homens
# foram cadastrados. C) Quantas mulheres têm menos de 20 anos.
print('-' * 41)
print(f"{'CADASTRO DE PESSOAS':^41}")
print('-' * 41)
maior18 = homem = mulher20 = pessoas = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    pessoas += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 41)
    if resp == 'N':
        break
print(f'Pessoas cadastradas: {pessoas}\nPessoas com mais de 18 anos: {maior18}\nHomens cadastrados: {homem}'
      f'\nMulheres com menos de 20 anos: {mulher20}')
