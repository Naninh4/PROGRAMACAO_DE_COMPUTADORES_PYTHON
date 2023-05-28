saida =[]
for x in range(0,int(input())):
    a, b = map(int, input().split())
    if max(a,b) > (2*min(a,b)) or (a + b)%3!=0:
        saida.append("NO")
    else:
        saida.append("YES")
print(*saida, sep="\n")