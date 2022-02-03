nota1 = float(input('primmeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print('tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1 , nota2, media))
if media < 5:
    print('o alno está reprovado ')
elif media >= 5 and media <=7:
    print('o aluno está em recuperação ')
elif media >= 7:
    print('o aluno está aprovado')
