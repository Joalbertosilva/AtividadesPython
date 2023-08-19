nota1 = float(input('Insira sua primeira nota: '))
nota2 = float(input('Insira sua segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media <= 9:
    print('Aprovado!')
elif media == 10:
    print('Aprovado com distinção!')
else:
    print('Reprovado!')