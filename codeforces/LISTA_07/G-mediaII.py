qtd_notas = int(input())

notas = list(map(int, input().split()))
media = sum(notas)/len(notas)
qtd_abaixo = []
qtd_acima = []
for _ in notas:
    if _ >= media:
        qtd_acima.append(_)
    if _ < media:
        qtd_abaixo.append(_)

print(f'{media:.1f}')
print(len(qtd_abaixo), *qtd_abaixo, sep=" ")
print(len(qtd_acima), *qtd_acima, sep=" ")