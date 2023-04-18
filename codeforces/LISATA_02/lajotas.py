altura = int(input())
base = int(input())


lajotas_t2 = ((altura - 1)*2) + ((base - 1)*2)

lajotas_t1 = ((base * altura) + ((altura - 1) * (base - 1)))

print(lajotas_t1)
print(lajotas_t2)
