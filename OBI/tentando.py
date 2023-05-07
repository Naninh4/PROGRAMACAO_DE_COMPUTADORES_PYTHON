x,y = map(int,input().split())
a, b=  map(int,input().split())
c, d=  map(int,input().split())

if ((a + c) <= x) and ((b <= y) and (d <= y)):
    print("S")
elif((a + d) <= x) and ((b <= y) and (c <= y)):
    print("S")
elif((b + c) <= x) and ((a <= y) and (d <= y)):
    print("S")
elif((b + d) <= x) and ((a <= y) and (c <= y)):
    print("S")
elif ((a + c) <= y) and ((b <= x) and (d <= x)):
    print("S")
elif((a + d) <= y) and ((b <= x) and (c <= x)):
    print("S")
elif((b + c) <= y) and ((a <= x) and (d <= x)):
    print("S")
elif((b + d) <= y) and ((a <= x) and (c <= x)):
    print("S")
else:
    print("N")
