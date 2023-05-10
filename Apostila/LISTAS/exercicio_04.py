# • Desempacotar listas
# • print(*lista)
# • Usado como parâmetros de funções
# • Passa cada elemento da lista como um parâmetro para
# a função
l=list(map(int,input().split()))
print(*l)

l = list(map(int, input().split()))
print(*l, sep=", ")

# saida: 1, 2, 3, 4, 5, 6