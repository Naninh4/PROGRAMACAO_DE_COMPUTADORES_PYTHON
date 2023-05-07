linhas = int(input())
colunas = int(input())
if linhas%2 == 0 and colunas%2 == 0:
    print("1")
elif (linhas%2 == 0 and colunas%2 != 0) or (linhas%2 != 0 and colunas%2 == 0) :
    print("0")
elif linhas%2 != 0 and colunas%2 != 0:
    print("1")
