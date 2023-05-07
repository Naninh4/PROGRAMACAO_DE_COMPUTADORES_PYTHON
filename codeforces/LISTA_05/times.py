j1 = int(input())
j2 = int(input())
j3 = int(input())
j4 = int(input())

dif1 = abs((j1 + j2) - (j3 + j4))
dif2 = abs((j1 + j3) - (j2 + j4))
dif3 = abs((j1 + j4) - (j3 + j2))



lista = [dif1,dif2,dif3]
lista.sort()
print(lista[0])
