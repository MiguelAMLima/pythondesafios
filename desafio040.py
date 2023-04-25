# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida: -Média
# abaixo de 5.0: "reprovado"; -Média entre 5.0 e 6.9: "recuperação"; -Média
# 7.0 ou superior: "aprovado".
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Aluno teve média {:.1f} e está reprovado!'.format(media))
elif 5 <= media < 7:
    print('Aluno teve média {:.1f} e está em recuperação!'.format(media))
else:
    print('Aluno teve média {:.1f} e está aprovado! parabéns!!!'.format(media))
