numero1, distancia1, velocidade1 = map(int, input().split())
numero2, distancia2, velocidade2 = map(int, input().split())

kms1 = distancia1 /100
kms2 = distancia2 /100

tempo1 = kms1/velocidade1
tempo2 = kms2/velocidade2

if tempo1 < tempo2:
    print(numero1)
else:
    print(numero2)
