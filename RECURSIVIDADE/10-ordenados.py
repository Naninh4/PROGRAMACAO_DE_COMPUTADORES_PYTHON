def ordenados(lista, cont, ordenada = False):
    #condição de parada
    if cont == (len(lista)-1):
        return ordenada
    #condicao de execução
    if lista[cont] < lista[cont+1]:
        #recursividade
        return ordenados(lista,cont+1, ordenada=True)
    else:
        #recursividade
       return ordenados(lista,cont+1, ordenada=False)
    
lista = [8,9,10,11,15]
print(ordenados(lista, 0,))
