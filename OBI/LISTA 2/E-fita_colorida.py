tamanho_lista = int(input())
fita = list(map(int, input().split()))

posicoes_0 = []
cont = 0
#descobrindo a posição dos zeros
for x in fita:
    if x == 0:
        posicoes_0.append(cont)
    cont+=1
cont=0
aux=0
cores =[]
for i in fita:
    if i == -1:
        diferenca=[]
        for x in posicoes_0:
            diferenca.append(abs(cont - x))
        if min(diferenca) >= 9:
            cores.append(9)
            diferenca=[]
        else:
            cores.append(min(diferenca))
            diferenca=[]
    cont+=1

for x in posicoes_0:
    cores.insert(x,0)
print(*cores)
