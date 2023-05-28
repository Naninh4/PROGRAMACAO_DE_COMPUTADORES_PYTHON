def media_ponderada(v1, p1, v2, p2):
    return ((v1*p1) + (v2*p2) )/ (p1 + p2)
v1, v2 = map(int, input().split())
p1, p2 = map(int, input().split())

print(media_ponderada(v1,p1,v2,p2))
