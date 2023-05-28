import timeit

code = '''
carneirinhos = []
lista_car_difs = []
cont = 0
for x in range(10000):  # Altere o valor para gerar uma entrada maior
    qtd_carneirinhos = 3  # Altere o valor para gerar uma entrada maior
    for x in list(1000000000,225555577,5666666777):
        if x not in carneirinhos:
            cont += 1
            carneirinhos.append(x)
    lista_car_difs.append(cont)
    cont = 0
    carneirinhos.clear()
for x in lista_car_difs:
    print(x)
'''

execution_time = timeit.timeit(stmt=code, number=1)
print(f"Tempo de execução: {execution_time} segundos")
