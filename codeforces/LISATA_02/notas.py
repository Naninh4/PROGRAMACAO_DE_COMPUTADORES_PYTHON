nota_maxima, nota_obtida = map(float, input().split())

porcentagem_nota = (nota_obtida * 100) / nota_maxima

resultado =  (porcentagem_nota/100) *100
print(int(resultado))