comprimento_v, distancia_p = map(int, input().split())
custo_km, valor_pedagio = map(int, input().split())

qtd = comprimento_v // distancia_p

resto = comprimento_v % distancia_p

valor_viagem = (custo_km * comprimento_v) + (qtd * valor_pedagio)

print(valor_viagem)