# batalha naval, testanndo validade do tabuleiro
qtd_navios = int(input())

colunas = [0,0,0,0,0,0,0,0,0,0,0]
valido = []
linhas = [colunas[:] for _ in range(11)]


for _ in range(0,qtd_navios):
    o ,tm ,li ,ci = map(int, input().split()) 
    if o == 0:
        if li <= len(linhas)-1 and ci + (tm - 1) <= len(linhas[0])-1:
            for x in range(ci,ci + tm):
                if linhas[li][x] == 0:
                    linhas[li][x] = 1
                else:
                    valido.append('F')
            valido.append("V")
        else:
            valido.append('F') #parte das colunas funcionando normalmente
    if o == 1:
        if ci <= len(linhas[0])-1 and li + (tm - 1) <= len(linhas)-1:
            for y in range(li,li + tm):
                if linhas[y][ci] == 0:
                    linhas[y][ci] = 1
                else:
                    valido.append('F')
            valido.append("V")
        else:
            valido.append('F')

if 'F' in valido:
    print("N")
else:
    print("Y")

    
