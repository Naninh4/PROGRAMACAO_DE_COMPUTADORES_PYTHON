pLitro_alcool, pLitro_gasolina, r_alcool, r_gasolina = map(float, input().split())

custo_alcool_pKM = r_alcool / pLitro_alcool 
custo_gasolina_pKM = r_gasolina / pLitro_gasolina

if custo_alcool_pKM <= custo_gasolina_pKM:
    print("G")
else:
    print("A")
    