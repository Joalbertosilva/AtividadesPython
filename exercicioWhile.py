resposta = 's'

while resposta.lower() == 's':
    numero1 = int(input('Insira um numero: '))
    numero2 = int(input('Insira outro numero: '))
    soma = numero1 + numero2
    print('A soma entre os numeros {} e {} é igual a: {}'.format(numero1, numero2, soma))
    resposta = input('Voce deseja continuar (Digite S para sim, N para não)? ')
    if resposta.lower() == 'n':
        print('Encerrado!\n\n\n')
        break;