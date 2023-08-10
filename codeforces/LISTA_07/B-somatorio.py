num  = int(input())
somatorio = 0
for x in range(0, num):
    somatorio += 1/num
    num-=1
print(f"{somatorio:.4f}")