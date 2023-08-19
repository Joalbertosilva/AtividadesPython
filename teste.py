teste = input('Escolha uma opção: ')

match teste.lower(): 
    case 'a':
        print('Letra A')
    case 'b':
        print('Letra B')
    case _:
        print('Nothing')