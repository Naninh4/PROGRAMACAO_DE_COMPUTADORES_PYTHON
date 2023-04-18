distancia = int(input())
velocidade =  int(input())

horas =  distancia // velocidade
minutos = int(((distancia / velocidade) - horas) * 60)
print("{0:02d}:{1:02d}".format(horas, minutos))


