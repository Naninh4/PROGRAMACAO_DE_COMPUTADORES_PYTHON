# Escreva uma função recursiva que receba uma lista de números inteiros e mostre a soma dos
# números pares da lista.
# Assinatura da função: def soma_pares(lista)

def soma_pares(lista, cont=0):
    if cont == len(lista):
        return 0
    if lista[cont] % 2 == 0:
        return lista[cont] + soma_pares(lista, cont+1)
    else:
        return soma_pares(lista,cont+1)
    
lista = [2,4,8,10,12,7]
print(soma_pares(lista))

