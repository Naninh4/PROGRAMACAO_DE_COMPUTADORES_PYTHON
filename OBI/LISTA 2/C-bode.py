tentativas = int(input())
contem_carro =0

ganhou_carro =0
for x in range(0,tentativas):
    contem_carro = int(input())
    if contem_carro != 1:
        ganhou_carro +=1
print(ganhou_carro)