# Crie um algoritmo que leia um número e mostre o seu
# dobro, tripo e raiz quadrada.
n = float(input('Digite um número: '))
print('O dobro de {} vale {}.'
      '\nO triplo de {} vale {}.'
      '\nA raiz quadrada de {} é igual a {:.3f}.'
      .format(n, n*2, n, n*3, n, pow(n, (1/2))))
