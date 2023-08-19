contador = 3
total = 0
while(contador > 0):
    nota = float(input('Digite sua nota: '))
    total = total + nota
    contador = contador - 1
    total = total/3
    print(total)