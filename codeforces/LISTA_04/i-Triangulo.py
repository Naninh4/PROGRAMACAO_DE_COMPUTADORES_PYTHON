a,b,c = map(int, input().split())

pitagoras = [a,b,c]
pitagoras.sort()

if a > abs(b - c) and a < (b + c):
    if b > abs(a - c) and b < (a + c):
        if c > abs(b - a) and c < (b + a):
            if pitagoras[2]**2 < (pitagoras[0] ** 2) + ( pitagoras[1] ** 2):
                print("a")
            elif pitagoras[2]**2 == (pitagoras[0] ** 2) + ( pitagoras[1] ** 2):
                print("r")
            elif pitagoras[2]**2 > (pitagoras[0] ** 2) + ( pitagoras[1] ** 2):
                print("o")
    
        else:
            print("n")
    else:
        print("n")
else:
    print("n")