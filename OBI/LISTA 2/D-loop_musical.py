lista = []
cont = 0
while True:
    picos = 0
    amostras = int(input())
    if amostras == 0:
        break
    magnitudes = list(map(int, input().split()))

    for x in range(0,amostras):
            if x==amostras-1:
                aux=0
            else:
                aux=x+1
            if magnitudes[x]>magnitudes[x-1] and magnitudes[x]>magnitudes[aux]:
                picos=picos+1
            elif magnitudes[x]<magnitudes[x-1] and magnitudes[x]<magnitudes[aux]:
                picos=picos+1

    lista.append(picos)
print(*lista, sep="\n")