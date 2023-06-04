# 8. Escreva uma função recursiva que receba uma lista de números inteiros e retorne o índice do
# maior elemento.
# Assinatura da função: def indice_do_maior(lista)
def indice_do_maior(lista,cont, maior):
    if cont == (len(lista)):
        return maior
    if lista[cont] >= maior:
        maior = lista[cont]
        cont+=1
        return indice_do_maior(lista,cont, maior)
    else:
        cont+=1
        return indice_do_maior(lista, cont, maior)

lista = [3,6,1,5,3,6,5,3,2,9]
print(indice_do_maior(lista,0,0))
      
