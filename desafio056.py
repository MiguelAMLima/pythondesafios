# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No
# final do programa, mostre: a média de idade do grupo, qual é o nome
# do homem mais velho e quantas mulheres têm menos de 20 anos.
idadetotal = 0
velhoidade = 0
velhonome = ''
contmulher20 = 0
for c in range(1, 5):
    print('-' * 5, f' {c}ª PESSOA ', '-' * 5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idadetotal += idade
    if sexo in 'Mm' and idade > velhoidade:
        velhoidade = idade
        velhonome = nome
    if sexo in 'Ff' and idade < 20:
        contmulher20 += 1
media = idadetotal / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho do grupo tem {velhoidade} anos e se chama {velhonome}.')
print(f'Ao todo são {contmulher20} mulheres com menos de 20 anos')
