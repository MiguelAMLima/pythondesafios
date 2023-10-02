# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma listagem
# de preços, organizando os dados em forma tabular.
produtos = ('Cerveja (500ml)', 6.20,
            'Água (1,5L)', 3.40,
            'Bananas (1kg)', 5.70,
            'Laranjas (1kg)', 4.70,
            'Maçãs (1kg)', 8.70,
            'Cebolas (1kg)', 5.10,
            'Batatas (1kg)', 5.20,
            'Tomates (1kg)', 7.70,
            'Leite (1L)', 5.30,
            'Arroz (1kg)', 5.80)
print('-' * 42, f'{"LISTAGEM DE PREÇOS":^42}', '-' * 42, sep='\n')
for count in range(0, len(produtos)):
    if count % 2 == 0:
        print(f'{produtos[count]:.<34}', end='')
    else:
        print(f'R${produtos[count]:>6.2f}')
print('-' * 42)
