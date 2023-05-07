casos = []
while True:
    x1,y1,x2,y2 = map(int, input().split())
    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        break
    elif x1 == x2 and y1 == y2:
        casos.append("0")

    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        casos.append("1")
    else:
        casos.append("2")
      
mostrar =  "\n" .join(casos)
print(mostrar)
