def sublista_sem_menor(lista):
    menor_v = min(lista)
    lista2 = [ x for x in lista]
    lista2.remove(menor_v)
    return lista2

