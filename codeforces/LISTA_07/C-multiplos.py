a, b = map(int, input().split())
lista =[]
for _ in range(a,b+1):
    if (_ % a == 0):
        lista.append(_)
print(*lista, sep=" ")