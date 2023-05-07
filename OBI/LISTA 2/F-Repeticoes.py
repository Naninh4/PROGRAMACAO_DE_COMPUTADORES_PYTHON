dna = input()
lista = list(dna)
sequencia=0
elemento_atual = lista[0]
maior_sequencia = 1
for i in range(0,len(lista)):
    if lista[i] == elemento_atual:
        sequencia +=1
        if sequencia > maior_sequencia:
            maior_sequencia = sequencia
    else:
        sequencia = 1
        elemento_atual = lista[i]

print(maior_sequencia)