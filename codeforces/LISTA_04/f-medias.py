a11, a21 = map(int,input().split())
a12, a22 = map(int,input().split())
p1,p2 = map(int,input().split())

if (((a11*p1) + (a21 * p2))// (p1 + p2)) >= (((a12*p1) + (a22 * p2))// (p1 + p2)):
    print(1)
elif (((a11*p1) + (a21 * p2))// (p1 + p2)) < (((a12*p1) + (a22 * p2))// (p1 + p2)):
    print(2) 