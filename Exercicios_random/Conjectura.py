n= 0
r = 0
def primo(num):
    divisores =0
    for i in range(1,(num+1)):
        if num % i == 0:
            divisores +=1
            print(i)
    if divisores <= 2:
      return True
    elif divisores > 2:
        return False

while True:
    r = n**2 + n + 41
    if primo(r) == False:
        print(f"Encontrei um contra exemplo, se n = {n}, então n^2 + n + 41 = {r} que não é primo.")
        exit()
    n+=1
    