nota1 = float(input('Insira sua nota: '))
nota2 = float(input('Insira sua segunda nota: '))
media = (nota1 + nota2)/2
print(media)

if media >= 6:
    print('Aprovado')
else:
    print('Reprovado')