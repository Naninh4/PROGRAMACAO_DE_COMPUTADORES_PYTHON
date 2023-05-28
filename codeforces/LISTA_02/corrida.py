metros_correr, comprimento_pista = map(int, input().split())

ponto_termino = metros_correr % comprimento_pista

print(ponto_termino)