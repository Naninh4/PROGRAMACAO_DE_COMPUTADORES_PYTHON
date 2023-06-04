# 7. Escreva uma função recursiva que receba um número inteiro n e retorne uma lista com os
# divisores de n.
# Assinatura da função: def divisores(n,k)

lista_divisores = []
def divisores(n,k):
    if k > n:
        return 0
    if n % k == 0:
        lista_divisores.append(k)
        return 1 + divisores(n,k+1)
    else:
        return divisores(n,k+1)

divisores(8,1)
print(*lista_divisores, sep=" ")