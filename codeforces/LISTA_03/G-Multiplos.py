num1 = int(input())
num2 = int(input())

if num1 >= num2 and num1 % num2 == 0:
    print("Multiplos")
elif num2 >= num1 and num2 % num1 == 0:
    print("Multiplos")
else:
    print("Nao multiplos")
