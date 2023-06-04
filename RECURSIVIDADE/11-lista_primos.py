def primo(num, cont=1, divisores=1):
    if cont >= num:
        if divisores == 2:
            return True
        else:
            return False
    if num % divisores == 0:
        return primo(num, cont +1, divisores + 1) 
    else:
        return primo(num,cont +1, divisores)
def primos(lista, cont):
    if cont == 0:
        return lista_primos
    if primo(lista[cont]) == True:
        lista_primos.append(lista[cont])
        return primos(lista, cont-1)
    else:
        return primos(lista, cont-1)
    
lista_primos =[]
lista = [8,2,10,1,12]
print(primos(lista, (len(lista)-1)))
