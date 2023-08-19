senha = 'joaoalberto'
contador = 0
while contador < 4:
    senha = input('Digite a senha: ')
    contador += 1
    if senha == 'joaoalberto':
        print('Acesso Permitido')
        break;
    elif contador == 3:
        print('Você só tem mais uma tentativa!')
    elif contador == 4:
        print('você foi bloqueado!')
    else:
        print('Senha incorreta')
        
    