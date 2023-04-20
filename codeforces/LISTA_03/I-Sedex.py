diametro_bola = int(input())
altura, largura, profundidade =  map(int,input().split())

if (diametro_bola <= altura) and (diametro_bola <= largura) and (diametro_bola <= profundidade):
    print("S")
else:
    print("N")