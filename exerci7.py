print('\n\nBom dia. Você será submetido a 5 perguntas sobre um crime: \n ')
print('___________________________________________\n')
print('****|Digite "S" para sim e "N" para não!|****')
print('___________________________________________\n')
contador = 0
resposta = 0
s = 0 
n = 0
for contador in range(0,1):
        resposta = (input('\nVocê telefonou para vitima? \n'))
        if resposta.lower() == 's':
            s += 1
        elif resposta == 'n':
            s == 0 
        resposta = (input('Esteve no local do crime? '))
        if resposta.lower() == 's':
            s += 1
        elif resposta == 'n':
            s == 0 
        resposta = (input('Mora perto da vitima? '))
        if resposta.lower() == 's':
            s += 1
        elif resposta == 'n':
            s == 0 
        resposta = (input('Devia para a vítima? '))
        if resposta.lower() == 's':
            s += 1
        elif resposta == 'n':
            s == 0 
        resposta = (input('Ja trabalhou para a vitima? '))
        if resposta.lower() == 's':
            s += 1
        elif resposta == 'n':
            s == 0 
        print(s)
        if s == 2:
                print('Você é suspeito!\n\n\n\n\n')
        elif s > 2 and s < 5:
                print('Cúmplice!\n\n\n\n\n')
        elif s == 5:
                print('Assassino!\n\n\n\n\n')
        else: 
            print("Você é inocente!\n\n\n\n\n")    