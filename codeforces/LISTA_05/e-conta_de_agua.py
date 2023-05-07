consumo = int(input())

for x in range(0, (consumo+1)):
    if x <= 10:
        custo = 7
    if x > 10 and x <=30:
        custo =  custo + 1
    if x > 30 and x <=100:
        custo =  custo + 2
    if x > 100:
        custo =  custo + 5
print(custo)