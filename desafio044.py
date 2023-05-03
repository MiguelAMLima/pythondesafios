# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento: -À vista
# dinheiro/cheque: 10% de desconto; -À vista no cartão: 5% de desconto;
# -Em até 2x no cartão: preço normal; -3x ou mais no cartão: 20% de juros.
preco = float(input('Preço do produto: R$ '))
print('Escolha a forma de pagamento:\n')
print('[ 1 ] À vista no dinheiro/cheque\n[ 2 ] À vista no cartão'
      '\n[ 3 ] Em até 2x no cartão\n[ 4 ] 3x ou mais no cartão\n')
escolha = int(input('Digite o número da opção desejada: '))
if escolha == 1:
    preco = preco - (10/100 * preco)
    print('Você ganhou 10% de desconto e o valor final será de R$ {:.2f}'.format(preco))
elif escolha == 2:
    preco = preco - (5/100 * preco)
    print('Você ganhou 5% de desconto e o valor final será de R$ {:.2f}'.format(preco))
elif escolha == 3:
    print('O valor final do produto será de R$ {:.2f}'.format(preco))
elif escolha == 4:
    preco = preco + (20/100 * preco)
    print('A compra terá juros de 20% e o valor final será de R$ {:.2f}'.format(preco))
else:
    print('Você não digitou nenhuma opção válida, tente novamente!')
