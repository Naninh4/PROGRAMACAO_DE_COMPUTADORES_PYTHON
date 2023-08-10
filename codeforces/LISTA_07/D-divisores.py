a = int(input())
l = []
for _ in range(1,a+1):
    if( a % _ == 0):
        l.append(_)
print(*l, sep=" ")