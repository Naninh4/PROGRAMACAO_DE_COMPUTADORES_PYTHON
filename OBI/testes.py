# tabuleiro = []

# for linhas in range(1,9):
#     linha = [] #a linha precisa ser esvaziada muié, se ligue viu.
#     for colunas in range(1,9):
#         linha.append(f"{linhas} {colunas}")
#     tabuleiro.append(linha)
# for linha in tabuleiro:
#     print(linha)
# cont = 0
# # diferenca_x = abs(x1 - x2)
# # diferenca_y = abs(y1 - y2)

base_folha, altura_folha = map(int,input().split())
base_foto1, altura_foto1 =  map(int,input().split())
base_foto2, altura_foto2 =  map(int,input().split()) 

area_foto1 = base_foto1 * altura_foto1
area_foto2 = base_foto2 * altura_foto1
area_folha = base_folha * altura_folha

if area_foto1 + area_foto2 <= area_folha:
    print("S")
else:
    print("N")