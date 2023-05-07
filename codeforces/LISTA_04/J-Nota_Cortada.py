inicio = int(input())
fim = int(input())

base = 160
altura = 70
metade = base/2

if (inicio == metade) and (fim == metade):
    print(0)
else:
    area_felix = ((inicio + fim)*altura)/2
    area_maria = ((abs(inicio - base) + abs(base - fim))*altura)/2
    if area_felix > area_maria:
        print(1)
    elif area_felix < area_maria:
        print(2)
    elif area_felix == area_maria:
        print(0)