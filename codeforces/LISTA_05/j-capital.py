a,b,c,d = map(int, input().split())

lista=[a,b,c,d]
lista.sort()
if (lista[3]/lista[0] == lista[2]/lista[1]) or (lista[3]/lista[1] == lista[2]/lista[0]) or (lista[3]/lista[2] == lista[1]/lista[0]) :
    print("S")
else:
    print("N")