eixo_x, eixo_y = map(int, input().split())

if eixo_x <= 432 and eixo_x >= 0:
    if eixo_y <= 468 and eixo_y >= 0:
        print("dentro")
    else:
        print("fora")
else:
    print("fora")
