numero1 = int(input('Insira um número: '))
numero2 = int(input('insira um número: '))
numero3 = int(input('Insira um número: '))

if numero1 > numero2:
    print('O número {} é maior que o número {} e {}'.format (numero1, numero2, numero3))
elif numero2 > numero3:
    print('O número {} é maior que o número {} e {}'.format(numero2, numero1, numero3))
elif numero1 == numero2 and numero3 == numero1:
    print('Os números {}, {} e {} são iguais'.format(numero1, numero2, numero3))
else:
    print('O número {} é maior que os numeros {} e {}'.format(numero3, numero2, numero1))
