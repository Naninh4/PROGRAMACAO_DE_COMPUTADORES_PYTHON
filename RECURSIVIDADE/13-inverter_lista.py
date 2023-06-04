# 13. Escreva uma função recursiva que receba uma lista l e inverta a ordem dos elementos da
# lista, trocando o primeiro com o último, o segundo com o penúltimo, o terceiro com com
# antepenúltimo, até que a lista fique totalmente invertida.
# Se a função receber a lista [1,2,3,4,5], deve retornar a lista [5,4,3,2,1] .
# Assinatura da função: def inveter_lista(lista)
# Dica: Defina parâmetros para auxilar no indece_finalrole da recursividade.

def inverter_lista(lista, start=0, end=None):
    if end is None:
        end = len(lista) - 1
    
    if start >= end:
        return lista

    lista[start], lista[end] = lista[end], lista[start]  # Troca os elementos de posição
    return inverter_lista(lista, start + 1, end - 1)
lista = [1,2,3,4,5]
print(inverter_lista(lista))