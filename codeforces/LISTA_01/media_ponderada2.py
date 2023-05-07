num1,num2= map(int, input().split())
p1,p2= map(int, input().split())

media = ((num1 * p1) + (num2 * p2))/(p1 + p2)
print(int(media))