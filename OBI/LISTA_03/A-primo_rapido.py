import math
divisores = 0
saida = []
for i in range(int(input())):
    num = int(input())
    if num <=1:
        saida.append("N")
    else:
        for x in range(2,int(math.sqrt(num))+1):
            if num%x == 0:
                divisores +=1
        if divisores == 0:
            saida.append("S")
        else:
            saida.append("N")
        divisores = 0
print(*saida, sep="\n")