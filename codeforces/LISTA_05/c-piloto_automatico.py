carro_a = int(input())
carro_b = int(input())
carro_c = int(input())

if (carro_b - carro_a) == ( carro_c - carro_b ):
    print(0)
elif (carro_b - carro_a) < ( carro_c - carro_b ):
    print(1)
elif (carro_b - carro_a) > ( carro_c - carro_b ):
    print(-1)