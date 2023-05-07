idade_mae = int(input())
idade_f1 = int(input())
idade_f2 = int(input())

idade_f3 = abs((idade_f1 + idade_f2) - idade_mae)
lista = [idade_f1, idade_f2, idade_f3]
lista.sort()

print(lista[-1])