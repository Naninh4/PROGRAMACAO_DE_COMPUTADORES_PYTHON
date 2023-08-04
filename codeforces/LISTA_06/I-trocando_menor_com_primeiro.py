def lista_troca_menor_primeiro(lista):
    menor_v = min(lista)
    if menor_v == lista[0]:
        return 0
    elif menor_v != lista[0]:
        i = lista.index(menor_v)
        lista.remove(menor_v)
        lista.insert(i,lista[0])
        lista.remove(lista[0])
        lista.insert(0, menor_v)
        return 1

lista = list(map(int, input().split()))
print(lista_troca_menor_primeiro(lista))