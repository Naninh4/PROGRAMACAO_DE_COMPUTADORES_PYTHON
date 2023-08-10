lista = []
diferentes = 1
for x in range(0, int(input())):
    lista.append(int(input()))
for i in range(0, (len(lista) - 1)):
    if i == (len(lista) -1):
        if lista[i] != 1:
            diferentes+=1
            break
    elif lista[i] != lista[i+1]:
        diferentes+=1
print(diferentes)
