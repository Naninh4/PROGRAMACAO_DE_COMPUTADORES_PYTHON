# Escreva uma função recursiva que receba uma lista l de números inteiros e um número inteiro
# x. A função deve retornar quantas vezes x ocorre na lista.
# Assinatura da função: def ocorrencias(lista, x)

def ocorrencias(lista, x,cont=0):
    if cont == (len(lista) -1):
        return 0
    if x == lista[cont]:
        return 1 + ocorrencias(lista,x,cont+1)
    else:
        return ocorrencias(lista,x,cont+1)
lista = [8,2,2,2,12]
print(ocorrencias(lista, 2))
