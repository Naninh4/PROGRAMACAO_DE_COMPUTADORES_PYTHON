nums = list(map(float,input().split()))
soma = sum(nums)
qtd = len(nums)
media = soma/qtd
print("{:.1f}".format(media))

# versão manual

nums = list(map(float,input().split()))

for i in nums:
    soma = soma + i
    qtd +=1

media = soma/qtd

print("{:.1f}".format(media))
