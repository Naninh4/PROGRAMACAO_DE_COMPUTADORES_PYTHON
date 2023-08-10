import math
num = int(input())
divisores = 0
if num == 1:
    print("Nao")
else:
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            divisores +=1
    if divisores == 0:
        print("Sim")
    else:
        print("Nao")