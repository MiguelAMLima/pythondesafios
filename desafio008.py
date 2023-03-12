# Escreva um programa que leia um valor em metros e
# o exiba em quilômetros, centímetros, etc.
metros = float(input('Digite o valor em metros: '))
print('A medida de {}m corresponde a:'
      '\n{}km'
      '\n{}hm'
      '\n{}dam'
      '\n{}dm'
      '\n{}cm'
      '\n{}mm'.format(metros, metros/1000, metros/100, metros/10, metros*10, metros*100, metros*1000))
