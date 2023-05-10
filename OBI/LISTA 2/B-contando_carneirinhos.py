qtd_testes = int(input())
carneirinhos = []
car_dif = []
lista_car_difs = []

for x in range(0,qtd_testes):
    qtd_carneirinhos = int(input())
    carneirinhos = list(map(int,input().split()))
    car_dif = list(set(carneirinhos))
    lista_car_difs.append(len(car_dif))
    car_dif =[]
    carneirinhos =[]
    
print(*lista_car_difs, sep="\n")