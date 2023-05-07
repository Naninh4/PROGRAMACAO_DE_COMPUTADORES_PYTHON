red, green, blue = map(int,input().split())

pa = [red,green,blue]
pa.sort()

if abs(pa[2] - pa[1]) == abs(pa[1] - pa[0]):
    print("S")
else:
    print("N")