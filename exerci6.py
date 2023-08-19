print('Em que horário você estuda?\n')
print('Se você estuda no horario matutino digite "M": \n')
print('Se você estuda no horario vespertino digite "V": \n ')
print('Se você estuda no horario noturno digite "N": \n')

horario = input('Escolha uma opção: ')

match horario.lower():
    case 'm':
        print('Bom dia!')
    case 'v':
        print('Boa tarde!')
    case 'n':
        print('Boa noite!')
    case _:
        print('Opção inválida!')

