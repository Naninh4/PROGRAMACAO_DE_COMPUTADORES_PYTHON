qtd_notas = int(input())

notas = list(map(int, input().split()))
media = sum(notas)/len(notas)
qtd_abaixo = 0
qtd_acima = 0
for _ in notas:
    if _ >= media:
        qtd_acima +=1
    if _ < media:
        qtd_abaixo+=1

print(f'{media:.1f}')
print(qtd_abaixo)
print(qtd_acima)