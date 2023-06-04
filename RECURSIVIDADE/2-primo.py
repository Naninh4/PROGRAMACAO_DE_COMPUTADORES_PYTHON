
def primo(num, cont=1, divisores=1):
    if cont >= num:
        if divisores == 2:
            return True
        else:
            return False
    if num % divisores == 0:
        return primo(num, cont +1, divisores + 1) 
    else:
        return primo(num,cont +1, divisores)

print(primo(7))

    