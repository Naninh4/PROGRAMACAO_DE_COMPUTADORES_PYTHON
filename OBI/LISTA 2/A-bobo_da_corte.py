candidatos = int(input())
voto_candidatos = []
for x in range(0,candidatos):
    voto_candidatos.append(int(input()))

maior = max(voto_candidatos)
if voto_candidatos[0] == maior:
    print("S")
else:
    print("N")