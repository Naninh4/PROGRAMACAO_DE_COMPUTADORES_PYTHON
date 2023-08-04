a, b, c = map(int, input().split())
d, e, f = map(int, input().split())
aux =0
frango = d - a
bife = e - b
massa = f - c
lista = [frango, bife, massa]

for i in lista:
    if i > 0:
        aux = aux + i

print(aux)
