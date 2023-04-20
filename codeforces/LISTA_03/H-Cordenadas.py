eixo_x, eixo_y = map(float, input().split())

if eixo_x == 0 and eixo_y == 0:
    print("Origem")
elif(eixo_x == 0 and (eixo_y > 0 or eixo_y < 0)):
    print("Eixo Y")
elif((eixo_x > 0 or eixo_x < 0) and eixo_y == 0):
    print("Eixo X")
elif(eixo_x > 0 and eixo_y > 0):
    print("Q1")
elif(eixo_x < 0 and eixo_y > 0):
    print("Q2")
elif(eixo_x < 0 and eixo_y < 0):
    print("Q3")
elif(eixo_x > 0 and eixo_y < 0):
    print("Q4")